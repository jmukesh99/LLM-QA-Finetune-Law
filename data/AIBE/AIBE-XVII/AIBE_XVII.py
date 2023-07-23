import json
import re

# Read the text file
with open("AIBE_XVII.txt", "r") as file:
    lines = file.readlines()

# Initialize the variables
json_data = []
current_question = ""
current_options = []

# Iterate over the lines and build the questions and options
for line in lines:
    # Clean the line
    line = line.split("http")[0].strip()  # Discard the text after "http"
    
    # Skip if line is empty
    if not line:
        continue
    
    # Check if the line starts with a number indicating a new question
    if line[0].isdigit():
        # If there was a previous question, add it to the json_data
        if current_question:
            json_data.append({"Question": current_question, "Option": current_options})
        
        # Start a new question
        current_question = line
        current_options = []
    # Check if the line starts with a letter indicating an option
    elif line[0] == "(" and line[2] == ")":
        current_options.append(line)

# Add the last question if it exists
if current_question:
    json_data.append({"Question": current_question, "Option": current_options})

# Save the list of dictionaries into a JSON file
with open("questions_AIBE_XVII.json", "w") as file:
    json.dump(json_data, file, indent=4)
