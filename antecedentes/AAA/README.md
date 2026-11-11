# Antecedente: Active Directory, NPS y RADIUS

Material de la práctica AAA con R1 .129, SW1 .130 y DC-2139 .131 en /29; dominio infra2139.test. **No acredita el estado del parcial /24.**

| Evidencia | Observación |
|---|---|
| [Grupos AD](../../imagenes/aaa/05-Grupos-AD.png) | radius0, radius5 y radius10 en grupos de privilegios |
| [Políticas](../../imagenes/aaa/07-NPS-Niveles10-5-completas.jpg) | shell:priv-lvl=10 y 5; política nivel 0 habilitada, con atributos fuera del borde inferior |
| [Aceptación](../../imagenes/aaa/26a-NPS-Aceptado-SW1.png) | Evento 6272, SW1 .130, radius5 |
| [Rechazo](../../imagenes/aaa/27-NPS-Rechazado-usuario-inexistente.png) | Evento 6273, R1 .129, usuario inexistente «show privilege»; no es una prueba de contraseña incorrecta para radius5 |
| [SSH](../../imagenes/aaa/18-R1-SSH.jpg) | SW1 a R1, usuario local de recuperación con nivel 15 |

Configuraciones sanitizadas: [R1](configs/R1.cfg), [SW1](configs/SW1.cfg), [NPS](configs/NPS-sanitized.xml). El XML no es un respaldo restaurable con secretos. El [script de consultas](verificacion.ps1) corresponde al dominio histórico; no se ejecutó contra el entorno actual.

Consola/AUX usaban RADIUS y respaldo local ante falta de respuesta; SSH usaba una lista local independiente. No se afirma autorización NPS por cada comando.
