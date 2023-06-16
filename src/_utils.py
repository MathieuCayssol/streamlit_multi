import os
import boto3
import streamlit as st

client = boto3.client('s3',
    aws_access_key_id = st.secrets["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key = st.secrets["AWS_SECRET_ACCESS_KEY"]
)

