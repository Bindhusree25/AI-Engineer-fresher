import pandas as pd

# Load dataset
df = pd.read_csv("unique_support_emails.csv")

def classify_priority(text):
    urgent_words = ["cannot", "immediately", "urgent", "help"]
    return "urgent" if any(w in text.lower() for w in urgent_words) else "not_urgent"

def classify_sentiment(text):
    if "sorry" in text.lower() or "cannot" in text.lower():
        return "negative"
    elif "thank" in text.lower():
        return "positive"
    else:
        return "neutral"

df["priority"] = df["subject"].apply(classify_priority)
df["sentiment"] = df["subject"].apply(classify_sentiment)

df.to_csv("unique_labeled_emails.csv", index=False)
print("Baseline classification complete → unique_labeled_emails.csv")
