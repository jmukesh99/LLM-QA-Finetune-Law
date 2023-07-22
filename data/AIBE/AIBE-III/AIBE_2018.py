import json

# Read the questions file
with open("aibe_2018.txt", "r") as file:
    lines = file.readlines()

# Initialize the variables
json_data = []
current_question = ""
current_options = []

# Iterate over the lines and build the questions and options
for line in lines:
    # Clean the line
    line = line.split("/")[0].strip()  # Discard the text after "/"

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
    elif line[0].isalpha() and line[1] == ")":
        current_options.append(line)

# Add the last question if it exists
if current_question:
    json_data.append({"Question": current_question, "Option": current_options})

# Convert the list of dictionaries into a JSON file with indentation
with open("questions_pretty.json", "w") as file:
    json.dump(json_data, file, indent=4)


# Read the answer key file
with open("aibe_2018_Answerkey.txt", "r") as file:
    answer_lines = file.readlines()

# Clean the answers, by removing the numbers and the newline characters
answers = [line.split(")")[0].strip()[-1] for line in answer_lines]

# Check that the number of questions matches the number of answers
assert len(json_data) == len(answers)

# Append the answers to the existing json_data
for question_dict, answer in zip(json_data, answers):
    question_dict["Answer"] = answer

# Save the updated json_data to a file
with open("questions_pretty_with_answers.json", "w") as file:
    json.dump(json_data, file, indent=4)
