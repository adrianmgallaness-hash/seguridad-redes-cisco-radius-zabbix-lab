# Matriz de validación

| Prueba | Fuente | Resultado y alcance |
|---|---|---|
| DHCP | [Salida del router](../evidencias/parcial/router-verificacion.txt) | Dos concesiones automáticas; sin conflictos listados |
| ARP e interfaz | Misma salida | Vecinos aprendidos y Fa0/0 up/up; no equivale a una prueba completa de conectividad entre todos los hosts |
| SSH | Salida y configuración del router | SSHv2 habilitado y VTY solo SSH con login local; no se recuperó una sesión SSH del parcial |
| Port-security | [Captura](../imagenes/parcial/port-security.png) | Gi0/1–3 protegidos; 2 MAC como máximo y shutdown |
| Violación real | Declaración del autor | Reportada como realizada; no verificable con la captura disponible, que muestra cero violaciones y Gi0/1 Secure-up |
| AD y NPS | [Antecedente AAA](../antecedentes/AAA/README.md) | Grupos y políticas, aceptación 6272 y rechazo 6273 en la práctica /29 |
| RADIUS del parcial | Configuración R-2139 | AAA deshabilitado; sin evidencia actual de autenticación NPS en este router |
| Zabbix/SNMP | [Antecedente Zabbix](../antecedentes/Zabbix/README.md) | Métricas reales de R1 y Switch en otra práctica; sin captura actual de R-2139/SW-2139 |
| Auditoría | [Reporte](../reportes/informe-cis-R-2139.md) | Ejecución local sobre copia sanitizada; solo lectura |

## Consultas para ampliar las evidencias

El [archivo IOS](../scripts/verificacion-ios.cli) contiene solo consultas. Registrar el equipo y su fecha; revisar las salidas antes de publicarlas. No publicar comandos SNMP con la comunidad literal ni configuraciones con secretos.

Para verificar una violación se requiere una salida posterior al ensayo que muestre el contador, el estado del puerto y, si existe, el registro PSECURE_VIOLATION. Según la [documentación de Cisco](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9600/software/release/17-17/configuration_guide/sec/b_1717_sec_9600_cg/port_security.html), el modo shutdown pone el puerto en error-disabled cuando se produce una violación. El comportamiento descrito por el fabricante es una referencia, no evidencia de ejecución en este laboratorio.
