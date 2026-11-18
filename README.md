# Weather Pipeline

Pipeline ETL lấy dữ liệu nhiệt độ theo giờ từ Open-Meteo API, xử lý và lưu theo các tầng Bronze, Silver, Gold trong SQLite.

## Stack

- Python
- Requests
- Pandas
- SQLite
- Matplotlib
- Open-Meteo API

## Data Pipeline

```text
Open-Meteo API
      |
      v
[Bronze]
Extract → Transform → Load
Raw hourly weather data
      |
      v
[Silver]
Extract → Transform → Load
Remove nulls / duplicates
      |
      v
[Gold Daily]
Extract → Transform → Load
Today's hourly temperature
      |
      v
[Describe]
Line chart + Min / Max temperature
```

```text
data/weather.db
├── bronze_weather
├── silver_weather
└── gold_daily
```

## Run Project

```bash
git clone https://github.com/DinhNguyenNgocMinh/weather-pipeline.git
cd weather-pipeline
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install requests pandas matplotlib
python main.py
```

macOS / Linux:

```bash
source .venv/bin/activate
pip install requests pandas matplotlib
python main.py
```
