import sqlite3
import pandas as pd
from pathlib import Path

import sys
src_dir = Path(__file__).resolve().parents[4]
sys.path.append(str(src_dir))
from config.paths import DB_PATH

def extract_gold_daily():

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql('SELECT * FROM gold_daily', conn)

    return df