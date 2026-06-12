import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sqlalchemy import text
from etl.db import get_engine
from etl.generate_data import generate_leads

engine = get_engine()

def run_etl():
    df = generate_leads(500)

    with engine.begin() as conn:
        # Load companies (deduplicated)
        companies = df[['company', 'industry', 'size', 'website', 'country']].drop_duplicates('company').copy()
        companies.columns = ['name', 'industry', 'size', 'website', 'country']
        companies.to_sql('companies', conn, if_exists='append', index=False)

        # Load channels (deduplicated)
        channels = pd.DataFrame({'name': df['channel'].unique()})
        channels.to_sql('channels', conn, if_exists='append', index=False)

        # Fetch back company IDs
        company_ids = pd.read_sql("SELECT company_id, name FROM companies", conn)
        df = df.merge(company_ids, left_on='company', right_on='name', how='left')

        # Load leads
        leads_df = df[['company_id', 'first_name', 'last_name', 'email', 'phone', 'job_title']].copy()
        leads_df.to_sql('leads', conn, if_exists='append', index=False)

        # Fetch back lead IDs and channel IDs
        lead_ids = pd.read_sql("SELECT lead_id, email FROM leads", conn)
        channel_ids = pd.read_sql("SELECT channel_id, name FROM channels", conn)
        df = df.merge(lead_ids, on='email', how='left')
        df = df.merge(channel_ids, left_on='channel', right_on='name', how='left')

        # Load lead events
        events_df = df[['lead_id', 'channel_id', 'event_type']].copy()
        events_df.to_sql('lead_events', conn, if_exists='append', index=False)

        # Load lead statuses
        status_df = df[['lead_id', 'status']].copy()
        status_df.to_sql('lead_status', conn, if_exists='append', index=False)

    print("ETL complete — 500 leads loaded.")

if __name__ == '__main__':
    run_etl()