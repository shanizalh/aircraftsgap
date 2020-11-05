# Import necessary packages
import pandas as pd
import os
from datetime import date

# List of column headers
headers = ['Fleet', 'Floc', 'Message type (R/A/G)', 'Error number', 'Functional identifier (FID)', 'Message text', 'Material', 'Sequence']

# Create empty dataframe
combined = pd.DataFrame(columns=headers)

# List of files
directories = os.listdir()
files = [file for file in directories if '.XLS' in file]

# Append all files into dataframe
for f in files:
    data = pd.read_csv(f, sep='\t', skiprows=0)
    combined = combined.append(data, ignore_index=True)

# Remove duplicates and reset index
combined = combined.drop_duplicates()[1:].reset_index()
combined = combined.iloc[:,1:]

# Start row index from 1
combined.index = combined.index + 1
combined

# Convert generated dataframe to excel
today = date.today()
today_date = today.strftime('%Y%m%d')
filename = 'zrccm2_' + today_date + '.xlsx'
combined.to_excel(filename)