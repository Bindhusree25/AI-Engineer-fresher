# Unique AI Support Assistant

This project demonstrates a simple AI-powered communication assistant pipeline.
It loads support emails, categorizes them by **sentiment** and **priority**, and generates **draft responses**.

---

## Files Included

- `baseline_unique.py` → Minimal baseline classifier
- `ai_assistant_pipeline.py` → End-to-end pipeline with labeling and draft response generation
- `unique_support_emails.csv` → Sample dataset of incoming support emails
- `unique_labeled_emails.csv` → Processed & labeled emails
- `unique_ai_responses.csv` → Generated draft responses

---

## How to Run

1. Install dependencies:
   ```bash
   pip install pandas
   ```

2. Run the baseline classifier:
   ```bash
   python baseline_unique.py
   ```

3. Run the full pipeline:
   ```bash
   python ai_assistant_pipeline.py
   ```

This will generate the labeled dataset and AI draft responses in CSV format.

---

## Sample Architecture

```
Emails (CSV) → Baseline (Sentiment & Priority) → Pipeline →
Categorized Emails + Draft Responses → CSV Outputs
```

---

## Example Output

- **unique_labeled_emails.csv**
```
id,sender,subject,priority,sentiment
1,alice@example.com,Help with login,urgent,negative
2,bob@example.com,Query about payment,not_urgent,neutral
```

- **unique_ai_responses.csv**
```
id,draft_response
1,"Dear alice@example.com, we’re sorry for the trouble logging in..."
```

---

## Author
This repository was auto-generated as a **unique demo project** for hackathon-style use cases.
