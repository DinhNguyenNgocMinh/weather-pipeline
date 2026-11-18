import sqlite3
import pandas as pd
from pathlib import Path

import sys
src_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(src_dir))
from config.paths import DB_PATH

def extract_bronze():

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql('SELECT * FROM bronze_weather', conn)

    return df