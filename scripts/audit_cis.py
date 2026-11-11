"""Revision estatica de controles seleccionados; no es certificacion CIS."""
import argparse
from collections import Counter
from pathlib import Path
import re

def evaluate(config):
    lines = config.splitlines()
    globals_ = {s for s in lines if s and not s.startswith((" ", "!"))}
    blocks = {}
    current = None
    for line in lines:
        if line and not line.startswith((" ", "!")):
            current = line
            blocks[current] = []
        elif line.startswith(" ") and current:
            blocks[current].append(line.strip())
    rows = []
    def add(name, ok, detail, recommendation):
        rows.append((name, "NO EVALUABLE" if ok is None else "CUMPLE" if ok else "HALLAZGO", detail, recommendation))
    vtys = [v for k,v in blocks.items() if k.startswith("line vty ")]
    def all_vty(test):
        return all(test(v) for v in vtys) if vtys else None
    def timeout(v):
        values = [re.fullmatch(r"exec-timeout (\d+)(?: (\d+))?", s) for s in v]
        values = [m for m in values if m]
        if not values: return None
        m = values[-1]
        return 0 < int(m[1])*60+int(m[2] or 0) <= 600
    def vty_timeout():
        values = [timeout(v) for v in vtys]
        return False if False in values else None if not values or None in values else True
    add("SSHv2", "ip ssh version 2" in globals_, "Declaracion global de version", "Usar SSHv2")
    add("VTY exclusivamente SSH", all_vty(lambda v: "transport input ssh" in v), "Se revisan todos los bloques VTY presentes", "Restringir todas las VTY a SSH")
    add("HTTP deshabilitado", "no ip http server" in globals_, "Directiva explicita", "Desactivar HTTP si no es necesario")
    add("HTTPS deshabilitado", "no ip http secure-server" in globals_, "Directiva explicita", "Desactivar administracion web no necesaria")
    add("AAA habilitado", "aaa new-model" in globals_ and "no aaa new-model" not in globals_, "Estado global AAA", "Evaluar AAA y recuperacion local")
    for label,key in [("Consola","line con 0"),("AUX","line aux 0")]:
        b = blocks.get(key)
        add("Timeout "+label, timeout(b) if b is not None else None, "Limite seleccionado: 1 a 600 segundos; ausente requiere revision", "Definir expiracion de sesiones")
        add("Privilegio "+label, not any(re.fullmatch(r"privilege level 15",s) for s in b) if b is not None else None, "Solo se detecta nivel 15 explicito; no se prueba autorizacion efectiva", "Aplicar minimo privilegio")
    add("Timeout VTY", vty_timeout(), "Todas las VTY presentes; limite 600 segundos", "Definir expiracion de sesiones")
    add("ACL de entrada VTY", all_vty(lambda v: any(re.fullmatch(r"access-class \S+ in(?: vrf-also)?",s) for s in v)), "Presencia de ACL; reglas requieren revision manual", "Limitar origenes de administracion")
    credentials = [s for s in globals_ if s.startswith(("enable secret ", "username "))]
    legacy = any(re.search(r"\b(?:secret|password) (?:0|5|7)\b",s) for s in credentials)
    add("Algoritmos de credenciales", False if legacy else None, "Detecta tipos 0/5/7; otros o ausentes requieren revision", "Evaluar tipos modernos compatibles sin publicar hashes")
    communities = [s for s in globals_ if s.startswith("snmp-server community ")]
    add("Comunidades SNMP solo lectura", all(re.search(r"\sRO(?:\s|$)",s,re.I) is not None for s in communities) if communities else None, "No verifica cifrado ni consultas reales", "Evitar permisos RW; evaluar SNMPv3")
    add("SNMP restringido a gestor", False if "access-list 20 permit 10.21.39.0 0.0.0.255" in globals_ and any(re.search(r"\s20$",s) for s in communities) else None, "Regla /24 conocida demasiado amplia; otras ACL requieren revision", "Limitar a la IP autorizada del gestor")
    remote = any(re.match(r"logging (?:host \S+|\d+\.\d+\.\d+\.\d+)(?:\s|$)",s) for s in globals_)
    add("Syslog remoto", remote, "Solo presencia de destino configurado", "Centralizar registros y verificar recepcion")
    unused = blocks.get("interface FastEthernet0/1")
    add("Fa0/1 sin uso apagada", "shutdown" in unused if unused is not None else None, "Puerto sin uso segun topologia aportada", "Apagar interfaces confirmadas sin uso")
    return rows

def report(config):
    rows = evaluate(config)
    counts = Counter(r[1] for r in rows)
    out = ["# Revision de hardening — R-2139", "",
           "Metodo: analisis estatico local de la configuracion sanitizada aportada; IOS 12.4.",
           "No hubo conexion al router ni cambios de configuracion. Solo se escribio este reporte.",
           "Controles seleccionados relacionados con CIS; no es una certificacion ni porcentaje oficial.",
           "Referencia: [CIS Cisco Benchmarks](https://www.cisecurity.org/benchmark/cisco).", "",
           "| Control | Estado | Criterio / alcance | Recomendacion |", "|---|---|---|---|"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    out += ["", "; ".join(f"{k}: {counts[k]}" for k in ("CUMPLE","HALLAZGO","NO EVALUABLE")) + ".",
            "", "La comunidad SNMP es RO pero su ACL abarca toda la LAN. RO no equivale a cifrado.",
            "Los marcadores conservan el tipo 5, permitiendo identificar el algoritmo sin divulgar el hash.",
            "Los hallazgos son recomendaciones: no se aplicaron reglas de hardening.",
            "No se validan estado operativo, servicios externos, contrasenas ni alcance CIS completo."]
    return "\n".join(out) + "\n"

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("config", type=Path)
    p.add_argument("--output", required=True, type=Path)
    a = p.parse_args()
    if a.config.resolve() == a.output.resolve():
        p.error("La salida no puede reemplazar la entrada")
    text = a.config.read_text(encoding="utf-8-sig")
    if not re.search(r"(?m)^hostname \S+",text) or not re.search(r"(?m)^end\s*$",text):
        p.error("Se requiere una configuracion exportada completa con hostname y end")
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(report(text), encoding="utf-8")
    print(f"Reporte generado: {a.output}; entrada sin cambios")

if __name__ == "__main__":
    main()
