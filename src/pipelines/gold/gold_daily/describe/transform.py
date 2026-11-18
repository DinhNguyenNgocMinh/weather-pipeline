import pandas as pd
from matplotlib import pyplot as plt
from datetime import date
import time
today = date.today()
def transform_describe(data):
    df = pd.DataFrame(data)

    # Max temperature
    max_temperature = df['temperature'].max()

    # Min temperature
    min_temperature = df['temperature'].min()


    plt.style.use('bmh')

    fig, (chart, describe) = plt.subplots(1, 2, figsize=(12, 5))

    chart.plot(df['time'], df['temperature'])
    chart.set_title(today)
    chart.set_xlabel("Hour")
    chart.set_ylabel("Temperature")

    describe.axis('off')
    describe.text(
        0.5, 0.5, f"Highest temperature: {max_temperature}\nLowest temperature: {min_temperature}\n",
        transform=describe.transAxes,
        fontsize=14,
        horizontalalignment='center',
        verticalalignment='center'
    )
        
    plt.tight_layout()
    plt.show(block=True)
    