import mysql.connector

config = {
    "user": "root",
    "password": "KOvi@6112",
    "host": "localhost",
    "database": "ikman_products",
}

db = mysql.connector.connect(**config)
cursor = db.cursor()


def add_product(index, product, availability):
    sql = "INSERT INTO `product_details` VALUES (%s,%s,%s)"
    cursor.execute(sql, (index, product, availability))
    db.commit()
    log_id = cursor.lastrowid
    print(f"Added product {log_id}")
