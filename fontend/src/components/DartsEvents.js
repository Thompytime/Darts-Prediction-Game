import React, { useState, useEffect } from "react";

function DartsEvents() {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        fetch("https://your-backend-url/events")
            .then((res) => res.json())
            .then((data) => setEvents(data));
    }, []);

    return (
        <div>
            <h2>BetMGM Premier League Nights</h2>
            <ul>
                {events.map((event, index) => (
                    <li key={index}>
                        <h3>{event.event_name}</h3>
                        <p><strong>Date:</strong> {event.event_date}</p>
                        <p><strong>Time:</strong> {event.event_time}</p>
                        <p><strong>Venue:</strong> {event.venue}, {event.city}, {event.country}</p>
                        <p><strong>Description:</strong> {event.description}</p>
                        <p><strong>Results:</strong> {event.results || "TBD"}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default DartsEvents;
