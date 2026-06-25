from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

app = Flask(__name__)

# ==================== EMAIL SPAM DETECTION ====================

# Load email dataset
email_data = pd.read_csv("email_spam.csv")

# Features and labels for email
X_email = email_data["text"]
y_email = email_data["label"]

# Convert text to TF-IDF vectors (better than CountVectorizer for email)
email_vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_email_vec = email_vectorizer.fit_transform(X_email)

# Split dataset
X_train_email, X_test_email, y_train_email, y_test_email = train_test_split(
    X_email_vec, y_email, test_size=0.2, random_state=42
)

# Train model with Random Forest for better performance
email_model = RandomForestClassifier(n_estimators=100, random_state=42)
email_model.fit(X_train_email, y_train_email)

# Calculate metrics
y_pred_email = email_model.predict(X_test_email)
email_accuracy = round(accuracy_score(y_test_email, y_pred_email) * 100, 2)
email_precision = round(precision_score(y_test_email, y_pred_email, average='weighted') * 100, 2)
email_recall = round(recall_score(y_test_email, y_pred_email, average='weighted') * 100, 2)
email_f1 = round(f1_score(y_test_email, y_pred_email, average='weighted') * 100, 2)

print("=== EMAIL SPAM DETECTOR ===")
print(f"Accuracy: {email_accuracy}%")
print(f"Precision: {email_precision}%")
print(f"Recall: {email_recall}%")
print(f"F1-Score: {email_f1}%")

# ==================== SMS SPAM DETECTION ====================

# Load SMS dataset
sms_data = pd.read_csv("spam.csv")

# Features and labels for SMS
X_sms = sms_data["message"]
y_sms = sms_data["label"]

# Convert text to numbers for SMS
sms_vectorizer = TfidfVectorizer(max_features=3000, stop_words='english')
X_sms_vec = sms_vectorizer.fit_transform(X_sms)

# Split dataset
X_train_sms, X_test_sms, y_train_sms, y_test_sms = train_test_split(
    X_sms_vec, y_sms, test_size=0.2, random_state=42
)

# Train model
sms_model = RandomForestClassifier(n_estimators=100, random_state=42)
sms_model.fit(X_train_sms, y_train_sms)

# Calculate metrics
y_pred_sms = sms_model.predict(X_test_sms)
sms_accuracy = round(accuracy_score(y_test_sms, y_pred_sms) * 100, 2)
sms_precision = round(precision_score(y_test_sms, y_pred_sms, average='weighted') * 100, 2)
sms_recall = round(recall_score(y_test_sms, y_pred_sms, average='weighted') * 100, 2)
sms_f1 = round(f1_score(y_test_sms, y_pred_sms, average='weighted') * 100, 2)

print("\n=== SMS SPAM DETECTOR ===")
print(f"Accuracy: {sms_accuracy}%")
print(f"Precision: {sms_precision}%")
print(f"Recall: {sms_recall}%")
print(f"F1-Score: {sms_f1}%")

# ==================== ROUTES ====================

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template(
        "dashboard.html",
        email_accuracy=email_accuracy,
        sms_accuracy=sms_accuracy,
        email_precision=email_precision,
        sms_precision=sms_precision,
        email_recall=email_recall,
        sms_recall=sms_recall,
        email_f1=email_f1,
        sms_f1=sms_f1
    )

@app.route("/detect-sms", methods=["POST"])
def detect_sms():
    data = request.json
    message = data.get("message", "").strip()
    
    if not message:
        return jsonify({"error": "Message cannot be empty"}), 400
    
    # Predict
    message_vector = sms_vectorizer.transform([message])
    result = sms_model.predict(message_vector)[0]
    confidence = max(sms_model.predict_proba(message_vector)[0]) * 100
    
    prediction_text = "🚨 Spam Message" if result == "spam" else "✅ Safe Message"
    
    return jsonify({
        "result": prediction_text,
        "type": result,
        "confidence": round(confidence, 2),
        "accuracy": sms_accuracy
    })

@app.route("/detect-email", methods=["POST"])
def detect_email():
    data = request.json
    message = data.get("message", "").strip()
    
    if not message:
        return jsonify({"error": "Message cannot be empty"}), 400
    
    # Predict
    message_vector = email_vectorizer.transform([message])
    result = email_model.predict(message_vector)[0]
    confidence = max(email_model.predict_proba(message_vector)[0]) * 100
    
    prediction_text = "🚨 Spam Email" if result == "spam" else "✅ Legitimate Email"
    
    return jsonify({
        "result": prediction_text,
        "type": result,
        "confidence": round(confidence, 2),
        "accuracy": email_accuracy
    })

@app.route("/api/metrics", methods=["GET"])
def get_metrics():
    return jsonify({
        "sms": {
            "accuracy": sms_accuracy,
            "precision": sms_precision,
            "recall": sms_recall,
            "f1": sms_f1
        },
        "email": {
            "accuracy": email_accuracy,
            "precision": email_precision,
            "recall": email_recall,
            "f1": email_f1
        }
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
