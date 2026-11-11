# Matriz de validación

| Prueba | Fuente | Resultado y alcance |
|---|---|---|
| DHCP | [Salida del router](../evidencias/parcial/router-verificacion.txt) | Dos concesiones automáticas; sin conflictos listados |
| ARP, interfaz y conectividad | [Nueva transcripción](../evidencias/parcial/router-conectividad-dhcp.txt) y salida inicial | Fa0/0 up/up; ping a .2 y .10 con 5/5 respuestas. El ping no demuestra los servicios de cada destino |
| SSH | Salida y configuración del router | SSHv2 habilitado y VTY solo SSH con login local; no se recuperó una sesión SSH del parcial |
| Port-security | [Captura](../imagenes/parcial/port-security.png) y [nueva salida](../evidencias/parcial/port-security-verificacion.txt) | Gi0/1–3 protegidos; 2 MAC como máximo y shutdown |
| Violación real | [Consola de SW-2139](../evidencias/parcial/port-security-violacion-Gi0-3.txt) | Acreditada en Gi0/3: máximo 2 MAC, contador 1, Secure-shutdown, err-disabled y eventos PSECURE_VIOLATION/ERR_DISABLE para MAC 0221.3900.0002 |
| Recuperación de port-security | [Captura](../imagenes/parcial/port-security-recuperacion-Gi0-3.png) y [salida](../evidencias/parcial/port-security-recuperacion-Gi0-3.txt) | Acreditada: Gi0/3 Secure-up / connected, 1 MAC aprendida y contador histórico 1; ping posterior desde Linux no aportado |
| AD y NPS actuales | [Captura](../imagenes/parcial/NPS-servicio-IP-clientes-grupos.png) y [diagnóstico](RADIUS.md) | IAS Running, servidor .10/24, grupos RED-NIVEL-0/5/10, cliente SW-2139 .2 habilitado; R-2139 .1 aún no listado |
| Eventos NPS anteriores | [Antecedente AAA](../antecedentes/AAA/README.md) | Aceptación 6272 y rechazo 6273 en la práctica /29; no sustituyen eventos del parcial |
| RADIUS del parcial | Running-configs de R-2139 y SW-2139 | Switch: VTY con LAB_RADIUS y autorización LAB_EXEC hacia NPS .10. Router: AAA deshabilitado. Falta acreditar autenticación con un evento actual NPS |
| Zabbix/SNMP del parcial | [Capturas de R-2139 y SW-2139](ZABBIX.md) | CPU, memoria y tráfico del router; tráfico y puertos activos del switch. IP de interfaz SNMP y prueba negativa de ACL no visibles |
| Auditoría | [Reporte](../reportes/informe-cis-R-2139.md) | Ejecución local sobre copia sanitizada; solo lectura |

## Consultas para ampliar las evidencias

El [archivo IOS](../scripts/verificacion-ios.cli) contiene solo consultas. Registrar el equipo y su fecha; revisar las salidas antes de publicarlas. No publicar comandos SNMP con la comunidad literal ni configuraciones con secretos.

La nueva salida del ensayo en Gi0/3 aporta contador, estado del puerto y registro PSECURE_VIOLATION. Se conservan las consultas anteriores con contador cero como línea base. Según la [documentación de Cisco](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9600/software/release/17-17/configuration_guide/sec/b_1717_sec_9600_cg/port_security.html), el modo shutdown pone el puerto en error-disabled cuando se produce una violación. La referencia explica el comportamiento; la evidencia de ejecución es la transcripción aportada de SW-2139. La recuperación ya cuenta con captura y transcripción: Secure-up / connected.
