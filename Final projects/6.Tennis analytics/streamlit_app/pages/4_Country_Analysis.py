import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
import pandas as pd

from database.db_connection import get_engine


st.title("🌍 Country Analysis")

engine = get_engine()

query = """
SELECT
    c.country,
    COUNT(DISTINCT c.competitor_id) AS total_competitors,
    ROUND(AVG(r.points), 2) AS average_points
FROM competitors c
JOIN competitor_rankings r
    ON c.competitor_id = r.competitor_id
WHERE c.country IS NOT NULL
GROUP BY c.country
ORDER BY total_competitors DESC
"""

df = pd.read_sql(query, engine)

st.dataframe(df, use_container_width=True)