import streamlit as st
import pandas as pd
from detector_script import detect_outliers,   # adjust this if using a subfolder

def main():
    st.set_page_config(page_title="Anomaly Detection App", page_icon="🕵️‍♀️") #Web page title.
    st.title("CSV Anomaly Detector") 
    st.markdown("Upload your data and learn about the anomalies and their fixes.")

    #st.file_uploader allows file upload. But in the main script, you are asking for the name of the file.
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file:
        try:
            #Reading the file and displaying a preview.
            df = pd.read_csv(uploaded_file)
            st.subheader("Data Preview")
            st.dataframe(df.head())

            cleaned_df = clean_data(df)
            outliers_df = detect_outliers(cleaned_df)

            st.subheader("🧼 Cleaned Data (Post-Processing)")
            st.dataframe(cleaned_df)

            st.subheader("🚨 Detected Outliers")
            st.dataframe(outliers_df)

            st.success("✅ Anomaly detection completed!")

        #Informing the user. Handling numerical columns with letters.
'''
print("Letters including those in units can cause a model to crash. Please go through your data to see if there are any numerical columns that contain units or other letters.")
cleaning = input("Are there numerical columns with units and letters (Y/N)? ").upper()
if cleaning == "Y":
    clean_numerical_columns()

#Informing the user. Handling columns with missing values.
option = input("Do you have a particular way in which you would like the outliers to be detected?\na)IQR\nb)Z-score\nc)Isolation Forest\nd)Default\n")



#Informing the user. Handling columns with outliers.
option = input("Do you have a particular way in which you would like the outliers to be detected?\na)IQR\nb)Z-score\nc)Isolation Forest\nd)Default\n")

#Filtering the numerical columns.
numerical_columns = data.select_dtypes(include=['float64', 'int64'])

'''
        
        except Exception as e:
            st.error(f"❌ Oops! Something went wrong: {e}")
    else:
        st.info("📥 Please upload a CSV file to begin.")

if __name__ == "__main__":
    main()
