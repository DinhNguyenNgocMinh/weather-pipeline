CREATE TABLE IF NOT EXISTS bronze_weather (
    id TEXT,
    temperature TEXT,
    date TEXT,
    time TEXT,
    uploaded_at DEFAULT CURRENT_TIMESTAMP
);