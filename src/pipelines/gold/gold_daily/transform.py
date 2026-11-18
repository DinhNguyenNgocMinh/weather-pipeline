import pandas as pd
from datetime import date

today = date.today()
def transform_gold_daily(data):

    df = pd.DataFrame(data)

    # Take today
    df = df[df['date'] == str(today)]

    # Drop no need col
    df.drop(columns='date', inplace=True)
    df.drop(columns='uploaded_at', inplace=True)

    return df