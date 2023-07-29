import json
import re

# Read the file
with open("answer.text", "r") as file:
    lines = file.readlines()

# Initialize variables
answer_key = None
explanation_key = None
output = []

# Loop through each line in the file
for line in lines:
    line = line.strip()  # remove leading and trailing whitespaces
    if not line:  # skip empty lines
        continue

    # Check if line starts with a), b), c), or d)
    if re.match(r"^[abcd]\)", line):
        # If the previous answer has an explanation, append it to the output
        if answer_key is not None and explanation_key is not None:
            output.append({ 'Answer': answer_key, 'Explanation': explanation_key })

        answer_key = line  # update the answer key
        explanation_key = None  # reset the explanation key

    else:
        # If explanation key is None, it means this is the first line of the explanation
        # If it's not None, then append this line to the previous lines
        explanation_key = line if explanation_key is None else explanation_key + " " + line

# Add the last question if it hasn't been added yet
if answer_key is not None and explanation_key is not None:
    output.append({ 'Answer': answer_key, 'Explanation': explanation_key })

# Convert the output to a JSON string with an indentation of 4
output_json = json.dumps(output, indent=4)

# Write the JSON string to a file
with open("answer.json", "w") as file:
    file.write(output_json)
