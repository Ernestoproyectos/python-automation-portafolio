# 🔍 Price Scraper — Monitor de Precios

Script en Python que monitorea precios de productos en sitios web y guarda
un historial en CSV, listo para abrir en Excel o Google Sheets.

## 💡 Problema que resuelve

Negocios de e-commerce, dropshipping o cualquier persona que necesite
vigilar precios de la competencia pierde horas revisando páginas
manualmente. Este script automatiza esa revisión y deja un registro
histórico de cómo cambian los precios en el tiempo.

## ⚙️ Cómo funciona

1. Defines una lista de productos con su URL y el selector CSS donde
   está el precio.
2. El script visita cada página, extrae el precio actual y lo guarda
   con fecha y hora en un archivo `price_history.csv`.
3. Cada vez que lo corres, se agrega una nueva fila — así construyes
   un historial de precios a lo largo del tiempo.

## 🚀 Uso

```bash
pip install -r requirements.txt
python scraper.py
```

## 🔧 Personalización

Edita la lista `PRODUCTS` en `scraper.py` con tus productos:

```python
PRODUCTS = [
    {
        "name": "Nombre del producto",
        "url": "https://tienda.com/producto",
        "price_selector": ".price-class",   # inspecciona la página para encontrarlo
        "title_selector": "h1.product-title",
    },
]
```

## 📅 Automatización (opcional)

Este script se puede programar para correr automáticamente cada día
usando un cron job (Linux/Mac) o el Programador de Tareas (Windows),
para tener un monitoreo de precios 100% automático.

## 🛠️ Tecnologías

- Python 3
- `requests` — para hacer las peticiones HTTP
- `BeautifulSoup4` — para extraer datos del HTML

## ⚖️ Nota legal

Antes de scrapear un sitio, revisa sus términos de servicio y el
archivo `robots.txt`. Este proyecto es una demostración técnica;
ajusta su uso según las políticas de cada sitio web.

---

**Servicio disponible:** puedo adaptar este scraper a cualquier sitio
web específico, agregar notificaciones automáticas por correo/Telegram
cuando el precio baje, o exportar directo a Google Sheets.
