import os
import datetime


class Order:
    id: int
    order_number: str
    dollar_price: float
    ruble_price: float
    delivery_date: datetime.date

    def __init__(self,
                 _id: int,
                 order_number: str,
                 dollar_price: float,
                 rate: float,
                 delivery_date: datetime.date):

        self.id = _id
        self.order_number = order_number
        self.dollar_price = dollar_price
        self.ruble_price = round(dollar_price * rate, 2)
        self.delivery_date = delivery_date
