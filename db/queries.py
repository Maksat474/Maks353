import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()


def create_tables():
    cursor.execute(
        """
        DROP TABLE IF EXISTS category
        """
    )
    cursor.execute(
        """
        DROP TABLE IF EXISTS products
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price DECIMAL,
            image TEXT,
            category_id INTEGER 
        )
        """
    )
    db.commit()


def populate_tables():
    cursor.execute(
        """
        INSERT INTO category (name) VALUES
        ('Книги'), ("Комиксы"), ("Журналы")
        """
    )
    cursor.execute(
        """
        INSERT INTO products (name, price, image, category_id) VALUES 
        ('Подсознание может все ', 560.00, 'images/book1.jpg', 1),
        ('Собор Парижской Богоматери', 210.00, 'images/book2.jpg', 1),
        ('Продавец обуви. История компании NIKE', 990.00, 'images/book3.jpg', 1)
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

def get_products_with_category():
    cursor.execute(
        """
        SELECT p.name, c.name FROM products AS p JOIN category AS c ON p.category_id = c.id
        """
    )
    return cursor.fetchall()

if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    pprint(get_all_products())
    pprint(get_products_with_category())
