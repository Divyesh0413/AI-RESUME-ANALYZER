# Import the built-in csv module to read the skill dictionary file.
import csv

# Import the regular expression module for accurate skill matching.
import re


# Define a function to load skills from the CSV file.
def load_skill_dictionary(file_path="data/skill_dictionary.csv"):

    # Create an empty list to store the skill dictionary.
    skill_data = []

    # Open the CSV file using UTF-8 encoding.
    with open(file_path, "r", encoding="utf-8") as file:

        # Read each row of the CSV file as a dictionary.
        reader = csv.DictReader(file)

        # Loop through every row in the CSV file.
        for row in reader:

            # Add the current row to the skill dictionary.
            skill_data.append(row)

    # Return the complete skill dictionary.
    return skill_data


# Define a function to extract skills from resume text.
def extract_skills(text, skill_data):

    # Convert the resume text to lowercase for consistent matching.
    text = text.lower()

    # Create an empty list to store detected skills.
    extracted_skills = []

    # Loop through every skill in the skill dictionary.
    for row in skill_data:

        # Get the skill name from the current row.
        skill = row["skill"]

        # Convert the skill name to lowercase.
        skill_lower = skill.lower()

        # Escape special characters so the skill can be safely used in regex.
        escaped_skill = re.escape(skill_lower)

        # Create a pattern that matches the complete skill.
        pattern = r"(?<!\w)" + escaped_skill + r"(?!\w)"

        # Search for the skill inside the resume text.
        if re.search(pattern, text):

            # Add the original skill name to the extracted skills list.
            extracted_skills.append(skill)

    # Remove duplicate skills while preserving their order.
    extracted_skills = list(dict.fromkeys(extracted_skills))

    # Return the detected skills.
    return extracted_skills


# Define a function to group extracted skills by category.
def categorize_skills(extracted_skills, skill_data):

    # Create an empty dictionary to store categorized skills.
    categorized_skills = {}

    # Loop through every extracted skill.
    for skill in extracted_skills:

        # Loop through every row in the skill dictionary.
        for row in skill_data:

            # Check whether the current row contains the extracted skill.
            if row["skill"].lower() == skill.lower():

                # Get the category of the current skill.
                category = row["category"]

                # Create the category if it does not already exist.
                if category not in categorized_skills:
                    categorized_skills[category] = []

                # Add the skill to its category.
                categorized_skills[category].append(skill)

                # Stop searching once the matching skill is found.
                break

    # Return the categorized skills.
    return categorized_skills