import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
import pandas as pd

from database.db_connection import get_engine


st.title("🎾 Venue Analysis")

engine = get_engine()

query = """
SELECT
    v.venue_name,
    v.city_name,
    v.country_name,
    v.timezone,
    c.complex_name
FROM venues v
LEFT JOIN complexes c
    ON v.complex_id = c.complex_id
"""

df = pd.read_sql(query, engine)

st.dataframe(df, use_container_width=True)