import psycopg2

def get_product_data(kaspi_code="AZIMA-Parago-00034"):
    conn = psycopg2.connect(
        dbname="azima_store",
        user="postgres",
        password="Чуть подождем с этим, а пока просто запушим",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    query = """
    SELECT * FROM products
    WHERE kaspi_code = %s
    """
    cursor.execute(query, (kaspi_code,))
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
    else:
        return None
