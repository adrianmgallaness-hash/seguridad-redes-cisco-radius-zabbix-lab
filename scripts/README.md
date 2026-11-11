# Herramientas de consulta y revisión

Requiere Python 3.10 o posterior, sin paquetes externos.

Desde la raíz del repositorio:

```bash
python scripts/audit_cis.py configs/R-2139-running-config.sanitized.cfg --output reportes/informe-cis-R-2139.md
python -m unittest discover -s scripts -p "test_*.py"
```

El auditor lee un archivo local y escribe únicamente el reporte solicitado; rechaza usar la ruta de entrada como salida. No utiliza conexiones de red, credenciales ni comandos de configuración. No imprime valores de secretos.

Los resultados «CUMPLE» se refieren a los controles locales seleccionados y a la copia analizada. «NO EVALUABLE» evita considerar correctos bloques ausentes. No analiza todos los comandos de IOS, valores implícitos, la fortaleza de contraseñas ni el funcionamiento real de servicios.

[Consultas IOS](verificacion-ios.cli): ejecutar las aplicables en el dispositivo correspondiente. Las consultas PowerShell del [antecedente AAA](../antecedentes/AAA/verificacion.ps1) se ejecutan en Windows Server, nunca en IOS.

La herramienta adapta controles de gestión, sesiones, servicios y registros descritos por [CIS para Cisco](https://www.cisecurity.org/benchmark/cisco). No implementa íntegramente un benchmark/versionado ni asigna una puntuación CIS oficial.
