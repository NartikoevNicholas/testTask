import datetime
import time
import settings.config as conf

from database import Database
from models.telegram_bot import Bot
from models.google_api import Sheet
from models.cbr_quote import Country
from models.order import Order
from models.pg_order import TableOrder, select_all_data, delete_row


def data_processing(data: list):
    result = []
    for el in data:
        # условие на случай, если вдруг строка в таблице будет не полностью заполнена
        if len(el) != 4:
            continue

        # date
        d_m_y = el[3].split(".")
        date = datetime.date(int(d_m_y[2]), int(d_m_y[1]), int(d_m_y[0]))

        result.append((int(el[0]), el[1], float(el[2]), date))
    return result


def main():
    # google sheet tabel
    sheet_tabel = Sheet(conf.KEY, conf.API)

    # get data from table google sheets
    data: list = sheet_tabel.sheet.spreadsheets().values().get(
        spreadsheetId=conf.SHEETS_ID,
        range="'Лист1'!A2:D").execute()["values"]

    # data analysis and processing
    data: list = data_processing(data)

    # country currency
    country_currency: float | None = Country(conf.USA_UNIQUE_CODE).currency

    # connect db
    db = Database(conf.db_name, conf.user, conf.password, conf.localhost)

    # insert or update element "data" in databases
    for el in data:
        # class instance "Order"
        order = Order(el[0], el[1], el[2], country_currency, el[3])
        TableOrder(order, db).insert_or_update_data()

    # delete row data
    data_db: list = select_all_data(db)
    for el in data_db:
        if data.__contains__(el):
            if datetime.datetime.now().date() > el[3]:
                Bot.message_send(f"Заказ просрочен! Номер заказа {el[1]}.")
        else:
            delete_row(db, el[0])


if __name__ == '__main__':
    while True:
        main()
        time.sleep(5)
        print("success")
