import requests
from datetime import datetime
from bs4 import BeautifulSoup


class Country:
    _url_: str
    currency: float | None

    def __init__(self, unique_code: str):
        self._date_ = f"{datetime.now().strftime('%d')}/{datetime.now().strftime('%m')}/{datetime.now().year}"
        self._url_ = f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={self._date_}&date_req2={self._date_}" \
                     f"&VAL_NM_RQ={unique_code}"
        self.currency = self._get_currency_()

    def _get_currency_(self):
        try:
            response = requests.get(self._url_)
            soup = BeautifulSoup(response.text, "lxml").find("value").text.replace(",", ".")
            return float(soup)
        except Exception as ex:
            print(ex)
            return None
