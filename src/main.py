import streamlit as st
import pandas as pd
from io_data import read_json
from pathlib import Path
from _utils import client
import os
from typing import Any

st.set_page_config(
    page_title="LoPO",
    page_icon="🗒️",
    layout="wide"
)

L_EXAMPLES_STUDY = ["BP12345", "BP5555", "BP8775"]
FIELDS = read_json(Path("src", "column_header.json"))

with st.sidebar:
    option = st.selectbox(
        'Select your study',
        L_EXAMPLES_STUDY
    )
    st.subheader('Welcome on the study "{}"'.format(option))
    sheet = st.radio(
        label = "Select the sheet you want to update 👇",
        options = ["SDTM", "ADAM", "LOPO"],
        index=0
    )

# if "df_value_sdtm" not in st.session_state:
#     st.session_state.df_value_sdtm = df_sdtm
# if "df_value_adam" not in st.session_state:
#     st.session_state.df_value_adam = df_adam
# if "df_value_lopo" not in st.session_state:
#     st.session_state.df_value_lopo = df_lopo

def save_changes(submit_changes: Any, df_sdtm: pd.DataFrame):
    if submit_changes:
        client.download_file(
            Bucket="lopo-streamlit", 
            Key="df_sdtm.csv", 
            Filename="df_sdtm_after_edition.csv"
        )
        df_sdtm_after_edition = pd.read_csv("df_sdtm_after_edition.csv", keep_default_na=False)
        if df_sdtm_after_edition.equals(df_sdtm):
            edited_df_sdtm.to_csv("df_sdtm.csv", index=False)
            client.upload_file(
                Bucket="lopo-streamlit", 
                Key="df_sdtm.csv", 
                Filename="df_sdtm.csv"
            )
            os.remove("df_sdtm.csv")
            os.remove("df_sdtm_after_edition.csv")
            st.experimental_rerun()
        else:
            st.error(body="The LoPO has been modified by someone else in the meantime")


def display_current():
    client.download_file(
        Bucket="lopo-streamlit", 
        Key="df_sdtm.csv", 
        Filename="df_sdtm.csv"
    )
    df_sdtm = pd.read_csv("df_sdtm.csv", keep_default_na=False)
    os.remove(path="df_sdtm.csv")
    return df_sdtm

if sheet == "SDTM":
    df_sdtm = display_current()
    st.title("Current LoPO")
    st.dataframe(df_sdtm)
    st.title("Edition Mode")
    edited_df_sdtm = st.data_editor(df_sdtm, num_rows="dynamic")
    submit_changes = st.button(
        label="Submit changes"
    )
    save_changes(submit_changes = submit_changes, df_sdtm = df_sdtm)
        






# if edited_df_sdtm is not None and not edited_df_sdtm.equals(st.session_state["df_value"]):
#     # This will only run if
#     # 1. Some widget has been changed (including the dataframe editor), triggering a
#     # script rerun, and
#     # 2. The new dataframe value is different from the old value
#     st.session_state["df_value_sdtm"] = edited_df_sdtm

# if edited_df_adam is not None and not edited_df_adam.equals(st.session_state["df_value_adam"]):
#     # This will only run if
#     # 1. Some widget has been changed (including the dataframe editor), triggering a
#     # script rerun, and
#     # 2. The new dataframe value is different from the old value
#     st.session_state["df_value_adam"] = edited_df_adam


# if edited_df_lopo is not None and not edited_df_lopo.equals(st.session_state["df_value_lopo"]):
#     # This will only run if
#     # 1. Some widget has been changed (including the dataframe editor), triggering a
#     # script rerun, and
#     # 2. The new dataframe value is different from the old value
#     st.session_state["df_value_lopo"] = edited_df_lopo