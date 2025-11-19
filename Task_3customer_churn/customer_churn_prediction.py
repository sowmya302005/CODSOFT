import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def load_data():
    print("📥 Loading dataset...")
    df = pd.read_csv("Churn_Modelling.csv")
    print("Dataset Loaded Successfully!")
    return df

def preprocess(df):
    print("🛠 Preprocessing data...")

    df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

    # Encode categorical columns
    le = LabelEncoder()
    df["Gender"] = le.fit_transform(df["Gender"])

    df = pd.get_dummies(df, columns=["Geography"], drop_first=True)

    # Train-test split
    X = df.drop("Exited", axis=1)
    y = df["Exited"]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    print("Preprocessing done!")
    return X, y

def train_model(X, y):
    print("🤖 Training model...")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Model Training Done!")
    print("\nAccuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

def main():
    df = load_data()
    X, y = preprocess(df)
    train_model(X, y)

if __name__ == "__main__":
    main()
