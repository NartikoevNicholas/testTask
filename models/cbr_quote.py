import requests
import datetime
from bs4 import BeautifulSoup


DATE = datetime.datetime.now()


class Country:
    _url: str
    _date = datetime.datetime.now()
    rate: float | None

    def __init__(self,
                 unique_code: str,
                 day: int = DATE.strftime("%d"),
                 month: int = DATE.strftime("%m"),
                 year: int = DATE.year):

        self.url = get_url(day, month, year, unique_code)
        self.rate = get_rate(self.url)


def get_rate(url: str):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml").find("value").text.replace(",", ".")
        return float(soup)
    except Exception as ex:
        print(ex)
        return None


def get_url(day: int, month: int, year: int, unique_code: str):
    return f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={day}" \
           f"/{month}/{year}&date_req2={day}/{month}/{year}&VAL_NM_RQ={unique_code}"
