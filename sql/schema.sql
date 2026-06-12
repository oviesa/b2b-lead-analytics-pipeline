CREATE TABLE companies (
    company_id   SERIAL PRIMARY KEY,
    name         VARCHAR(255) NOT NULL,
    industry     VARCHAR(100),
    size         VARCHAR(50),
    website      VARCHAR(255),
    country      VARCHAR(100),
    created_at   TIMESTAMP DEFAULT NOW()
);

CREATE TABLE leads (
    lead_id      SERIAL PRIMARY KEY,
    company_id   INT REFERENCES companies(company_id),
    first_name   VARCHAR(100),
    last_name    VARCHAR(100),
    email        VARCHAR(255) UNIQUE NOT NULL,
    phone        VARCHAR(50),
    job_title    VARCHAR(150),
    created_at   TIMESTAMP DEFAULT NOW()
);

CREATE TABLE channels (
    channel_id   SERIAL PRIMARY KEY,
    name         VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE lead_events (
    event_id     SERIAL PRIMARY KEY,
    lead_id      INT REFERENCES leads(lead_id),
    channel_id   INT REFERENCES channels(channel_id),
    event_type   VARCHAR(100),
    event_date   TIMESTAMP DEFAULT NOW(),
    metadata     JSONB
);

CREATE TABLE lead_status (
    status_id    SERIAL PRIMARY KEY,
    lead_id      INT REFERENCES leads(lead_id),
    status       VARCHAR(100),
    changed_at   TIMESTAMP DEFAULT NOW(),
    notes        TEXT
);