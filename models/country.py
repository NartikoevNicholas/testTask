import requests
from datetime import datetime
from bs4 import BeautifulSoup


class Country:

    _unique_code_: str

    def __init__(self, unique_code: str):
        self._unique_code_ = unique_code

    def get_currency(self):
        try:
            url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req=" \
                  f"{datetime.now().strftime('%d')}/{datetime.now().strftime('%m')}/{datetime.now().year}"
            response = requests.get(url)
            currency = BeautifulSoup(response.text, "xml").find(ID=self._unique_code_).prettify().split("\n")[14].replace(",", ".")
            return float(currency)
        except Exception as ex:
            print(ex)
            return None
