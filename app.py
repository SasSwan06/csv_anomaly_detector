import streamlit as st
import pandas as pd
from detector_script import detect_outliers, clean_numerical_columns, detect_duplicates, handle_duplicates_drop, detect_missing_values, handle_missing_values_drop, handle_missing_values_imputation, handle_missing_values_constant, handle_missing_values_ml, handle_missing_values_interpolation   # adjust this if using a subfolder

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
        
        st.subheader("Preparing Numerical Data")
        option1 = st.radio("Does your dataset have numerical columns with unwanted letters or characters?", ('Yes', 'No'))

        if option1 == 'Yes':
            st.subheader("Select Columns to Clean")
            #Selecting the columns available in the df.
            available_columns = df.columns.tolist()
            selected_columns = st.multiselect("Select the numerical columns with messy text to clean:",options=available_columns)
        ##### I dont like this condition.
        if selected_columns:
            for column in selected_columns:
                df = clean_numerical_columns(df, column)
                st.success("Columns cleaned successfully!")
            st.markdown("Dataset Preview")
            st.dataframe(df.head())

    ######################################### DEALING WITH DUPLICATES #####################################################
        st.subheader("Dealing With Duplicates")
        DUPLICATES_NOTE = "Duplicates are harmful."
        st.markdown(DUPLICATES_NOTE)
        st.text("Status of duplicates in your dataset: ")
        detect_duplicates(df)

        option2 = st.radio("Would you like to proceed with dropping the duplicates in your dataset? ", ('Yes', 'No'))

        if option2 == "Yes":
            handle_duplicates_drop(df)
            st.success("Duplicates dropped successfully!")
            st.markdown("Dataset Preview")
            st.dataframe(df.head())
        
    ######################################### DEALING WITH MISSING VALUES #############################################
        st.subheader("Dealing With Missing Values")
        MISSING_VALUES_NOTE = "Missing Values are dangerous, bud!"
        st.markdown(MISSING_VALUES_NOTE)
        st.text("Missing values in your dataset: ")
        detect_missing_values(df)

        option3 = st.radio("How would you like to deal with your missing values?", ('Dropping Missing Values', 'Impute with a descriptive statistic', 'Impute with a constant', 'Use Interpolation'))
        if option3 == 'Dropping Missing Values':
            st.text("Brief description of the pros and cons of dropping columns with missing values.")
            #Double user validation
            choice = st.radio("Do you wish to proceed with dropping the columns with missing values?", ('Yes', 'No'))

            if choice == "Yes":
                handle_missing_values_drop(df)
                st.success("Missing values dropped successfully!")
                st.markdown("Dataset Preview")
                st.dataframe(df.head())

        if option3 == 'Impute with a descriptive statistic':
            st.text("Brief description of the pros and cons of using this imputation.")
            handle_missing_values_imputation(df)
            st.success("Missing values imputed successfully!")
            st.dataframe(df.head())
        
        if option3 == 'Impute with a constant':
            st.text("Brief description")
            handle_missing_values_constant(df)
            st.success("Missing values imputed successfully!")
            st.dataframe(df.head())
        
        if option3 == 'Use Interpolation':
            st.text("Brief description")
            handle_missing_values_interpolation(df)
            st.success("Columns cleaned successfully!")
            st.dataframe(df.head())

    ########################################### DEALING WITH OUTLIERS ##############################################


        st.subheader("🧼 Cleaned Data (Post-Processing)")
        #st.dataframe(cleaned_df)

        #st.subheader("🚨 Detected Outliers")
        #st.dataframe(outliers_df)

        st.success("✅ Anomaly detection completed!")
        
    else:
        st.info("📥 Please upload a CSV file to begin.")

if __name__ == "__main__":
    main()
