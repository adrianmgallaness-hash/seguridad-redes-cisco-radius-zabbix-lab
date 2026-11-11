# Active Directory, NPS y RADIUS del parcial

## Evidencia recibida

![Servicio NPS, IP, clientes y grupos actuales](../imagenes/parcial/NPS-servicio-IP-clientes-grupos.png)

| Dato | Resultado observado |
|---|---|
| Servicio IAS | Running |
| IPv4 del servidor | 10.21.39.10/24, Ethernet0 2 |
| Grupos existentes | RED-NIVEL-0, RED-NIVEL-5 y RED-NIVEL-10 |
| Cliente R1 | 10.21.39.129, habilitado |
| Cliente SW1 | 10.21.39.130, habilitado |
| Cliente SW-2139 | 10.21.39.2, habilitado |
| Cliente para R-2139 .1 | No aparece en el listado aportado |

Los clientes .129 y .130 se conservan como registros de la práctica anterior; no representan las direcciones actuales .1 y .2.

## Configuración de red disponible

El [router](../configs/R-2139-running-config.sanitized.cfg) usa 10.21.39.1 y todavía contiene `no aaa new-model`. El [switch](../configs/SW-2139-running-config.sanitized.cfg) usa 10.21.39.2; sus VTY aplican LAB_RADIUS y LAB_EXEC, con NPS-2139 apuntando a .10.

Esto confirma preparación del switch y disponibilidad del servicio NPS. No acredita todavía un acceso aceptado por NPS desde los equipos actuales.

## Próximo paso: registrar el router actual

En la consola NPS de Windows Server, abrir **Clientes y servidores RADIUS → Clientes RADIUS → Nuevo**. Crear un cliente habilitado con nombre **R-2139**, dirección **10.21.39.1** y fabricante **RADIUS Standard**. Elegir un secreto compartido privado, que deberá coincidir con el configurado después en el router.

No sustituir el secreto existente de SW-2139 ni borrar los clientes anteriores durante esta preparación. La creación del nuevo cliente se marcará como realizada únicamente cuando se reciba la consulta posterior.

Después consultar:

```powershell
Get-NpsRadiusClient | Select-Object Name,Address,Enabled
netsh nps show np
Get-ADGroupMember "RED-NIVEL-5" | Select-Object Name,SamAccountName
```

Esas salidas permitirán comprobar el nuevo cliente, condiciones/atributos de las políticas y una cuenta del grupo de prueba antes de activar AAA en el router.

## Pruebas que faltan

- Registrar R-2139 .1 y verificar su presencia.
- Revisar las políticas actuales y sus atributos de privilegio.
- Configurar AAA/RADIUS en el router conservando acceso local de recuperación.
- Autenticar por SSH en router y switch usando una cuenta AD de prueba.
- Capturar la sesión, el privilegio asignado y el evento NPS 6272 correspondiente a .1/.2.
- Obtener nuevos running-configs sanitizados después de cambios reales y conservar el informe inicial de auditoría.

Los [eventos de la práctica anterior](../antecedentes/AAA/README.md) siguen separados de estas pruebas.

Referencia: [Microsoft: configurar clientes RADIUS en NPS](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-radius-clients-configure).
