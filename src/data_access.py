from db_connection import get_connection

def get_products_from_db(obek_label, limit=15):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT name, image_url, description
    FROM products
    WHERE cluster_label = ?
    LIMIT ?
    """
    cursor.execute(query, (obek_label, limit))
    results = cursor.fetchall()
    conn.close()

    products = []
    for r in results:
        product = {
            "name": r[0],
            "image_url": r[1],
            "description": r[2]
        }
        products.append(product)

    return products
