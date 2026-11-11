# Auditoría de hardening: línea base y revisión posterior

El auditor solo lee configuraciones exportadas y escribe reportes; no se conecta al router ni aplica reglas. Evalúa 16 controles seleccionados relacionados con hardening/CIS, sin certificación ni porcentaje oficial.

| Momento | Entrada | Resultado |
|---|---|---|
| Antes de RADIUS | [Línea base](../configs/historico/R-2139-pre-radius.sanitized.cfg) | [Informe inicial](../reportes/informe-cis-R-2139.md): 7 conformes, 9 hallazgos |
| Después de RADIUS | [Exportación final](../configs/R-2139-running-config.sanitized.cfg) | [Informe posterior](../reportes/informe-cis-R-2139-post-radius.md): 8 conformes, 8 hallazgos |

Se conservó intacto el reporte inicial y se verificó que es reproducible con su entrada histórica. La mejora del control AAA corresponde a la configuración RADIUS realmente aplicada y al nuevo running-config aportado; no se modificaron resultados para aparentar cumplimiento.

## Reproducción

Desde la raíz del repositorio:

```bash
python scripts/audit_cis.py configs/historico/R-2139-pre-radius.sanitized.cfg --output reportes/informe-cis-R-2139.md
python scripts/audit_cis.py configs/R-2139-running-config.sanitized.cfg --output reportes/informe-cis-R-2139-post-radius.md
python -m unittest discover -s scripts -p "test_*.py"
```

## Límites y hallazgos conservados

Consola/AUX siguen sin expiración y con privilegio 15 explícito, existen hashes tipo 5 (valores ocultos), VTY carece de ACL de origen, SNMP permite toda la LAN y no se identifica un destino syslog remoto. No se aplicaron reglas adicionales para eliminar esos hallazgos.

El control AAA del auditor detecta la directiva global. La prueba funcional separada es la [sesión SSH de nivel 5](../imagenes/parcial/SSH-R-2139-usuario-n5-nivel5.png) y el [evento NPS 6272](../evidencias/parcial/NPS-6272-R-2139-usuario-n5.txt). No se presenta una comprobación estática como sustituto del ensayo de autenticación.

El informe evalúa el router, no el switch. No comprueba la fortaleza real de contraseñas ni certifica el conjunto de recomendaciones CIS.
