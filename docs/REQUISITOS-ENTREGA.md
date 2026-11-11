# Correspondencia con el enunciado

| Solicitud del maestro | Archivo y estado |
|---|---|
| README con propósito y descripción | README.md, preparado |
| Diagrama | imagenes/topologia.svg, incrustado en README |
| Video al inicio | [Video publicado](https://youtu.be/cIgDrLqfHaw), enlazado al inicio del README |
| Imágenes incrustadas de los requisitos | README incluye topología, port-security y nuevas capturas Zabbix de R-2139/SW-2139; DHCP y SSH del parcial solo tienen transcripción/configuración |
| Un archivo de configuración por equipo | Running-configs completos de R-2139 y SW-2139, exportados y sanitizados |
| Carpeta de imágenes y diagrama | imagenes/ organizada por procedencia |

Los antecedentes AAA y las primeras capturas Zabbix usan otra red; las nuevas capturas del parcial están identificadas en docs/ZABBIX.md. Sigue pendiente acreditar RADIUS en el entorno actual. No se presenta el repositorio como una entrega con todos los requisitos verificados mientras falten esos materiales.

La violación de port-security en Gi0/3 ya está acreditada mediante [salida de consola](../evidencias/parcial/port-security-violacion-Gi0-3.txt): contador 1, Secure-shutdown/err-disabled y registros. Falta una captura de pantalla de ese resultado si se exige evidencia visual incrustada de cada prueba.
