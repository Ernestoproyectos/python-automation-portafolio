# 📊 Excel Report Automation

Script en Python que convierte datos crudos (CSV) en un reporte de Excel
profesional automáticamente: resumen, totales y gráfica incluidos.

## 💡 Problema que resuelve

Muchos negocios reciben datos crudos (ventas, inventario, asistencia,
lo que sea) y alguien tiene que armar el reporte "bonito" a mano cada
semana o cada mes: sumar, dar formato, hacer la gráfica. Este script
lo hace en segundos, siempre con el mismo formato profesional.

## ⚙️ Cómo funciona

1. Lee un archivo CSV con datos crudos.
2. Agrupa y suma automáticamente según la columna que definas.
3. Genera un archivo Excel con:
   - Hoja de datos originales, con formato
   - Hoja de resumen con totales
   - Gráfica de barras generada automáticamente

## 🚀 Uso

```bash
pip install -r requirements.txt
python report_generator.py
```

## 🔧 Personalización

Cambia estas líneas en `report_generator.py` según tus datos:

```python
GROUP_BY_COLUMN = "producto"
VALUE_COLUMN = "ventas"
```

## 🛠️ Tecnologías

- Python 3
- `pandas` — para procesar y agrupar los datos
- `openpyxl` — para generar el Excel con formato y gráficas

---

**Servicio disponible:** puedo adaptar este generador a cualquier
formato de datos, agregar múltiples hojas de resumen, tablas dinámicas,
o conectarlo directamente a una base de datos o Google Sheets.
