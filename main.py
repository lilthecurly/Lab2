import requests
import pandas as pd
import csv
from datetime import datetime, timedelta


def get_usd_exchange_rate(date):
    url = f'https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["Value"]["USD"]["Value"]
    else:
        return None
