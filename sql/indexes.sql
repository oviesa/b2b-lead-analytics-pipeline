CREATE INDEX idx_leads_email       ON leads(email);
CREATE INDEX idx_events_date       ON lead_events(event_date);
CREATE INDEX idx_events_lead_id    ON lead_events(lead_id);
CREATE INDEX idx_events_channel_id ON lead_events(channel_id);
CREATE INDEX idx_status_lead_id    ON lead_status(lead_id);