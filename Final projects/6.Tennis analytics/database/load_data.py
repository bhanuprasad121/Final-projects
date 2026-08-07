import pandas as pd

from database.db_connection import get_engine


def load_all_data() -> None:
    """Load processed CSV files into MySQL."""

    engine = get_engine()

    categories = pd.read_csv(
        "data/processed/categories.csv"
    )

    competitions = pd.read_csv(
        "data/processed/competitions.csv"
    )

    complexes = pd.read_csv(
        "data/processed/complexes.csv"
    )

    venues = pd.read_csv(
        "data/processed/venues.csv"
    )

    competitors = pd.read_csv(
        "data/processed/competitors.csv"
    )

    rankings = pd.read_csv(
        "data/processed/competitor_rankings.csv"
    )

    # Parent tables must be loaded first.
    categories.to_sql(
        "categories",
        engine,
        if_exists="append",
        index=False
    )

    complexes.to_sql(
        "complexes",
        engine,
        if_exists="append",
        index=False
    )

    competitors.to_sql(
        "competitors",
        engine,
        if_exists="append",
        index=False
    )

    competitions.to_sql(
        "competitions",
        engine,
        if_exists="append",
        index=False
    )

    venues.to_sql(
        "venues",
        engine,
        if_exists="append",
        index=False
    )

    rankings.to_sql(
        "competitor_rankings",
        engine,
        if_exists="append",
        index=False
    )

    print("All data loaded successfully.")


if __name__ == "__main__":
    load_all_data()