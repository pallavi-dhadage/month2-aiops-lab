"""
Day 3 - Functional Helpers (lambda, map, filter, sorted)
Run this file using: python scripts/day3_functional_helpers.py
"""

print("=" * 40)
print("1. LAMBDA")
print("=" * 40)
# A lambda is a small, anonymous function written in one line.
# Syntax: lambda arguments : expression

# Regular function
def add_regular(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

print(f"Regular add: {add_regular(5, 3)}")
print(f"Lambda add:  {add_lambda(5, 3)}")


print("\n" + "=" * 40)
print("2. MAP()")
print("=" * 40)
# map() applies a function to every item in an iterable (like a list).
# It returns a map object, so we wrap it in list() to see the results.

numbers = [1, 2, 3, 4, 5]

# Using map() with a lambda to square every number
squared = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared:  {squared}")

# AIOps use case: Converting a list of string numbers to integers
str_numbers = ["100", "200", "300"]
int_numbers = list(map(int, str_numbers))
print(f"Strings: {str_numbers} -> Integers: {int_numbers}")


print("\n" + "=" * 40)
print("3. FILTER()")
print("=" * 40)
# filter() extracts only the items where the function returns True.

# Keeping only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# AIOps use case: Filtering out empty strings or None values
raw_data = ["server1", "", "server2", None, "server3"]
clean_data = list(filter(None, raw_data)) # filter(None, ...) removes falsy values
print(f"Clean Data: {clean_data}")


print("\n" + "=" * 40)
print("4. SORTED() AND CUSTOM SORT KEYS")
print("=" * 40)
# sorted() returns a new sorted list. You can pass a 'key' function to customize sorting.

words = ["banana", "apple", "cherry", "date"]

# Sort alphabetically (default)
print(f"Alphabetical: {sorted(words)}")

# Sort by length of the word
print(f"By length:    {sorted(words, key=len)}")

# Sort in reverse
print(f"Reverse length: {sorted(words, key=len, reverse=True)}")


print("\n" + "=" * 40)
print("5. MINI PROJECT: SORT AND FILTER LOG ENTRIES BY SEVERITY")
print("=" * 40)

# Here is some raw log data (a list of dictionaries)
logs = [
    {"time": "10:00:05", "severity": "INFO", "msg": "User logged in"},
    {"time": "10:02:15", "severity": "WARNING", "msg": "Disk space low"},
    {"time": "10:05:30", "severity": "ERROR", "msg": "DB connection failed"},
    {"time": "10:01:00", "severity": "INFO", "msg": "Page loaded"},
    {"time": "10:10:00", "severity": "CRITICAL", "msg": "Server down"},
]

# 1. Filter out only ERROR and CRITICAL logs
critical_logs = list(filter(lambda log: log["severity"] in ["ERROR", "CRITICAL"], logs))
print("\n--- Critical Alerts Found ---")
for log in critical_logs:
    print(f"[{log['severity']}] {log['msg']}")

# 2. Sort all logs by severity (Custom Order)
# We define a dictionary to assign a numerical rank to each severity level
severity_rank = {"INFO": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 4}

# Sort the logs based on the severity rank
sorted_logs = sorted(logs, key=lambda log: severity_rank[log["severity"]], reverse=True)

print("\n--- All Logs Sorted by Severity (Highest to Lowest) ---")
for log in sorted_logs:
    print(f"[{log['severity']:8}] {log['time']} - {log['msg']}")