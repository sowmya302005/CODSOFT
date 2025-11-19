import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def load_data():
    print("📥 Loading dataset...")

    train_path = "fraudTrain.csv"
    test_path = "fraudTest.csv"

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    print("Dataset loaded successfully!")
    return train_df, test_df

def preprocess_data(df):
    print("🛠 Preprocessing data...")

    # Remove columns that should NOT be used for ML
    drop_cols = ["trans_date_trans_time", "dob", "unix_time", "merchant", 
                 "job", "first", "last", "street", "city", "state", 
                 "zip", "trans_num"]

    for col in drop_cols:
        if col in df.columns:
            df = df.drop(col, axis=1)

    # Encode only SMALL categorical columns
    categorical_cols = ["category", "gender"]

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype("category").cat.codes

    print("Preprocessing done!")
    return df


def main():
    train_df, test_df = load_data()

    train_df = preprocess_data(train_df)
    test_df = preprocess_data(test_df)

    X = train_df.drop("is_fraud", axis=1)
    y = train_df["is_fraud"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LogisticRegression(max_iter=500)
    model.fit(X_scaled, y)

    print("Model training done!")

    test_df_scaled = scaler.transform(test_df.drop("is_fraud", axis=1))
    y_pred = model.predict(test_df_scaled)

    print("Accuracy:", accuracy_score(test_df["is_fraud"], y_pred))
    print("Classification Report:")
    print(classification_report(test_df["is_fraud"], y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(test_df["is_fraud"], y_pred))

if __name__ == "__main__":
    main()
