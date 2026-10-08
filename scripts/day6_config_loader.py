"""
Day 6 - Environments & Secrets
Run this from the root folder: python scripts/day6_config_loader.py
"""
import os
from dotenv import load_dotenv
from pathlib import Path

print("=" * 40)
print("1. VIRTUAL ENVIRONMENTS & OS MODULE")
print("=" * 40)
# os.getenv() reads environment variables directly from the operating system
# We use a fallback (the second argument) in case the variable isn't set
os_env = os.getenv("ENVIRONMENT", "production")
print(f"Current Environment (from OS): {os_env}")


print("\n" + "=" * 40)
print("2. SECRETS (.env file)")
print("=" * 40)
# Find the root directory to locate the .env file
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"

# load_dotenv() reads the .env file and injects the variables into os.environ
load_dotenv(dotenv_path=env_path)

# Now we can safely read the secret!
api_key = os.getenv("AI_API_KEY")

if api_key:
    # SECURITY BEST PRACTICE: Never print full secrets to logs. 
    # Print a masked version instead.
    masked_key = api_key[:6] + "*" * (len(api_key) - 6)
    print(f"✅ API Key loaded successfully: {masked_key}")
else:
    print("❌ ERROR: API Key not found! Check your .env file.")

print("\n" + "=" * 40)
print("3. MINI PROJECT: Safe Config Loader")
print("=" * 40)
def get_config(key_name, default=None):
    """A reusable helper to safely load configs/secrets."""
    return os.getenv(key_name, default)

# Using our helper function
db_password = get_config("DB_PASSWORD", "default_pass_123")
print(f"Database Password (fallback used): {db_password}")