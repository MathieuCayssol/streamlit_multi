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

def display_current(filename: str):
    client.download_file(
        Bucket="lopo-streamlit", 
        Key=filename, 
        Filename=filename
    )
    df = pd.read_csv(filename, keep_default_na=False)
    os.remove(path=filename)
    return df

def save_changes(submit_changes: Any, filename: str, df: pd.DataFrame):
    if submit_changes:
        df.to_csv(filename, index=False)
        client.upload_file(
            Bucket="lopo-streamlit", 
            Key=filename, 
            Filename=filename
        )
        os.remove(filename)
        st.experimental_rerun()


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
    l_rep_group = [x for x in display_current(filename="df_sdtm.csv").columns if "reporting_group_" in x]
    with st.expander("Add a reporting group"):
        rg_add = st.text_input(
            label = 'Enter the reporting group you want to add'
        )
        rg_btn_add = st.button(
            label="Add"
        )
        if rg_btn_add:
            df_sdtm = display_current(filename="df_sdtm.csv").insert(loc=10+len(l_rep_group), column=f"reporting_group_{rg_add}", value=False)
            df_adam = display_current(filename="df_adam.csv").insert(loc=10+len(l_rep_group), column=f"reporting_group_{rg_add}", value=False)
            df_tlg = display_current(filename="df_lopo.csv").insert(loc=10+len(l_rep_group), column=f"reporting_group_{rg_add}", value=False)
            save_changes(submit_changes = rg_btn_add, filename = "df_sdtm.csv", df = df_sdtm)
            save_changes(submit_changes = rg_btn_add, filename = "df_adam.csv", df = df_adam)
            save_changes(submit_changes = rg_btn_add, filename = "df_lopo.csv", df = df_tlg)

    with st.expander("Delete a reporting group"):
        rg_delete = st.selectbox(
            label = 'Delete rg',
            options = l_rep_group
        )
        rg_btn_delete = st.button(
            label="Delete"
        )
        if rg_btn_delete:
            df_sdtm = display_current(filename="df_sdtm.csv")
            df_sdtm = df_sdtm.drop(rg_delete, axis=1)
            df_adam = display_current(filename="df_adam.csv")
            df_adam = df_adam.drop(rg_delete, axis=1)
            df_tlg = display_current(filename="df_lopo.csv")
            df_tlg = df_tlg.drop(rg_delete, axis=1)
            save_changes(submit_changes = rg_btn_delete, filename = "df_sdtm.csv", df = df_sdtm)
            save_changes(submit_changes = rg_btn_delete, filename = "df_adam.csv", df = df_adam)
            save_changes(submit_changes = rg_btn_delete, filename = "df_lopo.csv", df = df_tlg)
    
# if "df_value_sdtm" not in st.session_state:
#     st.session_state.df_value_sdtm = df_sdtm
# if "df_value_adam" not in st.session_state:
#     st.session_state.df_value_adam = df_adam
# if "df_value_lopo" not in st.session_state:
#     st.session_state.df_value_lopo = df_lopo

def encapsule_logic_edited_workflow(filename: str, sheet: str):
    df_sdtm = display_current(filename=filename)
    st.title(f"Current LoPO")
    st.subheader(f"Sheet {sheet}")
    st.dataframe(df_sdtm)
    st.title(f"Edition Mode")
    st.subheader(f"Sheet {sheet}")
    edited_df_sdtm = st.data_editor(
        df_sdtm,
        column_config={
            "program_ext": st.column_config.SelectboxColumn(options=[".R",".sas"]),
            "qc_program_ext": st.column_config.SelectboxColumn(options=[".R",".sas"]),
        },
        num_rows="dynamic")
    submit_changes = st.button(
        label="Submit changes"
    )
    save_changes(submit_changes = submit_changes, filename = filename, df = edited_df_sdtm)

if sheet == "SDTM":
    encapsule_logic_edited_workflow(
        filename="df_sdtm.csv",
        sheet="SDTM"
    )

if sheet == "ADAM":
    encapsule_logic_edited_workflow(
        filename="df_adam.csv",
        sheet="ADAM"
    )

if sheet == "LOPO":
    encapsule_logic_edited_workflow(
        filename="df_lopo.csv",
        sheet="LOPO"
    )  






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