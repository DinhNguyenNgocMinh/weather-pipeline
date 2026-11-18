from .extract import extract_silver
from .transform import transform_gold_daily
from .load import load_to_gold_daily

def run_gold_daily():

    try:
        silver_data = extract_silver()
        print("^^^^^^^^^^^^^^^^^\nPhase gold_daily extract")
    except Exception as e:
        print("Failed gold_daily extract")
        print(e)


    try:
        filtered_data = transform_gold_daily(silver_data)
        print("^^^^^^^^^^^^^^^^^\nPhase gold_daily transform")
    except Exception as e:
        print("Failed gold_daily transform")
        print(e)


    try:
        load_to_gold_daily(filtered_data)
        print("^^^^^^^^^^^^^^^^^\nPhase gold_daily load")
    except Exception as e:
        print("Failed gold_daily load")
        print(e)