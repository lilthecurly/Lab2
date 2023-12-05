import requests
import csv
from datetime import datetime, timedelta

start_date = datetime(2015, 1, 1)
end_date = datetime.now()


def get_usd_exchange_rate(date):
    url = f'https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["Valute"]["USD"]["Value"]
    else:
        return None


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)


with open('dataset.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Date', 'USD Exchange Rate'])


    for single_date in date_range(start_date, end_date):
        formatted_date = single_date.strftime('%Y/%m/%d')
        usd_rate = get_usd_exchange_rate(formatted_date)

        if usd_rate is not None:
            csv_writer.writerow([formatted_date, usd_rate])

print("Data saved to dataset.csv")