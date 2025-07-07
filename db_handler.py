import os
from dotenv import load_dotenv
import psycopg2

# Загружаем .env
load_dotenv()

def get_product_data(kaspi_code="AZIMA-Parago-00034"):
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products WHERE kaspi_code = %s", (kaspi_code,))
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row:
        columns = [
            "id", "kaspi_code", "name_cn", "category_1", "category_2", "category_3", "brand",
            "description", "image_paths", "material_pendant", "length_cm", "type",
            "color_metal", "color_insert", "gender", "assay", "material",
            "insert_material", "country", "weight_grams", "vendor_code", "price_yuan"
        ]
        return dict(zip(columns, row))
    return None
