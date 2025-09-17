import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

INPUT_DATA_FILE = 'system_monitor_report.xlsx'
MODEL_FILENAME = 'anomaly_detector.joblib'

def train_model():
    print(f"Loading data from {INPUT_DATA_FILE}...")
    try:
        df = pd.read_excel(INPUT_DATA_FILE, sheet_name='System_Log')
    except FileNotFoundError:
        print(f"Error: The file {INPUT_DATA_FILE} was not found.")
        print("Please run the monitoring script first to generate the report.")
        return

    features = ['CPU Usage (%)', 'Memory Usage (%)']
    X = df[features]

    print("Training the anomaly detection model...")
    model = IsolationForest(contamination='auto', random_state=42)
    model.fit(X)

    print(f"Saving the trained model to {MODEL_FILENAME}...")
    joblib.dump(model, MODEL_FILENAME)
    print("Model training complete and saved successfully.")

if __name__ == "__main__":
    train_model()
