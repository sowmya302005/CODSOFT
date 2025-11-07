# 🎬 CODSOFT - Machine Learning Task 1
# Movie Genre Classification using TF-IDF + Logistic Regression
# Author: [Shetty Sowmya]
# Date: [07/11/2025]
# ---------------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 🚀 Step 1: Load the dataset
print("🔹 Loading dataset...")
print("🔹 Loading dataset...")

# Read dataset using the correct delimiter (:::) and set column names
df = pd.read_csv(
    "C:/Users/user/Desktop/CODSOFT/Task-1_movie_genere/Genre Classification Dataset/train_data.txt",
    sep=" ::: ",
    engine="python",
    names=["id", "movie_name", "genre", "plot"]
)

print("✅ Dataset loaded successfully!")
print(df.head(), "\n")

# Check for missing values
print("🔹 Checking for missing values...")
print(df.isnull().sum())

# Keep only useful columns
df = df[["plot", "genre"]].dropna()

print("✅ Cleaned dataset ready!")

df['plot'] = df['plot'].str.lower()

# 🧩 Step 3: Split the dataset
X = df['plot']
y = df['genre']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\n✅ Data split complete!")
print(f"Training samples: {len(X_train)} | Testing samples: {len(X_test)}")

# 🔠 Step 4: Convert text to numerical vectors using TF-IDF
print("\n🔹 Extracting text features using TF-IDF...")
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)
print("✅ TF-IDF vectorization complete!")

# 🤖 Step 5: Train the Logistic Regression model
print("\n🔹 Training the model...")
model = LogisticRegression(max_iter=300)
model.fit(X_train_tfidf, y_train)
print("✅ Model training complete!")

# 📊 Step 6: Evaluate the model
y_pred = model.predict(X_test_tfidf)

print("\n🎯 Model Evaluation:")
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 🎥 Step 7: Try predicting a new movie plot
print("\n🎬 Test your model with a new movie plot!")
sample_plot = ["A young wizard discovers he has magical powers and goes to a school for wizards."]
sample_tfidf = vectorizer.transform(sample_plot)
predicted_genre = model.predict(sample_tfidf)[0]
print(f"Predicted Genre: {predicted_genre}")

print("\n✅ Task Completed Successfully!")
