import pandas as pd
import streamlit as st

import sys
from pathlib import Path

# Add the project root to Python's import path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from database.db_connection import get_engine


st.set_page_config(
    page_title="Tennis Analytics",
    page_icon="🎾",
    layout="wide"
)

st.title("🎾 Tennis Game Analytics")

engine = get_engine()

total_competitors = pd.read_sql(
    "SELECT COUNT(*) AS total FROM competitors",
    engine
).iloc[0]["total"]

total_countries = pd.read_sql(
    """
    SELECT COUNT(DISTINCT country_code) AS total
    FROM competitors
    """,
    engine
).iloc[0]["total"]

highest_points = pd.read_sql(
    """
    SELECT MAX(points) AS highest_points
    FROM competitor_rankings
    """,
    engine
).iloc[0]["highest_points"]

col1, col2, col3 = st.columns(3)

col1.metric("Total Competitors", total_competitors)
col2.metric("Countries Represented", total_countries)
col3.metric("Highest Points", highest_points)

st.subheader("🔍 Competitor Search & Filters")

# Get competitor data
competitor_df = pd.read_sql(
    """
    SELECT
        c.name,
        c.country,
        c.country_code,
        r.rank_position,
        r.points,
        r.movement,
        r.competitions_played
    FROM competitor_rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id
    """,
    engine
)

# Search by name
search_name = st.text_input(
    "Search competitor by name"
)

# Country filter
country_options = ["All"] + sorted(
    competitor_df["country"]
    .dropna()
    .unique()
    .tolist()
)

selected_country = st.selectbox(
    "Select Country",
    country_options
)

# Rank range
min_rank = int(competitor_df["rank_position"].min())
max_rank = int(competitor_df["rank_position"].max())

rank_range = st.slider(
    "Select Rank Range",
    min_rank,
    max_rank,
    (min_rank, max_rank)
)

# Points threshold
min_points = st.number_input(
    "Minimum Points",
    min_value=0,
    value=0
)

filtered_df = competitor_df.copy()

if search_name:
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(
            search_name,
            case=False,
            na=False
        )
    ]

if selected_country != "All":
    filtered_df = filtered_df[
        filtered_df["country"] == selected_country
    ]

filtered_df = filtered_df[
    filtered_df["rank_position"].between(
        rank_range[0],
        rank_range[1]
    )
]

filtered_df = filtered_df[
    filtered_df["points"] >= min_points
]

st.write("Matching Competitors:", len(filtered_df))

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

st.subheader("Top-Ranked Competitors")

leaderboard = pd.read_sql(
    """
    SELECT
        c.name,
        c.country,
        r.rank_position,
        r.points,
        r.movement
    FROM competitor_rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id
    ORDER BY r.rank_position
    LIMIT 20
    """,
    engine
)

st.dataframe(
    leaderboard,
    use_container_width=True,
    hide_index=True
)