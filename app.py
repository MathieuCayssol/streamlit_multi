import streamlit as st
import pandas as pd
from io_data import read_json
from pathlib import Path

st.set_page_config(
    page_title="LoPO",
    page_icon="🗒️",
    layout="wide"
)


L_EXAMPLES_STUDY = ["BP12345", "BP5555", "BP8775"]
FIELDS = read_json(Path("data_structure.json"))

with st.sidebar:
    option = st.selectbox(
        'Select your study',
        L_EXAMPLES_STUDY
    )

st.subheader('Welcome on the study "{}"'.format(option))



sheet = st.radio(
        "Select the sheet you want to update 👇",
        ["SDTM", "ADAM", "LOPO"]
)

df_sdtm = pd.DataFrame(columns = FIELDS["sdtm"], data = [['Yes', 'make_sdtm', '.R', 'qc_dm', '.R', 'Demographics', 'DM', '.parquet', '', '', True, False, '', '', '']])

df_adam = pd.DataFrame(columns = FIELDS["adam"], data=[['Yes', 'ad_adsl', '.R', 'qc_ad_adsl', '.R', 'Subject-Level Analysis Dataset', 'ADSL', '.parquet', 'ceececec', '', True, False, '', '', '']])

df_lopo = pd.DataFrame(columns = FIELDS["lopo"], data=[['Yes', 'Demography', 'DML01', 'l_dm', '.R', 'qc_l_dm', '.R', 'T1 | T2\n\nT3', 'Footnotes 1 | Footnotes 2', '', 'l_dm_F1\nl_dm_F2_F3', '.pdf', 't_dm', '', True, True, '', '', '']])

# if "df_value_sdtm" not in st.session_state:
#     st.session_state.df_value_sdtm = df_sdtm
# if "df_value_adam" not in st.session_state:
#     st.session_state.df_value_adam = df_adam
# if "df_value_lopo" not in st.session_state:
#     st.session_state.df_value_lopo = df_lopo

if sheet == "SDTM":
    edited_df_sdtm = st.experimental_data_editor(df_sdtm, num_rows="dynamic")

if sheet == "ADAM":
    edited_df_adam = st.experimental_data_editor(df_adam, num_rows="dynamic")

if sheet == "LOPO":
    edited_df_lopo = st.experimental_data_editor(df_lopo, num_rows="dynamic")


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