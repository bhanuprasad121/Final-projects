import json
from pathlib import Path

import pandas as pd


def transform_competitions() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Transform competition JSON into relational tables."""

    input_path = Path("data/raw/competitions.json")

    with input_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    category_rows = []
    competition_rows = []

    for competition in data.get("competitions", []):
        category = competition.get("category") or {}

        category_rows.append({
            "category_id": category.get("id"),
            "category_name": category.get("name")
        })

        competition_rows.append({
            "competition_id": competition.get("id"),
            "competition_name": competition.get("name"),
            "category_id": category.get("id"),
            "competition_type": competition.get("type"),
            "gender": competition.get("gender"),
            "parent_id": competition.get("parent_id")
        })

    categories_df = pd.DataFrame(category_rows)
    categories_df.drop_duplicates(
        subset=["category_id"],
        inplace=True
    )

    competitions_df = pd.DataFrame(competition_rows)
    competitions_df.drop_duplicates(
        subset=["competition_id"],
        inplace=True
    )

    categories_df.to_csv(
        "data/processed/categories.csv",
        index=False
    )

    competitions_df.to_csv(
        "data/processed/competitions.csv",
        index=False
    )

    print("Competition data transformed successfully.")

    return categories_df, competitions_df


if __name__ == "__main__":
    transform_competitions()