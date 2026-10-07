"""
Day 5 - File Formats (CSV, JSON, pathlib)
Run this from the root folder: python scripts/day5_file_formats.py
"""
import csv
import json
from pathlib import Path

print("=" * 40)
print("1. PATHLIB - Robust File Paths")
print("=" * 40)
# Path(__file__) gets the current script's path.
# .resolve().parent.parent goes up two levels to the project root (month2-aiops-lab)
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

json_file_path = DATA_DIR / "config.json"
csv_file_path = DATA_DIR / "servers.csv"
report_file_path = DATA_DIR / "alert_report.csv"

print(f"Project Root: {BASE_DIR}")
print(f"Data Folder:  {DATA_DIR}")
print(f"Config File Exists: {json_file_path.exists()}")


print("\n" + "=" * 40)
print("2. JSON - Reading Configuration")
print("=" * 40)
# Reading a JSON file into a Python dictionary
with open(json_file_path, "r") as file:
    config = json.load(file)

cpu_limit = config["cpu_threshold"]
mem_limit = config["memory_threshold"]

print(f"System: {config['system_name']}")
print(f"Thresholds -> CPU: {cpu_limit}% | Memory: {mem_limit}%")


print("\n" + "=" * 40)
print("3. CSV - Reading Server Data")
print("=" * 40)
# Reading a CSV file into a list of dictionaries
server_data = []
with open(csv_file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        server_data.append(row)

print(f"Successfully loaded {len(server_data)} servers from CSV.")


print("\n" + "=" * 40)
print("4. MINI PROJECT: Generate Alert Report")
print("=" * 40)
# Logic: Compare CSV data against JSON thresholds and write a new CSV report.
report_data = []

for server in server_data:
    cpu = int(server["cpu_usage"])
    mem = int(server["memory_usage"])
    
    issues = []
    if cpu >= cpu_limit:
        issues.append(f"CPU high ({cpu}%)")
    if mem >= mem_limit:
        issues.append(f"Memory high ({mem}%)")
        
    # If there are any issues, add to the report
    if issues:
        report_data.append({
            "server_name": server["server_name"],
            "issues": " & ".join(issues),
            "action_required": "YES"
        })

# Writing the report to a new CSV file
with open(report_file_path, "w", newline="") as file:
    fieldnames = ["server_name", "issues", "action_required"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader() # Write the header row
    writer.writerows(report_data) # Write all the data rows

print(f"✅ Report generated successfully!")
print(f"File saved to: {report_file_path}")
print(f"Total alerts generated: {len(report_data)}")