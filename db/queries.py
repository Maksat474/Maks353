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
        CREATE TABLE IF NOT EXISTS Questionaire(
            name TEXT,
            age INTEGER,
            gender TEXT,
            occupation TEXT,
            education TEXT,
            favorite_genre_of_literature TEXT,
            favorite_autor TEXT,
            favorite_piece TEXT
        )
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
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES category (id)
        )
        """
    )
    db.commit()


def populate_tables():
    cursor.execute(
        """
        INSERT INTO category (name) VALUES
        ("Книги"), ("Комиксы"), ("Сувениры")
        """
    )
    cursor.execute(
        """
        INSERT INTO products (name, price, image, category_id) VALUES 
        ('Подсознание может все ', 560.00, 'images/book1.jpg', 1),
        ('Собор Парижской Богоматери', 210.00, 'images/book2.jpg', 1),
        ('Продавец обуви. История компании NIKE', 990.00, 'images/book3.jpg', 1),
        ('ЭНЦИКЛОПЕДИЯ MARVEL. ХРОНИКИ. ГОД ЗА ГОДОМ', 1990.00, 'images/comics.jpg', 2),
        ('Закладки для книг', 25.00, 'images/souvenirs.jpg', 3)
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


def get_product_by_category_id(category_id: int):
    cursor.execute(
        """
        SELECT * FROM products WHERE category_id = :cat_id
        """, {"cat_id": category_id}
    )
    return cursor.fetchall()


def save_questionaire(data):
    print(data)
    cursor.execute(
        """
        INSERT INTO Questionaire(name, age, gender, occupation, education, 
        favorite_genre_of_literature, favorite_autor, favorite_piece)
        VALUES (:name, :age, :gender, :occupation, :education,
        :favorite_genre_of_literature, :favorite_autor, :favorite_piece)
        """, data
    )
    db.commit()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    # pprint(get_all_products())
    pprint(get_product_by_category_id(1))
