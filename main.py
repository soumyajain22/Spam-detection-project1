# Import required libraries
import pandas as pd
import numpy as np
import string
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# STEP 1: Load Dataset
# -----------------------------
# Download dataset from Kaggle: SMS Spam Collection
df = pd.read_csv("data/spam.csv", encoding='latin-1')

# Keep only required columns
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# Convert labels to binary
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# -----------------------------
# STEP 2: Text Preprocessing
# -----------------------------
def preprocess_text(text):
    text = text.lower()  # lowercase
    text = re.sub(r'\d+', '', text)  # remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    text = text.strip()
    return text

df['message'] = df['message'].apply(preprocess_text)

# -----------------------------
# STEP 3: Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.2, random_state=42
)

# -----------------------------
# STEP 4: Convert Text to Numbers (TF-IDF)
# -----------------------------
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# -----------------------------
# STEP 5: Train Model
# -----------------------------
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# -----------------------------
# STEP 6: Evaluate Model
# -----------------------------
y_pred = model.predict(X_test_tfidf)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -----------------------------
# STEP 7: Test with Custom Input
# -----------------------------
def predict_spam(message):
    processed = preprocess_text(message)
    vector = vectorizer.transform([processed])
    prediction = model.predict(vector)[0]
    
    if prediction == 1:
        return "Spam ❌"
    else:
        return "Not Spam ✅"

# Example
while True:
    user_input = input("\nEnter a message (or type 'exit'): ")
    if user_input.lower() == 'exit':
        break
    result = predict_spam(user_input)
    print("Prediction:", result)