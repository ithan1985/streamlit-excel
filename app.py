import io
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Excel Explorer Pro", layout="wide")

st.title("Excel Explorer Pro")

archivo = st.file_uploader("Sube un Excel", type=["xlsx","xls","xlsm","xlsb","ods"])

if archivo:
    df = pd.read_excel(archivo)
    st.dataframe(df)
