#!/usr/bin/env python3

import json
import os
import urllib.error
import urllib.parse
import urllib.request

CONFIG_PATH = os.path.expanduser("~/.config/patdesk/weather.conf")
USER_AGENT = "PatDesk/0.6 weather module"
TIMEOUT = 7


def yuck_string(value):
    return json.dumps(str(value), ensure_ascii=False)


def read_config():
    config = {}
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as handle:
            for raw_line in handle:
                line = raw_line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key = key.strip().upper()
                value = value.strip()
                if key in {"CITY", "COUNTRY_CODE"} and value:
                    config[key] = value
    except OSError:
        pass
    return config


def get_json(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        return json.load(response)


def geocode(city, country_code=None):
    params = {"name": city, "count": 5, "language": "fr", "format": "json"}
    data = get_json(
        "https://geocoding-api.open-meteo.com/v1/search?"
        + urllib.parse.urlencode(params)
    )
    results = data.get("results") or []
    if country_code:
        wanted = country_code.upper()
        matching = [
            item
            for item in results
            if str(item.get("country_code", "")).upper() == wanted
        ]
        if matching:
            results = matching
    if not results:
        return None
    item = results[0]
    return {
        "name": item.get("name") or city,
        "latitude": item.get("latitude"),
        "longitude": item.get("longitude"),
    }


def fetch_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,apparent_temperature,weather_code,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
        "timezone": "auto",
        "forecast_days": 1,
    }
    return get_json(
        "https://api.open-meteo.com/v1/forecast?"
        + urllib.parse.urlencode(params)
    )


def condition_from_code(code):
    try:
        code = int(code)
    except (TypeError, ValueError):
        return "·", "Conditions inconnues"

    if code == 0:
        return "☀", "Ciel dégagé"
    if code in {1, 2}:
        return "◐", "Partiellement nuageux"
    if code == 3:
        return "☁", "Couvert"
    if code in {45, 48}:
        return "≋", "Brouillard"
    if code in {51, 53, 55, 56, 57}:
        return "☂", "Bruine"
    if code in {61, 63, 65, 66, 67, 80, 81, 82}:
        return "☂", "Pluie"
    if code in {71, 73, 75, 77, 85, 86}:
        return "❄", "Neige"
    if code in {95, 96, 99}:
        return "⚡", "Orage"
    return "·", "Conditions variables"


def first_number(values):
    if not isinstance(values, list) or not values:
        return None
    return values[0]


def rounded(value):
    try:
        return int(round(float(value)))
    except (TypeError, ValueError):
        return None


def render_unconfigured():
    return (
        '(box :orientation "vertical" :class "patsecure-info patsecure-stale" :space-evenly false '
        '(label :class "patsecure-state" :halign "start" :text "Ville non configurée") '
        '(label :class "patsecure-note" :halign "start" :text "Configuration locale requise"))'
    )


def render_error():
    return (
        '(box :orientation "vertical" :class "patsecure-info patsecure-stale" :space-evenly false '
        '(label :class "patsecure-state" :halign "start" :text "Météo indisponible") '
        '(label :class "patsecure-note" :halign "start" :text "Nouvel essai automatique plus tard"))'
    )


def render(location, data):
    current = data.get("current") or {}
    daily = data.get("daily") or {}

    temp = rounded(current.get("temperature_2m"))
    apparent = rounded(current.get("apparent_temperature"))
    wind = rounded(current.get("wind_speed_10m"))
    tmax = rounded(first_number(daily.get("temperature_2m_max")))
    tmin = rounded(first_number(daily.get("temperature_2m_min")))
    rain = rounded(first_number(daily.get("precipitation_probability_max")))
    icon, condition = condition_from_code(current.get("weather_code"))

    temp_text = f"{temp}°C" if temp is not None else "—"
    apparent_text = f"{apparent}°C" if apparent is not None else "—"
    wind_text = f"{wind} km/h" if wind is not None else "—"
    range_text = f"{tmin}–{tmax}°C" if tmin is not None and tmax is not None else "—"
    rain_text = f"{rain}%" if rain is not None else "—"
    details = f"Ressenti {apparent_text} · vent {wind_text}"
    location_name = location.get("name") or ""
    note = f"Aujourd’hui {range_text} · pluie {rain_text} · {location_name}"

    return (
        '(box :orientation "vertical" :class "patsecure-info patsecure-ok" :space-evenly false '
        '(box :orientation "horizontal" :class "patsecure-status" :space-evenly false '
        f'(label :class "patsecure-dot" :text {yuck_string(icon)}) '
        f'(label :class "patsecure-state" :text {yuck_string(temp_text)}) '
        f'(label :class "patsecure-counts" :halign "start" :hexpand true :text {yuck_string(condition)})) '
        f'(label :class "patsecure-counts" :halign "start" :text {yuck_string(details)}) '
        f'(label :class "patsecure-note" :halign "start" :text {yuck_string(note)}))'
    )


def main():
    config = read_config()
    city = config.get("CITY")
    if not city:
        print(render_unconfigured())
        return

    try:
        location = geocode(city, config.get("COUNTRY_CODE"))
        if not location:
            print(render_error())
            return
        data = fetch_weather(location["latitude"], location["longitude"])
        print(render(location, data))
    except (OSError, ValueError, urllib.error.URLError, TimeoutError):
        print(render_error())


if __name__ == "__main__":
    main()
