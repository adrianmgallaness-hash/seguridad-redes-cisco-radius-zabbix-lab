# Configuraciones públicas

- [R-2139](R-2139-running-config.sanitized.cfg): running-config aportado por el autor. Se ocultaron hashes y comunidad SNMP, conservando el tipo de hash.
- [SW-2139](SW-2139-running-config.sanitized.cfg): running-config completo recibido del switch, con secretos y comunidad SNMP ocultos. Sustituye el fragmento documental anterior.
- [R1 y SW1 de AAA](../antecedentes/AAA/README.md): equipos de otra práctica, conservados como antecedentes.

El switch usa VLAN 10, gestión 10.21.39.2/24 y gateway 10.21.39.1. Las VTY usan LAB_RADIUS y LAB_EXEC con destino NPS 10.21.39.10 y respaldo local si el servidor no responde. La configuración prueba su presencia; falta una sesión autenticada y un evento NPS para verificar el funcionamiento actual.

El router aún contiene `no aaa new-model`; no se modificó su exportación para aparentar RADIUS habilitado. El informe de auditoría se limita al router, no al switch. En el switch están habilitados HTTP/HTTPS según la exportación recibida.

Estos archivos contienen marcadores y no deben pegarse directamente en los dispositivos.
