# coding: utf-8
"""Display hackatal2023 all scores."""
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

from db import DashboardDb
from utils.filesio import mkdir

db_path = Path("./run/dashboard.sqlite")
mkdir(db_path)


@st.cache_resource()
def prep_db():
    """Wrap db so it can be cached."""
    return DashboardDb(db_path)


st.set_page_config(
    page_title="HackaTAL 2023 - Leader board",
    layout="wide",
)
with st.container():
    st.title("HackaTAL 2023 - Détection de Citations.")
    st.header("Tous les scores des fichiers soumis.")

    db = prep_db()
    all = db.get_all()
    all_as_df = pd.DataFrame.from_records(all)
    st.text(datetime.now())
    st.dataframe(all_as_df)
