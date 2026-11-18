import requests
from .settings import open_mateo

s = open_mateo()

def extract_data():

    url = f"{s['base_url']}/{s['end_point']}?latitude={s['default_lat']}&longitude={s['default_lon']}&hourly={s['default_hourly']}&timezone={s['default_timezone']}&past_days={s['default_pastdays']}&forecast_days={s['default_forecastdays']}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f'>>>   Retrieve data from "{url}" successfully')
            return response.json()

        else:
            return response.status_code
    except Exception as e:
        print(e)
        print(f"<<<   Failed to extracting data")