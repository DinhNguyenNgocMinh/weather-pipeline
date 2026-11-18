from src.pipelines.bronze.run import run_bronze
from src.pipelines.silver.run import run_silver

def main():
    run_bronze()
    run_silver()

if __name__ == "__main__":
    main()