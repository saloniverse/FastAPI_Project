import pandas as pd

df = pd.read_excel('example_data.xlsx', engine='openpyxl')

print(df)

json_data = df.to_json(orient='records', indent=4)

with open('output_data.json', 'w') as json_file:
    json_file.write(json_data)

print("Excel data converted to JSON and saved as output_data.json")