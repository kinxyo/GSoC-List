import pandas as pd

file_paths = ['2023.json', '2022.json', '2021.json', '2020.json']
data_frames = [pd.read_json(file_path) for file_path in file_paths]

common_rows = []
for row in data_frames[0].values:  #Assuming the first DataFrame as a reference
    if all(row in df.values for df in data_frames):
        common_rows.append(row)

common_rows_df = pd.DataFrame(common_rows, columns=data_frames[0].columns) #Converting common rows to DataFrame for easier analysis/display

common_rows_df.to_excel('output.xlsx', index=False, engine='xlsxwriter')
print("Common Rows:")
print(common_rows_df)
