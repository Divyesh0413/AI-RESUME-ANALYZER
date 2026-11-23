# Import the built-in csv module to read job role data.
import csv


# Define a function to load job roles from the CSV file.
def load_job_roles(file_path="data/job_roles.csv"):

    # Create an empty list to store all job roles.
    job_roles = []

    # Open the CSV file using UTF-8 encoding.
    with open(file_path, "r", encoding="utf-8") as file:

        # Read each CSV row as a dictionary.
        reader = csv.DictReader(file)

        # Loop through every job role in the CSV file.
        for row in reader:

            # Get the required skills from the current job role.
            skills = row["required_skills"].split(",")

            # Remove unnecessary spaces from every skill.
            skills = [skill.strip() for skill in skills]

            # Create a dictionary containing the role and its skills.
            job_role = {
                "role": row["role"],
                "required_skills": skills
            }

            # Add the job role to the list.
            job_roles.append(job_role)

    # Return all loaded job roles.
    return job_roles


# Define a function to calculate the match score for one job role.
def calculate_match_score(resume_skills, required_skills):

    # Convert resume skills to lowercase for consistent comparison.
    resume_skills_lower = {
        skill.lower() for skill in resume_skills
    }

    # Convert required skills to lowercase for consistent comparison.
    required_skills_lower = {
        skill.lower() for skill in required_skills
    }

    # Find the skills that exist in both the resume and job requirements.
    matched_skills = resume_skills_lower.intersection(
        required_skills_lower
    )

    # Calculate the total number of required skills.
    total_required_skills = len(required_skills_lower)

    # Handle the case where a job has no required skills.
    if total_required_skills == 0:
        return 0.0, []

    # Calculate the percentage of required skills found in the resume.
    score = (
        len(matched_skills) / total_required_skills
    ) * 100

    # Find the required skills that are missing from the resume.
    missing_skills = required_skills_lower - resume_skills_lower

    # Return the score and missing skills.
    return round(score, 2), sorted(missing_skills)


# Define a function to compare a resume with all available job roles.
def match_resume_to_jobs(resume_skills, job_roles):

    # Create an empty list to store matching results.
    results = []

    # Loop through every available job role.
    for job in job_roles:

        # Calculate the match score and missing skills.
        score, missing_skills = calculate_match_score(
            resume_skills,
            job["required_skills"]
        )

        # Create a result dictionary for the current job role.
        result = {
            "role": job["role"],
            "match_score": score,
            "missing_skills": missing_skills
        }

        # Add the result to the results list.
        results.append(result)

    # Sort the results from highest score to lowest score.
    results.sort(
        key=lambda result: result["match_score"],
        reverse=True
    )

    # Return the sorted matching results.
    return results