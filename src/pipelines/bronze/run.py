from .extract import extract_data
from .transform import transform_data
from .load import load_data

def run_bronze():

    try:
        raw_data = extract_data()
        print("Success bronze extract")
    except Exception as e:
        print("Failed bronze extract")
        print(e)


    try:
        transformed_data = transform_data(raw_data)
        print("Success bronze transform")
    except Exception as e:
        print("Failed bronze transform")
        print(e)


    try:
        load_data(transformed_data)
        print("Success bronze load")
    except Exception as e:
        print("Failed bronze load")
        print(e)