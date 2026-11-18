def open_mateo():
    return {
        "base_url":r"https://api.open-meteo.com",
        "end_point":r"v1/forecast",

        "default_lat":21.0245,
        "default_lon":105.8412,
        "default_hourly":"temperature_2m",
        "default_timezone":"Asia%2FBangkok",
        "default_pastdays":92,
        "default_forecastdays":16
    }