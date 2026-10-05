"""
Day 5 - File Formats (CSV, JSON, pathlib)
Run this from the root folder: python scripts/day5_file_formats.py
"""
import csv
import json
from pathlib import Path  # Modern way to handle file paths

print("=" * 40)
print("1. PATHLIB - Robust File Paths")
print("=" * 40)
# Path(__file__) gets the current script's path.
# .resolve().parent.parent goes up two levels to the project root (month2-aiops-lab)
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

json_file_path = DATA_DIR / "config.json"
csv_file_path = DATA_DIR / "servers.csv"

print(f"Base Directory: {BASE_DIR}")
print(f"Data Directory: {DATA_DIR}")
print(f"Checking if config exists: {json_file_path.exists()}")


print("\n" + "=" * 40)
print("2. JSON - Reading Configuration")
print("=" * 40)
# Reading a JSON file
with open(json_file_path, "r") as file:
    config = json.load(file)

print(f"System: {config['system_name']}")
print(f"CPU Threshold: {config['cpu_threshold']}%")
print(f"Alerts go to: {', '.join(config['alert_emails'])}")


print("\n" + "=" * 40)
print("3. CSV - Reading Server Data")
print("=" * 40)
# Reading a CSV file into a list of dictionaries
server_data = []
with open(csv_file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        server_data.append(row)

for server in server_data:
    print(f"Server: {server['server_name']} | CPU: {server['cpu_usage']}% | Mem: {server['memory_usage']}%")


print("\n" + "=" * 40)
print("4. MINI PROJECT: Read JSON config + Write CSV report")
print("=" * 40)
# Logic: Read the thresholds from JSON, check the servers CSV, 
# and write a new CSV report containing ONLY the servers that breach the thresholds.

report_data = []
cpu_limit = config["cpu_threshold"]
mem_limit = config["memory_threshold"]

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
report_file_path = DATA_DIR / "alert_report.csv"
with open(report_file_path, "w", newline="") as file:
    # These are the column headers for our new CSV
    fieldnames = ["server_name", "issues", "action_required"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader() # Write the header row
    writer.writerows(report_data) # Write all the data rows

print(f"✅ Report generated successfully at: {report_file_path}")
print(f"Total alerts generated: {len(report_data)}")