import os
import pandas as pd

# Load the Excel file
file_path = r'C:Insert your file path here'
xl = pd.ExcelFile(file_path)

# Loop through all sheets
dfs = []
for sheet_name in xl.sheet_names:
    # Read the sheet into a dataframe
    df = xl.parse(sheet_name)
    # Collapse the first 10 columns of rows 1-5 into a single string
    details = ' '.join(df.iloc[0:5, 0:10].astype(str).values.flatten().tolist())
    # Create a new dataframe with the sheet name and details
    new_df = pd.DataFrame({'Store Number': sheet_name, 'Details': details}, index=[0])
    # Append the new dataframe to the list of dataframes
    dfs.append(new_df)

# Concatenate all dataframes into a single dataframe
result_df = pd.concat(dfs)
#print (result_df)
result_df.to_csv(r'C:Insert your file path here\output.csv', index=False)