CREATE TABLE IF NOT EXISTS silver_weather (
    id TEXT PRIMARY KEY,
    temperature FLOAT NOT NULL,
    date DATE NOT NULL,
    time NUMERIC NOT NULL,
    uploaded_at DEFAULT CURRENT_TIMESTAMP
)