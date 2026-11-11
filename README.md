**Video demostrativo:** [Ver el segundo parcial de Seguridad de Redes en YouTube](https://youtu.be/cIgDrLqfHaw)

# Segundo Parcial — Seguridad de Redes
**Adrian Magallanes · Matrícula 2025-2139**  
Cisco IOS · Active Directory / NPS / RADIUS · DHCP · SSH · Port-security · Zabbix / SNMP · Revisión de hardening

Laboratorio desarrollado en GNS3 y VMware. Reúne las configuraciones exportadas del router **R-2139** y el switch **SW-2139**, las salidas originales disponibles del parcial, las capturas del monitoreo de ambos equipos y antecedentes de prácticas de AAA y monitoreo.

## Recorrido de la entrega

| Contenido | Acceso |
|---|---|
| Topología y direccionamiento | [Diseño de red](docs/TOPOLOGIA.md) |
| Configuraciones públicas | [Router y switch](configs/README.md) |
| Pruebas y alcance de los resultados | [Matriz de validación](docs/PRUEBAS.md) |
| Capturas y transcripciones | [Evidencias](evidencias/README.md) |
| Análisis estático de hardening | [Informe inicial](reportes/informe-cis-R-2139.md) · [Después de RADIUS](reportes/informe-cis-R-2139-post-radius.md) |
| Herramienta y reproducción | [Scripts](scripts/README.md) |
| AD, NPS y RADIUS | [Estado del parcial y preparación](docs/RADIUS.md) |
| Monitoreo SNMP del parcial | [Evidencias de R-2139 y SW-2139](docs/ZABBIX.md) |
| Metodología de auditoría | [Alcance e informe inicial](docs/AUDITORIA.md) |

## Topología del parcial

![Topología del laboratorio en GNS3](imagenes/topologia-gns3.png)

Captura original aportada por el autor. En GNS3, los nodos aparecen como **R2**, **SW-MultiCapa**, **Windows-srv**, **PC-USUARIOS-1** y **ZABBIX**; estas etiquetas visuales se conservan tal como aparecen.

### Diagrama lógico y direccionamiento

![Diagrama de la LAN del parcial](imagenes/topologia.svg)

```mermaid
flowchart TB
  R["R-2139 · Fa0/0 · 10.21.39.1/24"] ---|"Fa0/0 ↔ Gi0/0"| S["SW-2139 · VLAN 10 · 10.21.39.2/24"]
  S ---|"Gi0/1"| W["Windows AD/NPS · 10.21.39.10/24"]
  S ---|"Gi0/2"| C["PC-USUARIOS-1 · DHCP .101 durante la prueba"]
  S ---|"Gi0/3"| Z["Zabbix · IP no verificada"]
```

Los enlaces se identifican en la captura GNS3 y en las descripciones de interfaces del switch. La IP del equipo Zabbix no se deduce de la captura; el vecino ARP .131 permanece sin función confirmada.

## Resultados documentados

- Conectividad: R-2139 obtuvo 5/5 respuestas desde 10.21.39.2 y 10.21.39.10. [Transcripción](evidencias/parcial/router-conectividad-dhcp.txt).
- DHCP: concesiones automáticas **10.21.39.100 y 10.21.39.101**, tabla de conflictos vacía.
- Router: sesión SSH de **usuario-n5** desde **10.21.39.101**, privilegio **5**, con las VTY configuradas para RADIUS. NPS registró el evento **6272**, cliente **R-2139 / 10.21.39.1**, política **LAB2139-Nivel5**.
- Switch: port-security activo en Gi0/1–Gi0/3, máximo **2 MAC**, acción **shutdown**. La prueba posterior en **Gi0/3** registró **1 violación**, estado **Secure-shutdown / err-disabled** y el evento PSECURE_VIOLATION. [Evidencia de consola](evidencias/parcial/port-security-violacion-Gi0-3.txt).
- Hardening: análisis estático de solo lectura. Informe inicial: **7 conformes / 9 hallazgos**; después de incorporar RADIUS: **8 conformes / 8 hallazgos**. Se conservan la configuración y el informe iniciales.
- Zabbix: las nuevas capturas muestran CPU, memoria y tráfico de R-2139, y tráfico y estado de interfaces de SW-2139.
- AD/NPS: la nueva captura confirma IAS en Running, servidor 10.21.39.10/24, grupos RED-NIVEL-0/5/10 y cliente SW-2139 (.2) habilitado. La nueva consulta también confirma R-2139 (.1) habilitado.
- AAA: **R-2139 ya está probado** con SSH y aceptación NPS actual. SW-2139 tiene RADIUS configurado; falta su sesión de prueba y evento NPS correspondientes. Los eventos anteriores siguen separados como antecedentes.

La violación de port-security está acreditada mediante la salida real de SW-2139, aportada por el autor tras el ensayo en Gi0/3. Las capturas anteriores con contador cero se conservan como estado previo. La recuperación también está acreditada: Gi0/3 regresó a Secure-up / connected, con una MAC aprendida y conservando el contador de 1 violación.

## Estructura

```text
configs/        Running-configs sanitizados de R-2139 y SW-2139
docs/           Topología, pruebas y metodología
evidencias/     Material original del parcial
scripts/        Auditor y comandos de consulta
reportes/       Resultado reproducible de la revisión
antecedentes/   Prácticas AAA y Zabbix con su topología original
```

## Protección de datos

Se sustituyeron hashes de credenciales y comunidad SNMP por marcadores. Los secretos RADIUS de los antecedentes también están ocultos. Las copias públicas son documentación y no deben pegarse directamente en los equipos. No se incluyen imágenes IOS, discos virtuales ni respaldos privados.

El análisis usa controles seleccionados de hardening relacionados con [CIS Cisco Benchmarks](https://www.cisecurity.org/benchmark/cisco). Es una revisión adaptada al laboratorio, no una certificación CIS ni una evaluación completa de un benchmark.

## Evidencias incrustadas

### DHCP, interfaces y SSH del router

La [transcripción original](evidencias/parcial/router-verificacion.txt) y la [verificación DHCP posterior](evidencias/parcial/router-conectividad-dhcp.txt) conservan los datos de DHCP e interfaces. Sigue faltando una captura DHCP. La sesión SSH actual se muestra a continuación.

![SSH actual a R-2139: usuario-n5, privilegio 5 y origen 10.21.39.101](imagenes/parcial/SSH-R-2139-usuario-n5-nivel5.png)

[Evento NPS 6272 de aceptación](evidencias/parcial/NPS-6272-R-2139-usuario-n5.txt) · [Guardado de configuración con resultado OK](evidencias/parcial/R-2139-guardado-configuracion.txt)

### Port-security del parcial

**Antes de la prueba:** captura original con contador cero.

![Port-security de SW-2139: máximo dos MAC, shutdown y cero violaciones en la captura](imagenes/parcial/port-security.png)

**Después de la prueba en Gi0/3:** extracto de la transcripción original (no es una captura de pantalla).

```text
Port Status                : Secure-shutdown
Maximum MAC Addresses      : 2
Last Source Address:Vlan   : 0221.3900.0002:10
Security Violation Count   : 1
```

![Violación real de port-security en Gi0/3: contador 1 y err-disabled](imagenes/parcial/port-security-violacion-Gi0-3.png)

**Recuperación del puerto:**

![Gi0/3 recuperado: Secure-up y connected; contador de violaciones 1](imagenes/parcial/port-security-recuperacion-Gi0-3.png)

[Salida completa y registros de violación](evidencias/parcial/port-security-violacion-Gi0-3.txt) · [Salida de recuperación](evidencias/parcial/port-security-recuperacion-Gi0-3.txt) · [Procedimiento y recuperación](docs/PRUEBA-PORT-SECURITY.md)

### Active Directory y NPS — estado actual del parcial

![NPS activo, IP del servidor, clientes registrados y grupos actuales](imagenes/parcial/NPS-servicio-IP-clientes-grupos.png)

IAS está activo en 10.21.39.10/24 y SW-2139 (.2) está registrado. R-2139 (.1) también fue agregado y su autenticación quedó acreditada mediante una sesión SSH y el evento NPS 6272. Las nuevas capturas muestran a usuario-n5 en RED-NIVEL-5 y las políticas LAB2139-Nivel10/5/0 habilitadas con shell:priv-lvl 10/5/0. En la sesión probada se aplicó LAB2139-Nivel5; los niveles 0 y 10 no se han probado en este entorno. [Detalle de RADIUS](docs/RADIUS.md).

![Políticas LAB2139 de niveles 10 y 5](imagenes/parcial/NPS-politicas-10-5.png)

![Políticas LAB2139 de niveles 5 y 0 y cuenta usuario-n5 en RED-NIVEL-5](imagenes/parcial/NPS-politicas-5-0-usuario-n5.png)

![R-2139 registrado en NPS con IP 10.21.39.1 y Enabled True; secreto oculto](imagenes/parcial/NPS-R-2139-registrado.png)

![AAA y listas VTY del router aplicadas; conectividad con NPS](imagenes/parcial/R-2139-AAA-VTY-conectividad.png)

![NPS activo, puertos RADIUS, regla de firewall limitada y auditoría habilitada](imagenes/parcial/NPS-puertos-firewall-auditoria.png)

El evento actual confirma aceptación por **LAB2139-Nivel5**. [Transcripción completa](evidencias/parcial/NPS-6272-R-2139-usuario-n5.txt). La hora del evento corresponde al reloj de Windows Server.

### Active Directory y NPS — antecedente /29

![Grupos de Active Directory](imagenes/aaa/05-Grupos-AD.png)

![Políticas NPS y privilegios](imagenes/aaa/07-NPS-Niveles10-5-completas.jpg)

![Aceptación RADIUS de SW1 en el escenario anterior](imagenes/aaa/26a-NPS-Aceptado-SW1.png)

![Rechazo RADIUS de un usuario inexistente en el escenario anterior](imagenes/aaa/27-NPS-Rechazado-usuario-inexistente.png)

### Sesión SSH — antecedente /29

![Sesión SSH de SW1 a R1 con autenticación local](imagenes/aaa/18-R1-SSH.jpg)

### Zabbix y SNMP — R-2139 y SW-2139

![Datos recientes del router R-2139 en Zabbix](imagenes/parcial/zabbix-R-2139.png)

![Datos recientes del switch SW-2139 en Zabbix](imagenes/parcial/zabbix-SW-2139.png)

Las capturas muestran los nombres de los equipos y métricas recibidas por Zabbix. No muestran las IP de las interfaces SNMP, la comunidad ni un ensayo de bloqueo por ACL. [Detalle de resultados](docs/ZABBIX.md).

### Zabbix — antecedente A3

![Métricas del router de la práctica A3](imagenes/zabbix/zabbix-r1.png)

![Métricas del switch de la práctica A3](imagenes/zabbix/zabbix-switch.png)
