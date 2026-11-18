import pandas as pd

def transform_bronze(data):

    try:
        df = pd.DataFrame(data)

        # Drop Null
        df.dropna(inplace=True)

        # Remove dup
        df.drop_duplicates(inplace=True)

        # Drop no need col
        df.drop(columns='uploaded_at', inplace=True)

        # Reset index
        df.reset_index(inplace=True)

        df.drop(columns='index', inplace=True)


        print(">>>   Transform data successfully")
        return df

    except Exception as e:
        print("<<<   Failed to transforming data")
        print(e)