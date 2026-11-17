import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# Goto URL
BASE_URL = os.getenv("BASE_URL")

# Login Creds
TEST_USER_EMAIL = os.getenv("EXISTING_EMAIL")
TEST_USER_PASSWORD = os.getenv("PASSWORD")
TEST_CONFIRMED_PASSWORD = os.getenv("CONFIRM_PASSWORD")

# Registration
FIRST_NAME = os.getenv("FIRSTNAME")
LAST_NAME = os.getenv("LASTNAME")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

