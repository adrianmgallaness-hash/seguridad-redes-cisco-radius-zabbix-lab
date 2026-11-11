# Evidencias del parcial

- [Router: ARP, DHCP, SSH e interfaces](parcial/router-verificacion.txt): extractos de la salida pegada por el autor. Se omitieron un comando PowerShell introducido por error en IOS y el bloque running-config, disponible sanitizado en configs.
- [Port-security de SW-2139](../imagenes/parcial/port-security.png): adjunto original recuperado de «Topología de red», sin alterar los resultados.

![Estado de port-security](../imagenes/parcial/port-security.png)

En la captura anterior al ensayo, Gi0/1–Gi0/3 muestran máximo 2 MAC, una aprendida por puerto, acción Shutdown y cero violaciones. Gi0/1 está Secure-up. El valor «Shutdown» es la acción configurada, no el estado operativo observado.

## Monitoreo del parcial

- [Router R-2139](../imagenes/parcial/zabbix-R-2139.png): CPU, memoria, ICMP y tráfico de Fa0/0.
- [Switch SW-2139](../imagenes/parcial/zabbix-SW-2139.png): ICMP, tráfico y estado de Gi0/0 y Gi0/1.
- [Descripción y alcance](../docs/ZABBIX.md).

Las capturas AD/NPS y las capturas Zabbix anteriores se conservan como antecedentes separados. Las nuevas imágenes no sustituyen las salidas de autenticación RADIUS o violación de port-security.

## Verificaciones adicionales aportadas

- [Conectividad y DHCP del router](parcial/router-conectividad-dhcp.txt): fragmento textual de la nueva salida, con pings exitosos a .2 y .10 y dos concesiones DHCP. Se omitieron intentos con errores de sintaxis; no se cambian los resultados.
- [Port-security antes del ensayo](parcial/port-security-verificacion.txt): transcripción de consultas, contador cero y sin coincidencias en el filtro de logs.
- [Violación real en Gi0/3](parcial/port-security-violacion-Gi0-3.txt): transcripción posterior aportada por el autor; contador 1, Secure-shutdown/err-disabled, MAC 0221.3900.0002 y registros PSECURE_VIOLATION/ERR_DISABLE. Esta salida sí acredita la violación. La recuperación está acreditada en la nueva salida y captura.

La nueva exportación del router sigue mostrando `no aaa new-model`. La respuesta ICMP de .10 no confirma por sí sola que sea el servidor NPS.

## Capturas de violación y recuperación

- [Bloqueo de Gi0/3](../imagenes/parcial/port-security-violacion-Gi0-3.png): máximo 2, contador 1, Secure-shutdown y err-disabled; incluye registros.
- [Recuperación de Gi0/3](../imagenes/parcial/port-security-recuperacion-Gi0-3.png): Secure-up / connected y contador 1.
- [Transcripción de recuperación](parcial/port-security-recuperacion-Gi0-3.txt): enlace y protocolo de línea up, una MAC aprendida.

Ambas capturas fueron aportadas por el autor; no se alteraron sus resultados.

## NPS y AD del parcial

[Captura actual de NPS](../imagenes/parcial/NPS-servicio-IP-clientes-grupos.png): IAS Running, IP 10.21.39.10/24, existencia de grupos RED-NIVEL-0/5/10 y listado de clientes. SW-2139 .2 está habilitado; R1 .129 y SW1 .130 corresponden al direccionamiento anterior. R-2139 .1 no aparece en esa consulta. No contiene secretos ni un evento de autenticación actual.

## Políticas actuales y cuenta de prueba

- [LAB2139 niveles 10 y 5](../imagenes/parcial/NPS-politicas-10-5.png): políticas habilitadas con atributos de privilegio.
- [LAB2139 niveles 5 y 0 y miembro de grupo](../imagenes/parcial/NPS-politicas-5-0-usuario-n5.png): usuario-n5 en RED-NIVEL-5.
- [Políticas AAA_Cisco anteriores](../imagenes/parcial/NPS-politicas-AAA-anteriores.png): siguen presentes en órdenes 1–3.
- [Listado de clientes previo al alta del router](../imagenes/parcial/NPS-clientes-antes-alta-router.png): no aparece todavía R-2139 .1.

Las capturas no son eventos de autenticación. No se atribuye una política efectiva o una aceptación al router sin la prueba correspondiente.

## Router registrado en NPS

[Captura del alta de R-2139](../imagenes/parcial/NPS-R-2139-registrado.png): dirección 10.21.39.1, Enabled True, después del alta y reinicio de IAS. La entrada del secreto está enmascarada. La captura acredita el registro del cliente, no todavía una autenticación aceptada desde el router.
