import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
import pandas as pd

from database.db_connection import get_engine


st.title("🏆 Competitor Rankings")

engine = get_engine()

query = """
SELECT
    c.name,
    c.country,
    c.country_code,
    r.rank_position,
    r.movement,
    r.points,
    r.competitions_played
FROM competitor_rankings r
JOIN competitors c
    ON r.competitor_id = c.competitor_id
ORDER BY r.rank_position
"""

df = pd.read_sql(query, engine)

st.dataframe(df, use_container_width=True)