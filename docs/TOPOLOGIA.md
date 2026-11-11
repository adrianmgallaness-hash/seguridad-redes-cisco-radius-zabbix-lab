# Diseño y direccionamiento

## Parcial: red 10.21.39.0/24

| Elemento | Dato sustentado |
|---|---|
| R-2139 | IOS 12.4; Fa0/0 10.21.39.1/24, up/up |
| Fa0/1 del router | Sin dirección, administrativamente apagada |
| DHCP LAN-2139 | Red /24, gateway .1, DNS .10, dominio lab2139.local |
| Exclusiones DHCP | .1–.99 y .131 |
| Clientes con concesión | .100 y .101 |
| Otros vecinos ARP | .2 y .131; función no confirmada |
| SW-2139 | Gi0/1–Gi0/3 muestran MAC dinámicas seguras en VLAN 10 |

El pool DHCP anuncia DNS .10; no se dispone de una prueba de resolución que confirme ese servicio. La fecha de vencimiento de concesiones mostrada por IOS pertenece a 2002: documenta el reloj del equipo, no la fecha de ejecución del parcial.

## Diferencias frente a antecedentes

La práctica AAA usa 10.21.39.128/29, router .129, switch .130 y DC-2139 .131, dominio infra2139.test. La práctica Zabbix también usa /29, pero .131 corresponde a Ubuntu. Son escenarios distintos: no deben fusionarse ni atribuir los eventos NPS antiguos al router R-2139 actual.

En el router del parcial figura `no aaa new-model`. Por tanto, los archivos disponibles no acreditan autenticación RADIUS en ese equipo.
