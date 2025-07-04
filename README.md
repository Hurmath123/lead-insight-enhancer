
# 🧠 Lead Insight Enhancer

The **Lead Insight Enhancer** is a Python-based tool that enriches raw lead exports (like those from SaaSquatch) into smart, scored prospects using domain intelligence, AI-powered summaries, and email generation. This version runs entirely offline using the open-source **llama3 model with Ollama** — perfect for privacy, cost efficiency, and control.

---

## 🚀 Why This Project?

Sales and BD teams often get raw CSVs of company names — but no real signal. This tool fills in that context:

- Is the company still active?
- How old is its web presence?
- Can we guess a real-looking email?
- Is there any recent traction or news?

With no external API calls, it gives quick insights right from your machine — helpful for prospecting, validation, or internal dashboards.

---

## 🧩 Features

| Feature | Description |
|--------|-------------|
| ✅ **Domain Status Check** | Verifies if the company website is online and reachable |
| 🕰️ **Domain Age (WHOIS)** | Estimates how long the company domain has existed |
| ✉️ **Email Pattern Guess** | Generates likely email based on company name and domain |
| 🧠 **AI News Summary** | Uses llama-3 to pull a 1-line summary of the company's latest updates |
| 🎯 **Lead Scoring** | Assigns a score based on activity, longevity, and name clarity |
| 📦 **CSV Output** | Saves enriched data as a downloadable CSV |

---

## ✨ Output Example

| Company | Website | Domain | Email Guess | Domain Live | Age (Days) | Company News | Score |
|---------|---------|--------|-------------|--------------|--------------|---------------|-------|
| OpenAI | openai.com | ... | contact@openai.com | ✅ | 2900 | "Launched GPT-4 Turbo." | 91 |

---

## 🛠️ Installation & Setup

1. **Clone the repo**

```bash
git clone https://github.com/Hurmath123/lead-insight-enhancer.git
cd lead-insight-enhancer
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Install Ollama and model**
Install Ollama and pull the llama3 model:

```bash
ollama pull llama3
```

Ensure Ollama is running:

```bash
ollama serve
```

---

## 🖥️ Streamlit UI

To use the tool with a simple web interface:

```bash
streamlit run app.py
```

Upload a CSV file and download the enhanced version directly.

---

## 📊 How the Scoring Works

Each lead is assigned a numeric score based on:

- ✅ **Domain is active** → +50
- 🧠 **Shorter company name** → up to +40
- 📅 **Domain age (up to 500 days)** → up to +50

**Total Score = Live (50) + Name Clarity (40) + Domain Age Bucket (0–50)**

---

## 🤖 Tech Stack

- **Python** (core logic)
- **Pandas** for CSV processing
- **Requests + WHOIS** for web intelligence
- **Streamlit** for UI

---

## 🧪 Test Data

If you don’t have a SaaSquatch export, just use the included `saasquatch_export.csv` file for a quick demo.

---

## 📦 Packaging Structure

```
lead-insight-enhancer/
├── enhancer.py               # Core logic
├── app.py                    # Streamlit UI
├── saasquatch_export.csv     # Example input
├── enhanced_leads.csv        # Output (created at runtime)
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📣 Why This Might Impress Caprae

This project:
- Targets a **clear pain point** in lead prioritization
- Shows **real-world judgment** (email patterns, domain scoring)
- Uses **multiple signals**, including llama-3, to surface value
- Has a **clean UI option** (Streamlit) and CLI for versatility
- Shows **product thinking** and packaging

---

## 🧠 Future Enhancements (Ideas)

- LinkedIn data enrichment
- Social media activity scraping
- Built-in filters (score > 100, news present, etc.)
- Export to Google Sheets or Notion

---

## 📬 Questions or Feedback?

Open an issue or ping me at `froughhurmath04@gmail.com`.

---

## 📝 License

MIT — use freely, attribute if you fork or publish.
