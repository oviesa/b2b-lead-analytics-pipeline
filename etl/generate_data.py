from faker import Faker
import pandas as pd
import random

fake = Faker()
CHANNELS = ['LinkedIn', 'Email', 'Organic', 'Referral', 'Paid Ads']
INDUSTRIES = ['SaaS', 'Finance', 'Healthcare', 'Retail', 'Manufacturing']
STATUSES = ['new', 'qualified', 'converted', 'lost']

def generate_leads(n=500):
    return pd.DataFrame([{
        'first_name': fake.first_name(),
        'last_name':  fake.last_name(),
        'email':      fake.unique.email(),
        'phone':      fake.phone_number(),
        'job_title':  fake.job(),
        'company':    fake.company(),
        'industry':   random.choice(INDUSTRIES),
        'size':       random.choice(['1-10', '11-50', '51-200', '500+']),
        'website':    fake.url(),
        'country':    fake.country(),
        'channel':    random.choice(CHANNELS),
        'event_type': random.choice(['click', 'form_submit', 'demo_request']),
        'status':     random.choice(STATUSES),
    } for _ in range(n)])