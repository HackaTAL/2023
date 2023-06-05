# coding: utf-8
"""Insert new score into db."""
import json
import random
import tempfile
from datetime import datetime
from pathlib import Path

import streamlit as st

from db import DashboardDb
from utils.filesio import mkdir
from utils.scoring import score, naive_prf_spans_score

db_path = Path("./run/dashboard.sqlite")
mkdir(db_path)


@st.cache_data()
def get_gold():
    """Return Gold data for scoring"""
    gold_file = Path("../data/dataset_hackatal_20230604.json.test")
    data = json.load(gold_file.open())

    return data


@st.cache_resource()
def prep_db():
    """Wrap db so it can be cached."""
    return DashboardDb(db_path)


st.set_page_config(
    page_title="HackaTAL 2023 - New score",
    layout="wide",
)
with st.container():
    st.title("HackaTAL 2023 - Détection de Citations.")
    st.header("Nouveau score.")

    db = prep_db()
    gold_data = get_gold()
    res = db.get_teams_mapping()
    teams = [name for name, _ in res]
    team_mapping = {name: id_team for name, id_team in res}

    # Form
    team = st.selectbox("Sélectionné votre équipe", teams)
    uploaded_file = st.file_uploader(
        "Choisissez le fichier à valider (format jsonl.gz)",
        accept_multiple_files=False,
        type=[],
    )
    run_info = st.text_input("Run info", help="Optional info about the submitted file.")
    button = st.button("Send")
    if button and uploaded_file is not None:
        # Load uploaded text
        insert_time = datetime.now()
        tmp_dir = Path(tempfile.mkdtemp(prefix="wordcloud_"))
        corpus_file = tmp_dir / Path(uploaded_file.name)
        with corpus_file.open("wb") as fh:
            fh.write(uploaded_file.read())

        predicted_data = json.load(corpus_file.open())

        scores = naive_prf_spans_score(predicted_data, gold_data)
        score_dump = json.dumps(scores)

        db.put(
            insert_time,
            team_mapping[team],
            uploaded_file.name,
            run_info,
            scores["0_f"],
            scores["0_r"],
            scores["0_p"],
            score_dump,
        )

        st.text(insert_time)
        st.table(
            [
                {
                    "insert_time": insert_time,
                    "team": team,
                    "file_name": corpus_file.name,
                    "run_info": run_info,
                    "f": scores["0_f"],
                    "r": scores["0_r"],
                    "p": scores["0_p"],
                    "score_dump": score_dump,
                }
            ]
        )
