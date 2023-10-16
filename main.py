import requests
import pandas as pd

start_date = pd.to_datetime("2023-09-01")
end_date = pd.to_datetime("2023-09-30")

exchange_rates = []

base_url = "https://www.cbr-xml-daily.ru/archive/"

while start_date <= end_date:
    date_str = start_date.strftime("%Y/%m/%d")
    url = f"{base_url}{date_str}/daily_json.js"

    response = requests.get(url)
    if requests.get(url).status_code == 200:
        data = requests.get(url).json()
        usd_rate = data['Valute']['USD']['Value']
        exchange_rates.append((date_str, usd_rate))

    start_date += pd.Timedelta(days=1)

df = pd.DataFrame(exchange_rates, columns=["Date", "USD_Rate"])

df.to_csv("dataset.csv", index=False)
