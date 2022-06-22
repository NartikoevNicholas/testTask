import database
from models.order import Order


class TabelOrder:

    def __init__(self, order: Order, db: database.Database):
        self.order = order
        self._cursor = db.connect.cursor()
        self._create_tabel()

    def _create_tabel(self):
        self._cursor.execute(
            """CREATE TABLE if NOT EXISTS orders(
                id serial PRIMARY KEY,
                order_number varchar(50) NOT NULL,
                dollar_price real NOT NULL,
                ruble_price real NOT NULL,
                delivery_date date NOT NULL);"""
        )

    def insert(self):
        self._cursor.execute(
            f"INSERT INTO orders VALUES("
            f"{self.order.id},"
            f"{self.order.order_number},"
            f"{self.order.dollar_price},"
            f"{self.order.ruble_price},"
            f"'{self.order.delivery_date}');"
        )
