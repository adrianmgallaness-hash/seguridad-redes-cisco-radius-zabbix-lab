# Configuraciones públicas

- [R-2139 final](R-2139-running-config.sanitized.cfg): exportación posterior a RADIUS y al guardado [OK] aportada por el autor. AAA habilitado, VTY con LAB_RADIUS/LAB_EXEC, NPS .10, origen .1. Se ocultaron hashes, comunidad SNMP y clave RADIUS tipo 7.
- [SW-2139](SW-2139-running-config.sanitized.cfg): exportación completa, gestión .2/24, VLAN 10, VTY con RADIUS hacia .10; secretos ocultos.
- [Router anterior a RADIUS](historico/R-2139-pre-radius.sanitized.cfg): línea base del informe inicial de auditoría, conservada sin modificar.
- [Antecedentes AAA](../antecedentes/AAA/README.md): configuraciones de la práctica /29 anterior.

La sesión SSH de usuario-n5 en R-2139 y el evento NPS 6272 confirman el nivel 5 y la política LAB2139-Nivel5. SW-2139 todavía necesita su propia sesión y evento actual. HTTP/HTTPS están habilitados en la exportación del switch; el informe de auditoría evalúa únicamente el router.

Los marcadores reemplazan secretos y hashes. Estos archivos son documentación y no deben pegarse directamente en los equipos.
