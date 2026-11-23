# Import the regular expression module for text cleaning.
import re


# Define a function to clean and normalize resume text.
def clean_resume_text(text):

    # Convert the complete text to lowercase for consistent comparison.
    text = text.lower()

    # Replace Windows-style line breaks with a single space.
    text = text.replace("\r\n", " ")

    # Replace remaining newline characters with a single space.
    text = text.replace("\n", " ")

    # Preserve important technical symbols while removing unnecessary characters.
    text = re.sub(r"[^a-z0-9+#.\-/ ]", " ", text)

    # Replace multiple consecutive spaces with a single space.
    text = re.sub(r"\s+", " ", text)

    # Remove unnecessary spaces from the beginning and end.
    text = text.strip()

    # Return the cleaned and normalized resume text.
    return text