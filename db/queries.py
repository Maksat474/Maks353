import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()


def create_tables():
    cursor.execute(
        """
        DROP TABLE IF EXISTS products
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price DECIMAL,
            image TEXT
        )
        """
    )


def populate_tables():
    cursor.execute(
        """
        INSERT INTO products (name, price, image) VALUES 
        ('Подсознание может все ', 560.00, 'images/book1.jpg'),
        ('Собор Парижской Богоматери', 210.00, 'images/book2.jpg'),
        ('Продавец обуви. История компании NIKE', 990.00, 'images/book3.jpg')
        """
    )
    db.commit()


def get_all_products():
    cursor.execute(
        """
        SELECT * FROM products
        """
    )
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    pprint(get_all_products())
