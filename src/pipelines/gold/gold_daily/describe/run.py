from .extract import extract_gold_daily
from .transform import transform_describe


def run_gold_daily_describe():

    try:
        gold_daily_data = extract_gold_daily()
        print("^^^^^^^^^^^^^^^^^\nPhase gold_daily_describe extract")
    except Exception as e:
        print("Failed gold_daily_describe extract")
        print(e)


    try:
        transform_describe(gold_daily_data)
        print("^^^^^^^^^^^^^^^^^\nPhase gold_daily_describe transform")
    except Exception as e:
        print("Failed gold_daily_describe transform")
        print(e)