import datetime
import json
from urllib.request import urlopen

from model.exchange_value import get_last_date, insert_exchange_value

API_ACCESS_KEY: str = "947ee49ef275fbc392ea3c4fa01ce515"

# скачивает котировки начиная с последнего дня в таблице до текущей даты
if __name__ == '__main__':
    last_date: datetime.date = datetime.datetime.now().date()
    current_date: datetime.date = get_last_date() + datetime.timedelta(days=1)

    while current_date <= last_date:
        url: str = 'http://data.fixer.io/api/' + current_date.isoformat() + '?access_key=' + API_ACCESS_KEY + '&symbols=USD,GBP,JPY'
        doc = urlopen(url).read()
        r = json.loads(doc.decode('UTF8'))
        eur: float = r['rates']['USD']
        gbp: float = eur / r['rates']['GBP']
        jpy: float = r['rates']['JPY'] / eur

        insert_exchange_value(date_val=current_date, eur=eur, gbp=gbp, jpy=jpy)

        current_date += datetime.timedelta(days=1)
