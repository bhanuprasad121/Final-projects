import json
from pathlib import Path

import requests

from api.api_config import BASE_URL, HEADERS


def extract_complexes() -> dict:
    """Extract complexes and venues from Sportradar."""

    url = f"{BASE_URL}/complexes.json"

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        output_path = Path("data/raw/complexes.json")

        with output_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Complexes data extracted successfully.")
        return data

    except requests.exceptions.RequestException as error:
        print(f"Complexes API error: {error}")
        return {}


if __name__ == "__main__":
    extract_complexes()