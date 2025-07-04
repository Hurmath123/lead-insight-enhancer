# app.py

import streamlit as st
import pandas as pd
from enhancer import enhance_csv
import os

st.set_page_config(page_title="Lead Insight Enhancer", layout="centered")
st.title("🚀 Lead Insight Enhancer (Offline with Ollama)")

uploaded_file = st.file_uploader("Upload your leads CSV", type=["csv"])

if uploaded_file is not None:
    file_path = os.path.join("temp_input.csv")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Enhancing leads..."):
        df_result = enhance_csv(file_path)

    st.success("Done! Preview below:")
    st.dataframe(df_result)

    csv_download = df_result.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Enhanced CSV", csv_download, "enhanced_leads.csv", "text/csv")
