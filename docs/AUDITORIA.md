# Auditoría de hardening: informe inicial y seguimiento

## Trabajo realizado

Se ejecutó [audit_cis.py](../scripts/audit_cis.py) sobre la [configuración sanitizada aportada de R-2139](../configs/R-2139-running-config.sanitized.cfg). El [reporte inicial](../reportes/informe-cis-R-2139.md) contiene **16 controles seleccionados: 7 conformes y 9 hallazgos**.

La revisión es estática y de solo lectura respecto de la configuración. El programa escribe el reporte, no se conecta al router ni aplica reglas. Los resultados no son una puntuación oficial CIS.

## Reproducción

Desde la raíz del repositorio, con Python 3.10 o posterior:

```bash
python scripts/audit_cis.py configs/R-2139-running-config.sanitized.cfg --output reportes/informe-cis-R-2139.md
python -m unittest discover -s scripts -p "test_*.py"
```

## Interpretación de los hallazgos

El archivo evaluado contiene AAA deshabilitado, consola/AUX sin expiración y privilegio 15 explícito, hashes tipo 5 (valores ocultos), VTY sin ACL de entrada, SNMP permitido para toda la LAN y ausencia de destino syslog remoto.

Los controles conformes incluyen SSHv2, VTY exclusivamente SSH, servicios HTTP/HTTPS deshabilitados, timeout VTY, comunidades SNMP de solo lectura y Fa0/1 apagada.

Encontrar estos problemas es parte del análisis inicial. No se sustituyen por resultados conformes sin una nueva configuración que los sustente.

## Si cambia la configuración

Conservar este informe como línea base. Después de aplicar y verificar cambios autorizados —por ejemplo, la incorporación de RADIUS— exportar otra copia sanitizada y generar un segundo informe con otro nombre:

```bash
python scripts/audit_cis.py configs/R-2139-post-cambios.sanitized.cfg --output reportes/informe-cis-R-2139-post-cambios.md
```

Los archivos posteriores del ejemplo solo deben crearse a partir de una exportación real. No se han recibido ni publicado todavía. Si el enunciado exige analizar sin aplicar hardening, el informe inicial responde a ese alcance; no se modifica el equipo para forzar un resultado perfecto.
