import streamlit as st
import pandas as pd
from anomaly_detection import detect_outliers, clean_data

def main():
    st.title("🕵️‍♀️ Anomaly Detection App")
    uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("📊 Original Data", df)

        cleaned = clean_data(df)
        outliers = detect_outliers(cleaned)

        st.write("✨ Cleaned Data", cleaned)
        st.write("🚨 Outliers", outliers)

if __name__ == "__main__":
    main()
