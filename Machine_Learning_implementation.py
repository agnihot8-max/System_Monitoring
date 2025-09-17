import psutil
import time
import pandas as pd
import joblib
from datetime import datetime

LOG_INTERVAL_SECONDS = 5
MODEL_FILENAME = 'anomaly_detector.joblib'
LOG_FILENAME = 'system_log.csv'


def main():

    print(f"Loading anomaly detection model from {MODEL_FILENAME}...")
    try:
        model = joblib.load(MODEL_FILENAME)
    except FileNotFoundError:
        print(f"Error: Model file '{MODEL_FILENAME}' not found.")
        print("Please run the 'train_model.py' script first.")
        return

    print(" Starting system monitoring with anomaly detection...")

    log_file_header_written = False

    try:
        while True:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cpu_usage = psutil.cpu_percent(interval=None)
            memory_info = psutil.virtual_memory()


            features = pd.DataFrame(
                [[cpu_usage, memory_info.percent]],
                columns=['CPU Usage (%)', 'Memory Usage (%)']
            )


            prediction = model.predict(features)


            status = "Normal"
            if prediction[0] == -1:
                status = "ANOMALY DETECTED"

            print(f"[{timestamp}] | CPU: {cpu_usage}% | Memory: {memory_info.percent}% | Status: {status}")

            if status == "ANOMALY DETECTED":
                print("  Unusual system behavior detected!")

            current_data = {
                'Timestamp': timestamp,
                'CPU Usage (%)': cpu_usage,
                'Memory Usage (%)': memory_info.percent,
            }
            df_to_log = pd.DataFrame([current_data])
            try:
                with open(LOG_FILENAME, 'x') as f:
                    df_to_log.to_csv(f, header=True, index=False)
            except FileExistsError:
                with open(LOG_FILENAME, 'a') as f:
                    df_to_log.to_csv(f, header=False, index=False)

            time.sleep(LOG_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("\n Monitoring stopped by user.")


if __name__ == "__main__":

    main()
