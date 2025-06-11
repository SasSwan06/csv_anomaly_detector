import streamlit as st
import pandas as pd
from detector_script import detect_outliers, clean_numerical_columns   # adjust this if using a subfolder

def main():
    st.set_page_config(page_title="Anomaly Detection App", page_icon="🕵️‍♀️") #Web page title.
    st.title("CSV Anomaly Detector") 
    st.markdown("Upload your data and learn about the anomalies and their fixes.")

    #st.file_uploader allows file upload. But in the main script, you are asking for the name of the file.
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        #Reading the file and displaying a preview.
        df = pd.read_csv(uploaded_file)
        st.subheader("Data Preview")
        st.dataframe(df.head())

            
        #outliers_df = detect_outliers(cleaned_df)
        st.subheader("Preparing Numerical Data")
        st.markdown("Numerical Data can sometimes come with letters which will cause problems in data processing later. Does your dataset have such columns?")

        if option1 == 'Yes':
            st.subheader("Select Columns to Clean")
            #Selecting the columns available in the df.
            available_columns = df.columns.tolist()
            selected_columns = st.multiselect("Select the numerical columns with messy text to clean:",options=available_columns)
    
        if selected_columns:
            for column in selected_columns:
                df = clean_numerical_columns(df, column)  # Make sure the function returns the modified df
                st.success("Columns cleaned successfully!")
            st.dataframe(df.head())
            
        st.subheader("🧼 Cleaned Data (Post-Processing)")
        #st.dataframe(cleaned_df)

        #st.subheader("🚨 Detected Outliers")
        #st.dataframe(outliers_df)

        st.success("✅ Anomaly detection completed!")
        
    else:
        st.info("📥 Please upload a CSV file to begin.")

if __name__ == "__main__":
    main()
