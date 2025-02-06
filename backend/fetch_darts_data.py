import requests
import psycopg2
from datetime import datetime

# API Details
API_KEY = '3'
LEAGUE_ID = '4554'
YEAR = '2025'
BASE_URL = f'https://www.thesportsdb.com/api/v1/json/{API_KEY}'
EVENTS_URL = f"{BASE_URL}/eventsseason.php?id={LEAGUE_ID}&s={YEAR}"

# Database connection
DB_CONFIG = {
    "dbname": "your_database",
    "user": "your_username",
    "password": "your_password",
    "host": "your_render_host",
    "port": "your_port",
}

def fetch_darts_data():
    response = requests.get(EVENTS_URL)
    if response.status_code == 200:
        return response.json().get("events", [])
    return []

def save_to_database(events):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    for event in events:
        event_id = event.get("idEvent")
        event_name = event.get("strEvent")
        event_date = event.get("dateEvent")
        event_time = event.get("strTime")
        venue = event.get("strVenue")
        city = event.get("strCity")
        country = event.get("strCountry")
        description = event.get("strDescriptionEN")
        results = event.get("strResult")  # Store as JSON

        cur.execute("""
            INSERT INTO darts_events (event_id, event_name, event_date, event_time, venue, city, country, description, results)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (event_id) DO UPDATE SET
                event_name = EXCLUDED.event_name,
                event_date = EXCLUDED.event_date,
                event_time = EXCLUDED.event_time,
                venue = EXCLUDED.venue,
                city = EXCLUDED.city,
                country = EXCLUDED.country,
                description = EXCLUDED.description,
                results = EXCLUDED.results;
        """, (event_id, event_name, event_date, event_time, venue, city, country, description, results))

    conn.commit()
    cur.close()
    conn.close()

# Run fetch and save
events = fetch_darts_data()
if events:
    save_to_database(events)
