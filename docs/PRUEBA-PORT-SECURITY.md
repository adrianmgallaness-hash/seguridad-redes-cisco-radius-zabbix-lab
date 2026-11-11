# Prueba controlada de violación de port-security

**Estado:** procedimiento preparado; la ejecución todavía no está acreditada. La última salida de Gi0/1 conserva contador 0 y Secure-up.

## Preparación

Usar Gi0/2, puerto PC-USUARIOS, manteniendo abiertas las consolas GNS3. Gi0/1 (Windows AD/NPS), Gi0/3 (Zabbix) y Gi0/0 (router) permanecen conectados.

Guardar primero estas consultas:

```text
show port-security interface GigabitEthernet0/2
show port-security address
show interfaces GigabitEthernet0/2 status
```

## Ensayo manteniendo máximo 2 MAC

Intercalar temporalmente un switch Ethernet sencillo de GNS3 entre Gi0/2 y el PC de usuarios. Conectar también dos VPCS nuevos a ese switch de prueba. No crear otro enlace de ese switch a la LAN.

Así llegan tres MAC distintas al mismo puerto protegido. Generar tráfico desde el PC original con `ping 10.21.39.1`. En cada VPCS ejecutar `ip dhcp` para que emita tráfico con su propia MAC; si recibe dirección, ejecutar también `ping 10.21.39.1`. Al llegar tráfico desde la tercera MAC, el modo shutdown debe bloquear Gi0/2. La obtención DHCP del último VPCS puede fallar como consecuencia del bloqueo; no se interpreta como prueba de DHCP defectuoso.

No se cambia el máximo permitido de 2 ni se conectan los VPCS a otros puertos protegidos.

## Captura posterior, antes de recuperar

```text
show port-security
show port-security interface GigabitEthernet0/2
show interfaces GigabitEthernet0/2 status
show logging | include PSECURE|ERR_DISABLE
```

Documentar el contador real, estado Secure-shutdown/err-disabled según la salida y los mensajes disponibles. No inventar el contador ni publicar este procedimiento como resultado ejecutado.

## Recuperación

Después de guardar la evidencia, retirar el switch temporal y los dos VPCS; restaurar la conexión directa del PC a Gi0/2. Desde la consola de SW-2139:

```text
configure terminal
interface GigabitEthernet0/2
shutdown
no shutdown
end
show port-security interface GigabitEthernet0/2
show interfaces GigabitEthernet0/2 status
```

Comprobar el ping desde el PC. Conservar capturas de antes, bloqueo y recuperación.

Referencia: [Cisco: port-security y recuperación manual](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-3750-series-switches/72846-layer2-secftrs-catl3fixed.html).
