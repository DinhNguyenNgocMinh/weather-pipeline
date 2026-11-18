import sqlite3
from pathlib import Path

import sys
src_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(src_dir))
from config.paths import DB_PATH



def load_to_bronze(data):

    sql_create = rf"{src_dir}\pipelines\bronze\sql\init.sql"
    sql_insert = rf"{src_dir}\pipelines\bronze\sql\insert.sql"
    sql_truncate = rf"{src_dir}\pipelines\bronze\sql\truncate.sql"


    df = data

    df = list(df.itertuples(index=False, name=None))

    with open(sql_create, 'r') as c:
        sql_create = c.read()

    with open(sql_insert, 'r') as i:
        sql_insert = i.read()

    with open(sql_truncate, 'r') as t:
        sql_truncate = t.read()

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_create)
        cursor.execute(sql_truncate)
        cursor.executemany(sql_insert, df)

    print(f'>>>   Write {len(df)} lines successfully into "{DB_PATH}"')
    conn.commit()
    conn.close()

    # try:
    #     df = data

    #     df = list(df.itertuples(index=False, name=None))

    #     with open(sql_create, 'r') as c:
    #         sql_create = c.read()

    #     with open(sql_insert, 'r') as i:
    #         sql_insert = i.read()

    #     with open(sql_truncate, 'r') as t:
    #         sql_truncate = t.read()

    #     with sqlite3.connect(DB_PATH) as conn:
    #         cursor = conn.cursor()
    #         cursor.execute(sql_create)
    #         cursor.execute(sql_truncate)
    #         cursor.executemany(sql_insert, df)

    #     print(f'>>>   Write {len(df)} lines successfully into "{DB_PATH}"')
    #     conn.commit()
    #     conn.close()

    # except Exception as e:
    #     print("<<<   Failed to loading data")
    #     print(e)
