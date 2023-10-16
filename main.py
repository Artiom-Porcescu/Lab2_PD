import requests
import pandas as pd

def get_usd_exchange_rates(start_date, end_date):
    exchange_rates = []

    base_url = "https://www.cbr-xml-daily.ru/archive/"

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%Y/%m/%d")
        url = f"{base_url}{date_str}/daily_json.js"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            usd_rate = data['Valute']['USD']['Value']
            exchange_rates.append((date_str, usd_rate))

        current_date += pd.Timedelta(days=1)

    return exchange_rates

start_date = pd.to_datetime("2023-09-01")
end_date = pd.to_datetime("2023-09-30")

usd_rates = get_usd_exchange_rates(start_date, end_date)

df = pd.DataFrame(usd_rates, columns=["Date", "USD_Rate"])

df.to_csv("dataset.csv", index=False)

print("Данные сохранены в dataset.csv”)
