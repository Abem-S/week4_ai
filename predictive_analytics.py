# Task 3: Predictive Analytics for Resource Allocation
# Using Kaggle Breast Cancer dataset to simulate issue priority prediction

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Dataset
# Make sure you have downloaded 'breast_cancer.csv' from Kaggle and placed it in the same folder
df = pd.read_csv("breast_cancer.csv")

# 2. Quick Exploration
print("Dataset shape:", df.shape)
print(df.head())

# 3. Preprocessing
# Drop unnecessary columns if any (like ID)
if 'id' in df.columns:
    df = df.drop(columns=['id'])

# Encode target variable as numerical (simulate issue priority)
# Original 'diagnosis' is M=Malignant, B=Benign
# Map to numerical labels: Malignant=2 (high), Benign=1 (medium)
df['priority'] = df['diagnosis'].map({'M': 2, 'B': 1})

# Drop original diagnosis column
df = df.drop(columns=['diagnosis'])

# Features and target
X = df.drop(columns=['priority'])
y = df['priority']

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 5. Predict on test set
y_pred = clf.predict(X_test)

# 6. Evaluate model
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
print(f"Accuracy: {accuracy:.4f}")
print(f"F1-score: {f1:.4f}")

# Detailed classification report
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix visualization
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=['Medium','High'], yticklabels=['Medium','High'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.savefig("confusion_matrix.png")
