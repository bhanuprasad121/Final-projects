import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SPORTRADAR_API_KEY")

BASE_URL = "https://api.sportradar.com/tennis/trial/v3/en"

HEADERS = {
    "accept": "application/json",
    "x-api-key": API_KEY
}

