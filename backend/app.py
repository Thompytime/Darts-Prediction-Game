from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

DB_CONFIG = {
    "dbname": "your_database",
    "user": "your_username",
    "password": "your_password",
    "host": "your_render_host",
    "port": "your_port",
}

@app.route('/events', methods=['GET'])
def get_events():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("SELECT event_name, event_date, event_time, venue, city, country, description, results FROM darts_events ORDER BY event_date ASC")
    events = cur.fetchall()

    cur.close()
    conn.close()

    events_list = [
        {
            "event_name": row[0],
            "event_date": row[1].strftime('%Y-%m-%d'),
            "event_time": str(row[2]),
            "venue": row[3],
            "city": row[4],
            "country": row[5],
            "description": row[6],
            "results": row[7],
        }
        for row in events
    ]

    return jsonify(events_list)

if __name__ == '__main__':
    app.run(debug=True)
