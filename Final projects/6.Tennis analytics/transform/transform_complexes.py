import json
from pathlib import Path

import pandas as pd


def transform_complexes():
    input_path = Path("data/raw/complexes.json")

    if not input_path.exists():
        raise FileNotFoundError(
            "data/raw/complexes.json was not found. "
            "Run python -m api.extract_complexes first."
        )

    with input_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    complexes = data.get("complexes", [])

    if not complexes:
        print("No complexes found in the API response.")
        print("Check data/raw/complexes.json")
        return None, None

    complex_rows = []
    venue_rows = []

    for complex_item in complexes:
        complex_id = complex_item.get("id")

        complex_rows.append({
            "complex_id": complex_id,
            "complex_name": complex_item.get("name")
        })

        for venue in complex_item.get("venues", []):
            venue_rows.append({
                "venue_id": venue.get("id"),
                "venue_name": venue.get("name"),
                "city_name": venue.get("city_name"),
                "country_name": venue.get("country_name"),
                "timezone": venue.get("timezone"),
                "complex_id": complex_id
            })

    complexes_df = pd.DataFrame(
        complex_rows,
        columns=["complex_id", "complex_name"]
    )

    venues_df = pd.DataFrame(
        venue_rows,
        columns=[
            "venue_id",
            "venue_name",
            "city_name",
            "country_name",
            "timezone",
            "complex_id"
        ]
    )

    complexes_df.drop_duplicates(
        subset=["complex_id"],
        inplace=True
    )

    if not venues_df.empty:
        venues_df.drop_duplicates(
            subset=["venue_id"],
            inplace=True
        )

    Path("data/processed").mkdir(
        parents=True,
        exist_ok=True
    )

    complexes_df.to_csv(
        "data/processed/complexes.csv",
        index=False
    )

    venues_df.to_csv(
        "data/processed/venues.csv",
        index=False
    )

    print("Complexes rows:", len(complexes_df))
    print("Venues rows:", len(venues_df))
    print("Complex data transformed successfully.")

    return complexes_df, venues_df


if __name__ == "__main__":
    transform_complexes()