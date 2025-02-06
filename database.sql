CREATE TABLE darts_events (
    id SERIAL PRIMARY KEY,
    event_id VARCHAR(50) UNIQUE,
    event_name VARCHAR(255),
    event_date DATE,
    event_time TIME,
    venue VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100),
    description TEXT,
    results TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
