import streamlit as st
import pandas as pd
from detector_script import detect_outliers, clean_data  # adjust this if using a subfolder

def main():
    st.set_page_config(page_title="Anomaly Detection App", page_icon="🕵️‍♀️")
    st.title("🕵️‍♀️ Anomaly Detection in CSV Data")
    st.markdown("Upload a `.csv` file, and we'll sniff out the shady data points for you. 🔍")

    uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.subheader("📊 Preview: Uploaded Data")
            st.dataframe(df.head())

            cleaned_df = clean_data(df)
            outliers_df = detect_outliers(cleaned_df)

            st.subheader("🧼 Cleaned Data (Post-Processing)")
            st.dataframe(cleaned_df)

            st.subheader("🚨 Detected Outliers")
            st.dataframe(outliers_df)

            st.success("✅ Anomaly detection completed!")
        
        except Exception as e:
            st.error(f"❌ Oops! Something went wrong: {e}")
    else:
        st.info("📥 Please upload a CSV file to begin.")

if __name__ == "__main__":
    main()
