import pandas as pd
import requests
import whois
from urllib.parse import urlparse
from datetime import datetime
import openai
import streamlit as st
import os

# --- Load OpenAI Key ---
openai.api_key = st.secrets["OPENAI_API_KEY"]  # Make sure this is set in environment
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Give a 1-line update about OpenAI"}]
)

print(response["choices"][0]["message"]["content"])
# --- Helper Functions ---

def generate_email(company_name, domain):
    clean_domain = domain.replace("www.", "")
    parts = company_name.lower().split()
    if len(parts) >= 2:
        return f"{parts[0]}.{parts[1]}@{clean_domain}"
    return f"{parts[0]}@{clean_domain}"

def is_domain_alive(domain):
    try:
        url = f"http://{domain}"
        response = requests.get(url, timeout=3)
        return response.status_code < 400
    except Exception as e:
        print(f"Domain check failed for {domain}: {e}")
        return False

def get_domain_age(domain):
    try:
        w = whois.whois(domain)
        created = w.creation_date
        if isinstance(created, list):
            created = created[0]
        age_days = (datetime.now() - created).days if created else None
        return age_days
    except Exception as e:
        print(f"WHOIS failed for {domain}: {e}")
        return None

def get_company_news_summary(company):
    try:
        prompt = f"Give a brief 1-line update about recent news or milestones for {company}."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You summarize business updates."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"Error fetching news for {company}: {e}")
        return "No news found"

# --- Main Enhancer ---

def enhance_csv(file_path):
    df = pd.read_csv(file_path)

    df["domain"] = df["Website"].apply(lambda x: urlparse(x).netloc or x)
    df["email_guess"] = df.apply(lambda row: generate_email(row["Company"], row["domain"]), axis=1)
    df["domain_alive"] = df["domain"].apply(is_domain_alive)
    df["domain_age_days"] = df["domain"].apply(get_domain_age)
    df["company_news"] = df["Company"].apply(get_company_news_summary)

    df["score"] = (
        df["domain_alive"].astype(int) * 50 +
        df["Company"].str.len().apply(lambda x: max(0, 40 - x)) +
        df["domain_age_days"].apply(lambda x: min(x or 0, 500) // 10)
    )

    df.to_csv("enhanced_leads.csv", index=False)
    print("✅ Enhanced CSV saved as enhanced_leads.csv")
