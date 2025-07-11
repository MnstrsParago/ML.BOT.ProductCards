import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_category_path(category_id):
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    cur = conn.cursor()
    path = []

    while category_id:
        cur.execute("SELECT name, parent_id FROM categories WHERE id = %s", (category_id,))
        row = cur.fetchone()
        if not row:
            break
        name, parent_id = row
        if name:  # если это конечная категория — используем её
            path.insert(0, name)
        category_id = parent_id

    cur.close()
    conn.close()
    return path
