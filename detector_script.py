'''
This is an csv data anomaly detector. The user can upload their data and get the anomalies listed to them.
'''
#####Flag outliers, save them to a dataframe, check if the dataframe is empty, then convert the dataframe to a csv
#####Check if the column is passed as an appropriate argument. column, column name.
#####Is printing from a function good practice?
#####Breaking a line in python.
#####What is a good ratio to consider dropping?
#####Work on docstrings.
#####Is it better practice by convention to have a function return something always?
#####Special charecters to be cleaned from the string.
#####DUPLICATES

#Import statements. Absolutely important to execute in the beginning of every program.
import pandas as pd
#import sklearn
#import matplotlib.pyplot as plt 
#import seaborn as sns

#####Disclaimer statement constants.
DISCLAIMER = "This script only deals with anomalies including missing values, outliers and unscaled columns."
DROP_DISCLAIMER = "Dropping rows can be detrimental to the dataset. Only consider dropping if the number of rows with anomalies is insignificant or if dropping would cause no significant changes to the dataset."

#Allowing user to upload their csv file.
file_name = input("Please enter the name of the csv file: ")
data = pd.read_csv(file_name)

#Printing a preview of the dataset.
print(data.head())

################################## EXTRACTING LETTERS FROM NUMERICAL COLUMNS #######################################
def clean_numerical_columns(df):
    '''
    #DOCSTRING TO BE DONE
    '''
    #####It is not good practice to rely on user's input in this case, but i will go with this for the initial prototype.
    #####I need to find a better way to identify required columns.
    number = int(input("How many columns? "))
    for i in range (0, number):
        column = input("Please enter the names of the column: ")

        df[column] = df[column].str.replace(r'[a-z/A-Z]+', '', regex=True)
        df[column] = pd.to_numeric(df[column], errors='coerce')

######################################### DEALING WITH MISSING VALUES #############################################
def detect_missing_values(df):
    '''
    Flags columns with missing values.
    '''
    #Displaying the number of rows in the dataset.
    #Separate functionality?
    number_of_rows = df.shape[0]
    print(f"The total number of rows in your dataset is {number_of_rows}")
    #Traversing through the columns (names only) of the data frame.
    for column in df:
        #Calculating the number of missing values in the column.
        column_null_number = df[column].isnull().sum() 
        #Condition to confirm the presence of outliers.
        if column_null_number != 0:
            #Statement to flag the outliers in every column
            print(f"The column {column} has {column_null_number} missing values.")


def handle_missing_values_drop(df):
    '''
    Handles missing values by dropping rows with missing values.
    '''
    #Printing a disclaimer.
    print(DROP_DISCLAIMER)
    '''
    #Asking the user if they wish to proceed.
    choice = input("Are you sure you wish to proceed (Y/N)? ").upper()
    if choice == "N":
        return
    '''
    #After authentication, dropping rows.
    ######Something is missing.
    df.dropna(axis=0)
    return

def handle_missing_values_imputation(df):
    '''
    Handles missing values by imputing them with a statistical value.
    '''
    
    
    """
    Handles missing values in a DataFrame, specific to the data type.

    The missing values are handled in the following ways
    - If the column is categorical (dtype 'object' or 'category'), fills missing values with the mode.
    - If the column is numerical, fills missing values with the median.
    - Skips columns with no missing values.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame with possible missing values.
    
    Returns:
    pd.DataFrame: The DataFrame with missing values handled.
    """
    for col in df.columns:
        missing_count = df[col].isnull().sum()
        #Condition to check if the column has missing values.
        if missing_count > 0:
            #Conditions to check if the column is categorical or numerical.
            if (df[col].dtype == 'object' or df[col].dtype.name == 'category'):
                mode_value = df[col].mode().iloc[0]
                df[col] = df[col].fillna(mode_value)
                print(f"Filled {missing_count} missing values in '{col}' with mode: {mode_value}")

            #If not categorical, fill the column with the mean.
            #####Check for cases when imputing with the median would be better.
            else:
                    median_value = df[col].median() #Calculating the mean.
                    df[col] = df[col].fillna(median_value)
                    print(f"Filled {missing_count} missing values in '{col}' with median: {median_value}")
    return df

def handle_missing_values_constant(df, column, contant_string):
    '''
    Handles missing values by imputing them with a constant value of choice (contant_string)
    #####ONLY FOR CATEGORICAL VARIABLES. SET CHECK IN PLACE.
    '''
    if (df[column.name].dtype == 'object' or df[column.name].dtype.name == 'category'):
        df[column.name] = df[column.name].fillna(contant_string)
    else:
        print("The column you are trying to impute is not categorical.")
    return

def handle_missing_values_ml(df):
    '''
    Handles missing values by predicting the most likely value using a machine-learning model to predict the most
    likely next value. 
    - Resource-intensive
    - Will work only if there is enough non-missing data to train on.
    '''
    
    return

def handle_missing_values_interpolation(df):
    '''
    Handles missing values by backfill or forwardfill
    '''
    return

def missing_values_to_csv(df):
    '''
    Identifies anomalies and records them in a csv file.
    '''
    return

########################################### DEALING WITH OUTLIERS ##############################################
##Currently all functions employ the IQR method to detect outliers
#Function to determine outliers.
def detect_outliers(df):
    '''
    Currently the function takes the dataset and flags outliers using the IQR method.
    Outliers are values in a dataset that lie 1.5 IQR below the 1st quartile or 1.5 IQR above the third quartile.
    '''

    numerical_columns = data.select_dtypes(include=['float64', 'int64'])
    for column in numerical_columns.columns:
        #Counter keeps track of the number of outliers in a column.
        column_outlier_count = 0 
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        iqr_lower = q1 - (1.5 * iqr)
        iqr_upper = q3 + (1.5 * iqr)
        for value in df[column]:
            if (value < iqr_lower) or (value > iqr_upper):
                column_outlier_count += 1
                #Later, add a functionality to note the line of the csv into a separate file.
        
        if column_outlier_count > 0:
            print(f"The column {df[column].name} has {column_outlier_count} outliers.")
            #Later, find and add skew to provide more information.


#Making the skew_threshold and winsorize_limit the parameters to avoid hardcoding. The parameters are also set to default values.
def handle_outliers_winsorize(df, column, skew_threshold=0.5, winsorize_limit=0.05):
    """
    Handles outliers in a pandas column by winsorizing based on skew.
    
    Parameters:
    - column: pandas Series, numerical column.
    - skew_threshold: float, minimum skew required to proceed with winsorizing.
    - winsorize_limit: float, proportion that will be winsorized from the column.
    
    Returns:
    - winsorized column
    """
    #Importing  winsorize.
    from scipy.stats.mstats import winsorize

    skewness = column.skew()
    print(f"Skewness of {column.name}: {skewness:.2f}")

    # If skew is less than the skew threshold, dont do anything and exit the function.
    if abs(skewness) < skew_threshold:
        print("Skew not significant, no winsorization applied.")
        return column
    '''
    #Asymmetric winsorization.
    # Determine winsorization limits
    if skewness > 0:
        limits = (0, winsorize_limit)  # Trim upper outliers
    else:
        limits = (winsorize_limit, 0)  # Trim lower outliers
    '''
    #####Using symmetric winsorization.
    limits = (winsorize_limit, winsorize_limit)
    # Apply winsorization (need to dropna first, then reinsert)
    winsorized_data = winsorize(column.dropna(), limits=limits)
    df.loc[df[column.name].notna(), column.name] = winsorized_data

    print(f"Winsorization applied with limits: {limits}")
    return column

def handle_outliers_drop(df):
    '''
    Handles outliers by dropping rows containing outliers.
    '''
    #Printing a disclaimer.
    print(DROP_DISCLAIMER)
    '''
    #Asking the user if they wish to proceed.
    choice = input("Are you sure you wish to proceed (Y/N)? ").upper()
    if choice == "N":
        return
    '''
    #After authentication, dropping rows.
    ######Something is missing.
    df.dropna(axis=0)
    return       

#Really wanna convert this to a method, but will do that later. VISION: column.outliersToCsv()
def outliers_to_csv():
    return

'''
for col in numerical_columns.columns:
    data[col] = handle_outliers(data, data[col], skew_threshold = 0.2)

#print(data.head())
'''

########################################### DEALING WITH RESCALING ##############################################
def detect_rescaling(df, column):
    '''
    Flags columns requiring normalisation
    '''
    return

#HANDLING RESCALING.
def handle_rescaling(df, column):
    '''
    Handles rescaling by min-max normalization.
    '''
    return


######################################## END OF ANOMALY HANDLING FUNCTIONS #####################################
#Informing the user. Handling numerical columns with letters.
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
#Collecting outliers in a dataframe.
all_outliers = pd.DataFrame()

#For numerical columns.
for column_name in df.select_dtypes(include=['float64', 'int64']).columns:

    if column_outlier_count > 0:
        outliers = df.loc[outlier_indices].copy()
        outliers['outlier_column'] = column_name
        all_outliers = pd.concat([all_outliers, outliers])

# Save if any outliers found
if not all_outliers.empty:
    all_outliers.to_csv("flagged_outliers.csv")
    print("\nAll outliers saved to 'flagged_outliers.csv'")
'''

"""
TEST CODE
Run a machine learning algorithm to check accuracy.
##TEST STATEMENT. detect_outliers(data, data["Kilometers_Driven"])
"""
