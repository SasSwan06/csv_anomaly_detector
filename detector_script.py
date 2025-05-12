'''
This is an csv data anomaly detector. The user can upload their data and get the anomalies listed to them.
'''
import pandas as pd
import sklearn
#import matplotlib.pyplot as plt 
#import seaborn as sns

#Allowing user to upload their csv file.
file_name = input("Please enter the name of the csv file: ")
data = pd.read_csv(file_name)
print(data.head())
OUTLIER_WARNING_NOTICE = "Please be sure that you would like to delete the outliers as some outliers can present important insights."
option = input("Do you have a particular way in which you would like the outliers to be detected?\na)IQR\nb)Z-score\nc)Isolation Forest\nd)Default\n")

#Importing  winsorize.
from scipy.stats.mstats import winsorize

#Making the skew_threshold and winsorize_limit the parameters to avoid hardcoding. The parameters are also set to default values.
def handle_outliers(df, column, skew_threshold=0.5, winsorize_limit=0.05):
    """
    Handles outliers in a pandas column by winsorizing based on skew.
    
    Parameters:
    - column: pandas Series, numerical column.
    - skew_threshold: float, minimum skew required to proceed with winsorizing.
    - winsorize_limit: float, proportion that will be winsorized from the column.
    
    Returns:
    - winsorized column
    """
    skewness = column.skew()
    print(f"Skewness of {column.name}: {skewness:.2f}")

    # If skew is less than the skew threshold, dont do anything.
    if abs(skewness) < skew_threshold:
        print("Skew not significant, no winsorization applied.")
        return column
    '''
    # Determine winsorization limits
    if skewness > 0:
        limits = (0, winsorize_limit)  # Trim upper outliers
    else:
        limits = (winsorize_limit, 0)  # Trim lower outliers
    '''
    #Initially, tried dealing with positive and negative skew separately, but for this dataset, using symmetric winsorization proved more helpful.
    limits = (winsorize_limit, winsorize_limit)
    # Apply winsorization (need to dropna first, then reinsert)
    limits = (winsorize_limit, winsorize_limit)
    winsorized_data = winsorize(column.dropna(), limits=limits)
    df.loc[df[column.name].notna(), column.name] = winsorized_data

    print(f"Winsorization applied with limits: {limits}")
    return column

#Filtering the numerical columns.
numerical_columns = data.select_dtypes(include=['float64', 'int64'])

'''
for col in numerical_columns.columns:
    data[col] = handle_outliers(data, data[col], skew_threshold = 0.2)

#print(data.head())
'''
##Currently all functions employ the IQR method to detect outliers
#Function to determine outliers.
def count_outliers(df):
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


def detect_outliers(df, column):
    '''
    Purpose of this function is to go through a specific column of the data and return the flagged outliers.
    '''
    column_outlier_count = 0 
    skew_level = ""
    q1 = column.quantile(0.25)
    q3 = column.quantile(0.75)
    iqr = q3 - q1
    iqr_lower = q1 - (1.5 * iqr)
    iqr_upper = q3 + (1.5 * iqr)

    for value in column:
        if (value < iqr_lower) or (value > iqr_upper):
            column_outlier_count += 1

    if column.skew() >= 1:
        skew_level == "high"
    elif column.skew() >= 0.5 and column.skew() < 1:
        skew_level = "moderate"
    elif column.skew() < 0.5:
        skew_level = "low"
    print(f"Column: {column.name}")
    print(f"Detected {column_outlier_count} outliers.")  
    print(f"Skew: {column.skew()}") #REDUNDANT!!
    print(f"Severity of skew: {skew_level}") 
    #Maybe make a separate function calling the relevant suggested action course.
    print(f"Suggested Action:")              

#Really wanna convert this to a method, but will do that later. VISION: column.outliersToCsv()
def outliers_to_csv():
    return
    
detect_outliers(data, data["Kilometers_Driven"])




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

#Flag outliers, save them to a dataframe, check if the dataframe is empty, then convert the dataframe to a csv