# This is a module inside the utils package: log_helper.py

def filter_critical_logs(logs):
    """Returns only ERROR and CRITICAL logs."""
    return [log for log in logs if log["severity"] in ["ERROR", "CRITICAL"]]

def sort_logs_by_severity(logs):
    """Sorts logs from highest severity to lowest."""
    severity_rank = {"INFO": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 4}
    return sorted(logs, key=lambda log: severity_rank[log["severity"]], reverse=True)