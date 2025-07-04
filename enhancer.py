import pandas as pd
import requests
import whois
from urllib.parse import urlparse
from datetime import datetime

# Ollama config (local LLM)
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"

def get_ollama_response(prompt):
    """Query Ollama's local LLM for a response."""
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception:
        return "No news found"

def generate_email(company_name, domain):
    """Generate a likely email format."""
    parts = company_name.lower().split()
    if len(parts) >= 2:
        return f"{parts[0]}.{parts[1]}@{domain}"
    return f"{parts[0]}@{domain}"

def is_domain_alive(domain):
    """Check if domain is accessible."""
    try:
        response = requests.get(f"http://{domain}", timeout=3)
        return response.status_code < 400
    except Exception:
        return False

def get_domain_age(domain):
    """Calculate domain age in days from WHOIS data."""
    try:
        w = whois.whois(domain)
        created = w.creation_date
        if isinstance(created, list):
            created = created[0]
        return (datetime.now() - created).days if created else None
    except Exception:
        return None

def get_company_news_summary(company):
    """Generate one-line recent update using Ollama."""
    prompt = f"Give a one-line recent update or news about {company}. If nothing recent, say 'No news found'."
    return get_ollama_response(prompt)

def enhance_csv(file_path):
    """Process CSV and return enhanced DataFrame."""
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
    return df
