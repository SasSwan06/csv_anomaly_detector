'''
This is an csv data anomaly detector. The user can upload their data and get the anomalies listed to them.
'''
import pandas as pd
import sklearn
import matplotlib.pyplot as plt 
import seaborn as sns

#Allowing user to upload their csv file.
#Later on, make this an input?
file_name = input("Please enter the name of the csv file: ")
data = pd.read_csv(file_name)
print(data.head())

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

numerical_columns = data.select_dtypes(include=['float64', 'int64'])

for col in numerical_columns.columns:
    data[col] = handle_outliers(data, data[col], skew_threshold = 0.2)

#print(data.head())

#Function to determine outliers.
def detect_outliers(df):
    '''
    Currently the function takes the dataset and flags outliers using the IQR method.
    Outliers are values in a dataset that lie 1.5 IQR below the 1st quartile or 1.5 IQR above the third quartile.
    '''
    numerical_columns = data.select_dtypes(include=['float64', 'int64'])
    for column in numerical_columns.columns:
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

detect_outliers(data)


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