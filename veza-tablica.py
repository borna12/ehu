import pandas as pd



# Read the two Excel files
file1 = pd.read_csv('EHU.csv')
file2 = pd.read_csv('ehu-veze.csv')

# Merge the two files on the ID column
merged_files = pd.merge(file1, file2, on='ID', how='outer', suffixes=('_file1', '_file2'))

##brisanje nepotrebnih stupaca
merged_files=merged_files.drop(['Stranica', 'str. priloga',"Svezak"], axis=1)


# Create a new column "Match" and set the value to "good" if the ID is present in both files

# Write the merged file with the "Match" column to a new Excel file
merged_files.to_csv('ehu-povezan.csv', index=False)