import json
from pathlib import Path

import requests

from api.api_config import BASE_URL, HEADERS


def extract_rankings():
    url = f"{BASE_URL}/double_competitors_rankings.json"

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=30
        )

        print("Status code:", response.status_code)
        print("Response preview:", response.text[:500])

        response.raise_for_status()

        data = response.json()

        output_path = Path("data/raw/rankings.json")
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with output_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Rankings data extracted successfully.")
        return data

    except requests.exceptions.HTTPError as error:
        print("HTTP error:", error)
        return {}

    except requests.exceptions.JSONDecodeError:
        print("Response was not valid JSON.")
        print(response.text[:1000])
        return {}

    except requests.exceptions.RequestException as error:
        print("Request error:", error)
        return {}


if __name__ == "__main__":
    extract_rankings()