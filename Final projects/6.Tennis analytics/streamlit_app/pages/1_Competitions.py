import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
import pandas as pd

from database.db_connection import get_engine


st.title("🎾 Competitions Analysis")

engine = get_engine()

query = """
SELECT
    c.competition_id,
    c.competition_name,
    cat.category_name,
    c.competition_type,
    c.gender,
    c.parent_id
FROM competitions c
LEFT JOIN categories cat
    ON c.category_id = cat.category_id
ORDER BY cat.category_name, c.competition_name
"""

try:
    df = pd.read_sql(query, engine)

    st.write("Rows returned:", len(df))

    if df.empty:
        st.warning("No competition data found in the database.")
    else:
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

except Exception as e:
    st.error("Error loading competition data")
    st.exception(e)