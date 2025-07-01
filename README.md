
# 🧠 Lead Insight Enhancer

The **Lead Insight Enhancer** is a Python-based tool that transforms raw lead exports (e.g., from SaaSquatch) into rich, prioritized prospect data. It augments each entry with intelligent signals like website activity, domain age, AI-generated news, and an email guess — helping sales and BD teams focus on the leads that matter most.

---

## 🚀 Why This Project?

Modern sales pipelines are noisy. SaaSquatch and other lead-gen tools provide long lists of potential companies, but lack context:

- Is the company still active?
- How old is its web presence?
- Can we guess a real-looking email?
- Is there any recent traction or news?

This app addresses those blind spots in a minimal, automated way — ideal for internal lead research, early-stage startups, or SDR teams looking to boost productivity.

---

## 🧩 Features

| Feature | Description |
|--------|-------------|
| ✅ **Domain Status Check** | Verifies if the company website is online and reachable |
| 🕰️ **Domain Age (WHOIS)** | Estimates how long the company domain has existed |
| ✉️ **Email Pattern Guess** | Generates likely email based on company name and domain |
| 🧠 **AI News Summary** | Uses GPT-4 to pull a 1-line summary of the company's latest updates |
| 🎯 **Lead Scoring** | Assigns a score based on activity, longevity, and name clarity |
| 📦 **CSV Output** | Saves enriched data as a downloadable CSV |

---

## 📁 Example Input CSV

```csv
Company,Website
OpenAI,https://www.openai.com
Caprae Capital,https://www.capraecapital.com
Notion,https://www.notion.so
Stripe,https://www.stripe.com
Zapier,https://www.zapier.com
```

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

3. **Set your OpenAI API key**

```bash
export OPENAI_API_KEY=your_key_here
```

4. **Run on your input CSV**

```bash
python lead_enhancer.py
```

Output will be saved as `enhanced_leads.csv`.

---

## 🖥️ Optional: Streamlit UI

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

## 🔐 API Key Required

This project uses OpenAI’s GPT-4 API to summarize company updates. You’ll need an API key from [https://platform.openai.com](https://platform.openai.com).

---

## 🤖 Tech Stack

- **Python** (core logic)
- **Pandas** for CSV processing
- **Requests + WHOIS** for web intelligence
- **OpenAI API** for text generation
- **Streamlit** for optional UI

---

## 🧪 Test Data

If you don’t have a SaaSquatch export, just use the included `saasquatch_export.csv` file for a quick demo.

---

## 📦 Packaging Structure

```
lead-insight-enhancer/
├── lead_enhancer.py               # Core logic
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
- Uses **multiple signals**, including GPT-4, to surface value
- Has a **clean UI option** (Streamlit) and CLI for versatility
- Shows **product thinking** and packaging

---

## 🧠 Future Enhancements (Ideas)

- Use LinkedIn + Apollo APIs to pull real email addresses
- Add export to Google Sheets
- Include social signals like Twitter/X activity
- Add filters: score > 80, domain live, etc.

---

## 📬 Questions or Feedback?

Open an issue or ping me at `froughhurmath04@gmail.com`.

---

## 📝 License

MIT — use freely, attribute if you fork or publish.
