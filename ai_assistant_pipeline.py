import pandas as pd
import uuid, datetime

# Load input
df = pd.read_csv("unique_support_emails.csv")

def assign_priority(text):
    urgent_words = ["cannot", "immediately", "urgent", "critical", "help"]
    return "urgent" if any(w in text.lower() for w in urgent_words) else "not_urgent"

def assign_sentiment(text):
    if any(w in text.lower() for w in ["cannot", "error", "issue"]):
        return "negative"
    elif "thank" in text.lower():
        return "positive"
    else:
        return "neutral"

def generate_response(row):
    if row["priority"] == "urgent":
        return f"Dear {row['sender']}, we understand your concern regarding '{row['subject']}'. Our team is prioritizing this issue and will update you shortly."
    return f"Hello {row['sender']}, thank you for reaching out regarding '{row['subject']}'. We will get back to you soon."

# Process
df["id"] = [str(uuid.uuid4()) for _ in range(len(df))]
df["priority"] = df["subject"].apply(assign_priority)
df["sentiment"] = df["subject"].apply(assign_sentiment)
df["timestamp"] = datetime.datetime.utcnow().isoformat()
df.to_csv("unique_labeled_emails.csv", index=False)

# Responses
responses = pd.DataFrame({
    "id": df["id"],
    "draft_response": df.apply(generate_response, axis=1)
})
responses.to_csv("unique_ai_responses.csv", index=False)

print("Pipeline executed → unique_labeled_emails.csv & unique_ai_responses.csv")
