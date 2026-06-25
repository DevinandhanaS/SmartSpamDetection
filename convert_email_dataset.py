import pandas as pd
import numpy as np

# Convert email spam dataset to CSV format
# Assumes you have downloaded the SpamBase dataset from UCI ML Repository

data = pd.read_csv(
    "spambase.data",
    header=None
)

# The last column is the label (0=ham, 1=spam)
# Create column names for features
feature_names = [f"feature_{i}" for i in range(len(data.columns) - 1)]
feature_names.append("label")
data.columns = feature_names

# Convert numeric labels to categorical
data['label'] = data['label'].map({0: 'ham', 1: 'spam'})

# Since spambase doesn't have text, we'll create a text representation
# from the features for demonstration
def create_text_representation(row):
    # Create a simple text representation from numeric features
    words = []
    for col in feature_names[:-1]:
        if row[col] > 0.5:
            words.append(col.replace('_', ' '))
    return ' '.join(words) if words else 'content'

data['text'] = data.apply(create_text_representation, axis=1)

# Save to CSV with relevant columns
email_data = data[['text', 'label']].copy()
email_data.to_csv("email_spam.csv", index=False)

print("Email dataset converted successfully!")
print(f"Total emails: {len(email_data)}")
print(f"Spam emails: {len(email_data[email_data['label'] == 'spam'])}")
print(f"Ham emails: {len(email_data[email_data['label'] == 'ham'])}")
