import requests
import pandas as pd
import csv
from datetime import datetime, timedelta

start_date = datetime(2015, 1, 1)
end_date = datetime.now()


def get_usd_exchange_rate(date):
    url = f'https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["Value"]["USD"]["Value"]
    else:
        return None


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)
