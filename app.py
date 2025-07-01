import streamlit as st
import pandas as pd
from enhancer import enhance_csv

st.title("Lead Insight Enhancer 🔍")
uploaded = st.file_uploader("Upload SaaSquatch CSV", type="csv")

if uploaded:
    with open("input.csv", "wb") as f:
        f.write(uploaded.read())
    st.info("Processing CSV...")
    enhance_csv("input.csv")
    st.success("Done! Download below:")
    with open("enhanced_leads.csv", "rb") as f:
        st.download_button("Download Enhanced CSV", f, file_name="enhanced_leads.csv")
