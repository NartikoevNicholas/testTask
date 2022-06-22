import settings.config as conf
from models.account import ServiceAccount


def main():
    acc = ServiceAccount(conf.KEY, conf.API).account
    row_data = acc.spreadsheets().values().get(spreadsheetId=conf.SHEETS_ID, range="Лист1").execute()["values"]
    pass


if __name__ == '__main__':
    main()

