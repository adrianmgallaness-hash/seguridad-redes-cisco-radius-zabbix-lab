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
| Cliente para R-2139 .1 | Alta posterior confirmada: R-2139, 10.21.39.1, Enabled True |
| Cuenta del grupo RED-NIVEL-5 | usuario-n5 |

Los clientes .129 y .130 se conservan como registros de la práctica anterior; no representan las direcciones actuales .1 y .2.

## Configuración de red disponible

El [router](../configs/R-2139-running-config.sanitized.cfg) usa 10.21.39.1 y todavía contiene `no aaa new-model`. El [switch](../configs/SW-2139-running-config.sanitized.cfg) usa 10.21.39.2; sus VTY aplican LAB_RADIUS y LAB_EXEC, con NPS-2139 apuntando a .10.

Esto confirma preparación del switch y disponibilidad del servicio NPS. No acredita todavía un acceso aceptado por NPS desde los equipos actuales.

## Políticas y usuario observados

![Políticas LAB2139 de niveles 10 y 5](../imagenes/parcial/NPS-politicas-10-5.png)

![Políticas LAB2139 de niveles 5 y 0; miembro usuario-n5](../imagenes/parcial/NPS-politicas-5-0-usuario-n5.png)

| Política habilitada | Orden visible | Atributo Cisco |
|---|---|---|
| LAB2139-Nivel10 | 4 | shell:priv-lvl=10 |
| LAB2139-Nivel5 | 5 | shell:priv-lvl=5 |
| LAB2139-Nivel0 | 6 | shell:priv-lvl=0 |

Las tres muestran NP-Allow-Dial-in TRUE y Service-Type Login. Las condiciones se representan por SID en la salida. La consulta Get-ADGroupMember muestra a usuario-n5 dentro de RED-NIVEL-5; no acredita todavía un inicio de sesión ni el privilegio realmente asignado.

La [captura de políticas anteriores](../imagenes/parcial/NPS-politicas-AAA-anteriores.png) muestra AAA_Cisco_Nivel10/5/0 antes de las LAB2139, en órdenes 1/2/3. No se deshabilitan ni se cambia su orden basándose solo en estas capturas. El evento NPS del ensayo identificará la política efectivamente utilizada.

El [listado previo](../imagenes/parcial/NPS-clientes-antes-alta-router.png) no contiene .1. La nueva captura posterior confirma su alta:

![R-2139 habilitado en NPS](../imagenes/parcial/NPS-R-2139-registrado.png)

Se ejecutó el alta con Read-Host -AsSecureString y se reinició IAS. El secreto aparece oculto; no se publica su valor.

## Registro del router — completado

En la consola NPS de Windows Server, abrir **Clientes y servidores RADIUS → Clientes RADIUS → Nuevo**. Crear un cliente habilitado con nombre **R-2139**, dirección **10.21.39.1** y fabricante **RADIUS Standard**. Elegir un secreto compartido privado, que deberá coincidir con el configurado después en el router.

No sustituir el secreto existente de SW-2139 ni borrar los clientes anteriores durante esta preparación. La consulta posterior ya fue recibida y confirma R-2139 .1 habilitado.

Después consultar:

```powershell
Get-NpsRadiusClient | Select-Object Name,Address,Enabled
netsh nps show np
Get-ADGroupMember "RED-NIVEL-5" | Select-Object Name,SamAccountName
```

Las políticas y la cuenta de prueba ya aparecen en las capturas; también se confirmó el alta de R-2139 .1.

## Pruebas que faltan

- Alta de R-2139 .1: completada y verificada.
- Comprobar en el ensayo la política efectiva; los atributos configurados ya fueron revisados.
- Configurar AAA/RADIUS en el router conservando acceso local de recuperación.
- Autenticar por SSH en router y switch usando una cuenta AD de prueba.
- Capturar la sesión, el privilegio asignado y el evento NPS 6272 correspondiente a .1/.2.
- Obtener nuevos running-configs sanitizados después de cambios reales y conservar el informe inicial de auditoría.

Los [eventos de la práctica anterior](../antecedentes/AAA/README.md) siguen separados de estas pruebas.

Referencia: [Microsoft: configurar clientes RADIUS en NPS](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-radius-clients-configure).

## Alta por PowerShell — ejecutada y verificada

En Windows Server, PowerShell como administrador:

```powershell
$clavePrivada = Read-Host "Secreto compartido para R-2139" -AsSecureString
New-NpsRadiusClient -Name "R-2139" -Address "10.21.39.1" -SharedSecret ([System.Net.NetworkCredential]::new("", $clavePrivada).Password) -ErrorAction Stop | Out-Null
Remove-Variable clavePrivada
Restart-Service IAS
Get-NpsRadiusClient | Select-Object Name,Address,Enabled
```

Elegir un secreto privado y conservarlo para introducir el mismo en el router. No incluirlo en capturas o archivos públicos. La entrada se oculta y el objeto creado no se imprime. El reinicio de IAS interrumpe brevemente nuevas autenticaciones RADIUS. Si la creación da error, revisar el mensaje antes de continuar; no modificar otro cliente para sustituirlo.

La [documentación de New-NpsRadiusClient](https://learn.microsoft.com/en-us/powershell/module/nps/new-npsradiusclient) indica que el servicio NPS debe reiniciarse después de usar el cmdlet. La captura de la consulta posterior acredita el alta.

## Siguiente fase: configuración del router y prueba SSH

Se preparó el [bloque RADIUS propuesto para IOS 12.4](../scripts/R-2139-radius-propuesto.cli). Todavía no se afirma que esté aplicado. Configura NPS .10, origen .1, listas LAB_RADIUS/LAB_EXEC en las VTY y autenticación local de consola/AUX. El secreto es un marcador y debe sustituirse localmente.

El respaldo local en la lista RADIUS se utiliza cuando el servidor no responde; un rechazo explícito de NPS no activa ese respaldo. Mantener abierta la consola local durante la prueba.

Probar desde Linux `ssh -l usuario-n5 10.21.39.1` y, dentro de esa sesión, `show privilege`. Se espera nivel 5 si se aplica la política correspondiente; el resultado real y el evento 6272 deben recibirse antes de documentar aceptación. La contraseña AD de usuario-n5 es independiente del secreto compartido RADIUS.

Referencia: [Cisco: autenticación en IOS 12.4 y respaldo local](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_aaa/configuration/12-4/sec-usr-aaa-12-4-book/sec-cfg-authentifcn.html).
