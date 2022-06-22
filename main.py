import settings.config as conf
import datetime

from models.order import Order
from models.cbr_quote import Country
from models.account import ServiceAccount
from models.pg_order import TabelOrder
from database import Database


def main():
    # connect google acc
    acc = ServiceAccount(conf.KEY, conf.API)

    # get data from table
    list_data = acc.account.spreadsheets().values().get(
        spreadsheetId=conf.SHEETS_ID,
        range="Лист1").execute()["values"][1:]

    # get rate
    country_rate = Country(conf.USA_UNIQUE_CODE).rate

    # connect db
    db = Database(conf.db_name, conf.user, conf.password, conf.localhost)
    pass
    for el in list_data:
        d_m_y = el[3].split(".")
        date = datetime.date(int(d_m_y[2]), int(d_m_y[1]), int(d_m_y[0]))
        order = Order(int(el[0]), el[1], float(el[2]), country_rate, date)
        TabelOrder(order, db).insert()
        pass


if __name__ == '__main__':
    main()
