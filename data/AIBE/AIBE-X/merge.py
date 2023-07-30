import json
import pandas as pd

# Load second file
with open('AIBE-X.json') as json_file1:
    data1 = json.load(json_file1)

# Load first file
with open('AIBE-X-GPT4-Ans.json') as json_file2:
    data2 = json.load(json_file2)

# Combine dictionaries from both files
combined_data = [dict(**d1, **d2) for d1, d2 in zip(data1, data2)]

# Save combined data to a new file
with open('AIBE-X-combined.json', 'w') as outfile:
    json.dump(combined_data, outfile, indent=4)

df = pd.read_json("AIBE-X-combined.json")
df.to_csv("AIBE-X.csv", index=False)