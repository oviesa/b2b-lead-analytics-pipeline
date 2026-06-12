import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from etl.db import get_engine

engine = get_engine()

def leads_by_channel():
    query = """
        SELECT c.name AS channel, COUNT(*) AS leads
        FROM lead_events le
        JOIN channels c ON le.channel_id = c.channel_id
        GROUP BY c.name
        ORDER BY leads DESC
    """
    return pd.read_sql(query, engine)

def top_industries():
    query = """
        SELECT co.industry, COUNT(l.lead_id) AS lead_count
        FROM leads l
        JOIN companies co ON l.company_id = co.company_id
        GROUP BY co.industry
        ORDER BY lead_count DESC
    """
    return pd.read_sql(query, engine)

def monthly_trend():
    query = """
        SELECT DATE_TRUNC('month', created_at) AS month, COUNT(*) AS new_leads
        FROM leads
        GROUP BY month
        ORDER BY month
    """
    return pd.read_sql(query, engine)

if __name__ == '__main__':
    print("=== Leads by Channel ===")
    print(leads_by_channel().to_string(index=False))
    print("\n=== Top Industries ===")
    print(top_industries().to_string(index=False))
    print("\n=== Monthly Trend ===")
    print(monthly_trend().to_string(index=False))