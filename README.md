# System_Monitoring

  AI-Powered System Monitor & Anomaly Detector
  This project is a comprehensive system monitoring tool that uses machine learning to detect anomalous system behavior. It consists of three interconnected Python scripts:
  
  system_monitor.py: A script that monitors and logs key system metrics like CPU and memory usage, running processes, and network connections.
  
  train_model.py: A script that trains an Isolation Forest machine learning model on the data collected by the monitor to learn what "normal" system behavior looks like.
  
  anomaly_detector.py: A real-time monitoring script that uses the trained model to flag unusual or anomalous patterns in system usage.
  
  Features
  Comprehensive Monitoring: Tracks CPU usage, memory usage, top-consuming processes, and active network connections.
  
  Detailed Reporting: Saves monitoring data to an Excel file (system_monitor_report.xlsx) with separate sheets for system logs, alerts, and a visual CPU usage graph.
  
  Threshold-Based Alerts: Creates a cpu_threat_log.txt file and an "Alert_Tickets" sheet in the Excel report for any CPU usage that exceeds a predefined threshold.
  
  AI-Powered Anomaly Detection: Uses an Isolation Forest algorithm, a powerful method for detecting outliers, to identify subtle anomalies that simple thresholds might miss.
  
  Real-Time Detection: Once trained, the anomaly detector can run in real-time, providing immediate feedback on system status.

# How to Use
  Follow these steps in order to collect data, train the model, and run the real-time anomaly detector.
  
  Step 1: Monitor Your System to Collect Baseline Data
  First, run the system_monitor.py script to collect data about your system's typical performance. For best results, run this while you perform your usual tasks (e.g., browsing, coding, etc.) to create a realistic dataset. The script will run for a predefined duration (default is 60 seconds) and then automatically stop.
  
Output: This will generate two files:
  
  system_monitor_report.xlsx: An Excel file containing the collected system metrics, alerts, and a graph. This file is the input for the model training step.
  
  cpu_threat_log.txt: A simple text file logging any instances where CPU usage crossed the defined alert threshold.
  
  Step 2: Train the Anomaly Detection Model
  Next, use the data you just collected to train the AI model. The train_model.py script reads the Excel report and creates a model file.
  
Output: This will create one file:
  
  anomaly_detector.joblib: This file contains the trained machine learning model, ready to be used for real-time detection.
  
  Step 3: Run the Real-Time Anomaly Detector
  With a trained model, you can now run the anomaly_detector.py script to monitor your system in real-time. It will use the model to analyze current CPU and memory usage and will flag any data points it considers anomalous.
  How it Works: The script will print the system status to your console every few seconds. If it detects something unusual, it will display an "ANOMALY DETECTED" message. Press CTRL+C to stop the script.

Output:

  system_log.csv: A CSV file that logs the real-time monitoring data for future analysis.

# Customization
  You can easily customize the behavior of the system_monitor.py script by changing the global variables at the top of the file:
  
  LOG_INTERVAL_SECONDS: How often (in seconds) to log data.
  
  RUN_DURATION_SECONDS: Total time (in seconds) the monitoring script should run.
  
  CPU_ALERT_THRESHOLD: The CPU percentage that will trigger a high-usage alert.
  
  OUTPUT_FILENAME: The name of the output Excel report.
  
  THREAT_LOG_FILENAME: The name of the CPU alert log file.
