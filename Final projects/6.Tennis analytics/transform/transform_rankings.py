import json
from pathlib import Path

import pandas as pd


def transform_rankings() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Transform nested rankings into competitor tables."""

    input_path = Path("data/raw/rankings.json")

    with input_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    competitor_rows = []
    ranking_rows = []

    rank_id = 1

    for ranking_group in data.get("rankings", []):
        for ranking in ranking_group.get(
            "competitor_rankings",
            []
        ):
            competitor = ranking.get("competitor") or {}

            competitor_id = (
                ranking.get("competitor_id")
                or competitor.get("id")
            )

            competitor_rows.append({
                "competitor_id": competitor_id,
                "name": competitor.get("name"),
                "country": competitor.get("country"),
                "country_code": competitor.get("country_code")
            })

            ranking_rows.append({
                "rank_id": rank_id,
                "competitor_id": competitor_id,
                "rank_position": ranking.get("rank"),
                "movement": ranking.get("movement"),
                "points": ranking.get("points"),
                "competitions_played": ranking.get(
                    "competitions_played"
                )
            })

            rank_id += 1

    competitors_df = pd.DataFrame(competitor_rows)
    rankings_df = pd.DataFrame(ranking_rows)

    competitors_df.drop_duplicates(
        subset=["competitor_id"],
        inplace=True
    )

    rankings_df.drop_duplicates(
        subset=["rank_id"],
        inplace=True
    )

    competitors_df.to_csv(
        "data/processed/competitors.csv",
        index=False
    )

    rankings_df.to_csv(
        "data/processed/competitor_rankings.csv",
        index=False
    )

    print("Ranking data transformed successfully.")

    return competitors_df, rankings_df


if __name__ == "__main__":
    transform_rankings()