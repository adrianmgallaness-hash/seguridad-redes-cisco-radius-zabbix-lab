# Correspondencia con el enunciado

| Solicitud del maestro | Archivo y estado |
|---|---|
| README con propósito y descripción | README.md, preparado |
| Diagrama | imagenes/topologia.svg, incrustado en README |
| Video al inicio | [Video publicado](https://youtu.be/cIgDrLqfHaw), enlazado al inicio del README |
| Imágenes incrustadas de los requisitos | README incluye topología, port-security y nuevas capturas Zabbix de R-2139/SW-2139; SSH del router ya tiene captura actual; DHCP sigue con transcripción |
| Un archivo de configuración por equipo | Running-configs completos de R-2139 y SW-2139, exportados y sanitizados |
| Carpeta de imágenes y diagrama | imagenes/ organizada por procedencia |

Los antecedentes AAA y las primeras capturas Zabbix usan otra red; las nuevas capturas del parcial están identificadas en docs/ZABBIX.md. RADIUS del router ya está acreditado con sesión de nivel 5 y evento NPS 6272. Falta probar RADIUS del switch en el entorno actual. No se presenta el repositorio como una entrega con todos los requisitos verificados mientras falten esos materiales.

La violación de port-security en Gi0/3 ya está acreditada mediante [salida de consola](../evidencias/parcial/port-security-violacion-Gi0-3.txt): contador 1, Secure-shutdown/err-disabled y registros. Ya se incorporaron al README las capturas de [bloqueo](../imagenes/parcial/port-security-violacion-Gi0-3.png) y [recuperación](../imagenes/parcial/port-security-recuperacion-Gi0-3.png).
