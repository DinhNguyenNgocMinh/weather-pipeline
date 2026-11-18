from pathlib import Path

root = Path(__file__).resolve().parents[2]

DB_PATH = rf"{root}\data\weather.db"

BRONZE_PATH = rf"{root}\src\pipelines\bronze"
SILVER_PATH = rf"{root}\src\pipelines\silver"
GOLD_PATH = rf"{root}\src\pipelines\gold"

SETTING_PATH = rf"{root}\src\config\settings.py"
