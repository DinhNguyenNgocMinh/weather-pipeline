import sqlite3
import pandas as pd
from pathlib import Path

import sys
src_dir = Path(__file__).resolve().parents[3]
sys.path.append(str(src_dir))
from config.paths import DB_PATH

def extract_silver():

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql('SELECT * FROM silver_weather', conn)

    return df