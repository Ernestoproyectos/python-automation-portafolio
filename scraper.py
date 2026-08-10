"""
Price Scraper - Monitor de precios de productos
--------------------------------------------------
Extrae precios de una lista de productos desde páginas web
y guarda los resultados en un archivo Excel/CSV con historial.

Autor: [Tu nombre]
"""

import csv
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path

# --------------------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------------------
# Lista de productos a monitorear: nombre, URL y los selectores CSS
# donde se encuentra el precio y el título en cada página.
# NOTA: cada sitio tiene una estructura distinta, hay que ajustar
# el selector CSS revisando el HTML de la página (clic derecho > inspeccionar).

PRODUCTS = [
    {
        "name": "Ejemplo Producto 1",
        "url": "https://example.com/producto-1",
        "price_selector": ".price",
        "title_selector": "h1.product-title",
    },
    # Agrega más productos aquí siguiendo el mismo formato
]

OUTPUT_FILE = Path(__file__).parent / "price_history.csv"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def fetch_price(product: dict) -> dict:
    """Obtiene el precio actual de un producto desde su página web."""
    try:
        response = requests.get(product["url"], headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        price_element = soup.select_one(product["price_selector"])
        title_element = soup.select_one(product["title_selector"])

        price_text = price_element.get_text(strip=True) if price_element else "N/A"
        title_text = title_element.get_text(strip=True) if title_element else product["name"]

        return {
            "producto": title_text,
            "precio": price_text,
            "url": product["url"],
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "estado": "ok",
        }

    except requests.exceptions.RequestException as e:
        return {
            "producto": product["name"],
            "precio": "N/A",
            "url": product["url"],
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "estado": f"error: {e}",
        }


def save_results(results: list[dict]):
    """Guarda (o agrega) los resultados a un archivo CSV con historial."""
    file_exists = OUTPUT_FILE.exists()

    with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["producto", "precio", "url", "fecha", "estado"])
        if not file_exists:
            writer.writeheader()
        writer.writerows(results)


def run():
    print(f"Monitoreando {len(PRODUCTS)} producto(s)...\n")
    results = []

    for product in PRODUCTS:
        print(f"  → Consultando: {product['name']}")
        result = fetch_price(product)
        results.append(result)
        print(f"    Precio encontrado: {result['precio']} ({result['estado']})")
        time.sleep(1)  # pausa entre requests para no saturar el servidor

    save_results(results)
    print(f"\nResultados guardados en: {OUTPUT_FILE}")


if __name__ == "__main__":
    run()
