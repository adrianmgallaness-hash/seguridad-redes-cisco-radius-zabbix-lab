# Revision de hardening — R-2139

Metodo: analisis estatico local de la configuracion sanitizada aportada; IOS 12.4.
No hubo conexion al router ni cambios de configuracion. Solo se escribio este reporte.
Controles seleccionados relacionados con CIS; no es una certificacion ni porcentaje oficial.
Referencia: [CIS Cisco Benchmarks](https://www.cisecurity.org/benchmark/cisco).

| Control | Estado | Criterio / alcance | Recomendacion |
|---|---|---|---|
| SSHv2 | CUMPLE | Declaracion global de version | Usar SSHv2 |
| VTY exclusivamente SSH | CUMPLE | Se revisan todos los bloques VTY presentes | Restringir todas las VTY a SSH |
| HTTP deshabilitado | CUMPLE | Directiva explicita | Desactivar HTTP si no es necesario |
| HTTPS deshabilitado | CUMPLE | Directiva explicita | Desactivar administracion web no necesaria |
| AAA habilitado | CUMPLE | Estado global AAA | Evaluar AAA y recuperacion local |
| Timeout Consola | HALLAZGO | Limite seleccionado: 1 a 600 segundos; ausente requiere revision | Definir expiracion de sesiones |
| Privilegio Consola | HALLAZGO | Solo se detecta nivel 15 explicito; no se prueba autorizacion efectiva | Aplicar minimo privilegio |
| Timeout AUX | HALLAZGO | Limite seleccionado: 1 a 600 segundos; ausente requiere revision | Definir expiracion de sesiones |
| Privilegio AUX | HALLAZGO | Solo se detecta nivel 15 explicito; no se prueba autorizacion efectiva | Aplicar minimo privilegio |
| Timeout VTY | CUMPLE | Todas las VTY presentes; limite 600 segundos | Definir expiracion de sesiones |
| ACL de entrada VTY | HALLAZGO | Presencia de ACL; reglas requieren revision manual | Limitar origenes de administracion |
| Algoritmos de credenciales | HALLAZGO | Detecta tipos 0/5/7; otros o ausentes requieren revision | Evaluar tipos modernos compatibles sin publicar hashes |
| Comunidades SNMP solo lectura | CUMPLE | No verifica cifrado ni consultas reales | Evitar permisos RW; evaluar SNMPv3 |
| SNMP restringido a gestor | HALLAZGO | Regla /24 conocida demasiado amplia; otras ACL requieren revision | Limitar a la IP autorizada del gestor |
| Syslog remoto | HALLAZGO | Solo presencia de destino configurado | Centralizar registros y verificar recepcion |
| Fa0/1 sin uso apagada | CUMPLE | Puerto sin uso segun topologia aportada | Apagar interfaces confirmadas sin uso |

CUMPLE: 8; HALLAZGO: 8; NO EVALUABLE: 0.

La comunidad SNMP es RO pero su ACL abarca toda la LAN. RO no equivale a cifrado.
Los marcadores conservan el tipo 5, permitiendo identificar el algoritmo sin divulgar el hash.
Los hallazgos son recomendaciones: no se aplicaron reglas de hardening.
No se validan estado operativo, servicios externos, contrasenas ni alcance CIS completo.
