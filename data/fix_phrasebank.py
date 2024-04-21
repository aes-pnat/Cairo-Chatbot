import json
'''
Create a script which loads financial_phrasebank.json . 
That json is a list of objects which on the top level have the following keys: features, rows, num_rows_total, num_rows_per_page and partial. 
All keys are the same across all objects in the list, except "rows", which need to be concatenated across the 
'''
# Path to the JSON file
json_file = '/home/apasalic/workspace/ChatOne/data/financial_phrasebank.json'

# Load the JSON file
with open(json_file, 'r') as f:
    data = json.load(f)

# Concatenate the values of the 'rows' key
concatenated_rows = []
for obj in data:
    concatenated_rows.extend(obj['rows'])

# Print the concatenated rows
new_json = {
    'features': data[0]['features'],
    'rows': concatenated_rows,
    'num_rows_total': data[0]['num_rows_total'],
    'num_rows_per_page': data[0]['num_rows_per_page'],
    'partial': data[0]['partial']
}

# Save the new JSON file
new_json_file = '/home/apasalic/workspace/ChatOne/data/new_financial_phrasebank.json'
with open(new_json_file, 'w') as f:
    json.dump(new_json, f)