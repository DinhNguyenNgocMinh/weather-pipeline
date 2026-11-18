from src.pipelines.bronze.run import run_bronze
from src.pipelines.silver.run import run_silver
from src.pipelines.gold.gold_daily.run import run_gold_daily
from src.pipelines.gold.gold_daily.describe.run import run_gold_daily_describe

def main():
    run_bronze()
    run_silver()
    run_gold_daily()
    run_gold_daily_describe()

if __name__ == "__main__":
    main()