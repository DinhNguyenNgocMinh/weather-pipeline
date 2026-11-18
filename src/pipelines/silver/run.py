from .extract import extract_bronze
from .transform import transform_bronze
from .load import load_to_silver

def run_silver():

    try:
        bronze_data = extract_bronze()
        print("^^^^^^^^^^^^^^^^^\nPhase silver extract")
    except Exception as e:
        print("Failed silver extract")
        print(e)


    try:
        cleaned_data = transform_bronze(bronze_data)
        print("^^^^^^^^^^^^^^^^^\nPhase silver transform")
    except Exception as e:
        print("Failed silver transform")
        print(e)


    try:
        load_to_silver(cleaned_data)
        print("^^^^^^^^^^^^^^^^^\nPhase silver load")
    except Exception as e:
        print("Failed silver load")
        print(e)