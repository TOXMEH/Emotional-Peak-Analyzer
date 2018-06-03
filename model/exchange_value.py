import datetime
from typing import List

from pony.orm import *

db = Database()
db.bind(provider='mysql', host='localhost', user='root', passwd='password', db='local')


class ExchangeValue(db.Entity):
    _table_ = "exchange_values"
    date_val = PrimaryKey(datetime.date, column="date")
    eur = Optional(float, column="EUR")
    jpy = Optional(float, column="JPY")
    gbp = Optional(float, column="GBP")


db.generate_mapping(create_tables=False)


@db_session
def insert_exchange_value(date_val: datetime.date, eur: float = None, jpy: float = None, gbp: float = None):
    ExchangeValue(date_val=date_val, eur=eur, jpy=jpy, gbp=gbp)


@db_session
def get_last_date() -> datetime.date:
    return max(p.date_val for p in ExchangeValue)


@db_session
def get_exchange_values_between(start_date: datetime.date, finish_date: datetime.date) -> List[float]:
    return select(p for p in ExchangeValue if between(p.date_val, start_date, finish_date))[:]
    # if exchange_value_name is ExchangeValueName.EUR:
    #     return select(p.eur for p in ExchangeValue if between(p.date_val, start_date, finish_date))[:]
    # elif exchange_value_name is ExchangeValueName.GBP:
    #     return select(p.gbp for p in ExchangeValue if between(p.date_val, start_date, finish_date))
    # elif exchange_value_name is ExchangeValueName.JPY:
    #     return select(p.jpy for p in ExchangeValue if between(p.date_val, start_date, finish_date))
