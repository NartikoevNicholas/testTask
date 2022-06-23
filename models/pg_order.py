import database
from models.order import Order


class TableOrder:

    """Когда я создаю таблицу в бд я полагаю, что
       столбцы 'id' и 'order_number' уникальны и не повторяются.
       Таблицы состоит из следующих полей:
       'id' - идентификатор;
       'order_number' - номер заказа;
       'dollar_price' - цена в доларах;
       'ruble_price' - цена в рублях;
       'delivery_date' - дата доставки."""

    def __init__(self, order: Order | None, db: database.Database):
        self.order = order
        self._cursor_ = db.connect.cursor()
        self._create_tabel_()

    def _create_tabel_(self):
        self._cursor_.execute(
            "CREATE TABLE if NOT EXISTS orders("
            "id serial PRIMARY KEY,"
            "order_number varchar(50) NOT NULL,"
            "dollar_price real NOT NULL,"
            "ruble_price real NOT NULL,"
            "delivery_date date NOT NULL);")

    def insert_or_update_data(self):

        self._cursor_.execute(
            f"SELECT * FROM orders WHERE "
            f"order_number = '{self.order.order_number}';")

        if t := self._cursor_.fetchone() is not None:

            self._cursor_.execute(
                f"UPDATE orders SET dollar_price = '{self.order.dollar_price}',"
                f"ruble_price = '{self.order.ruble_price}',"
                f"delivery_date = '{self.order.delivery_date}' "
                f"WHERE order_number = '{self.order.order_number}';")

        else:

            self._cursor_.execute(
                f"INSERT INTO orders VALUES("
                f"{self.order.id},"
                f"{self.order.order_number},"
                f"{self.order.dollar_price},"
                f"{self.order.ruble_price},"
                f"'{self.order.delivery_date}');")


def select_all_data(db: database.Database):
    cursor = db.connect.cursor()
    cursor.execute("SELECT id, order_number, dollar_price, delivery_date FROM orders")
    return cursor.fetchall()


def delete_row(db: database.Database, _id: int):
    cursor = db.connect.cursor()
    cursor.execute(f"DELETE FROM orders WHERE id='{_id}'")
