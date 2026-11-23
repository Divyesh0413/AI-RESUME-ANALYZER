# Import PdfReader to extract text from PDF files.
from pypdf import PdfReader

# Import Document to extract text from DOCX files.
from docx import Document


# Define a function to extract text from a PDF resume.
def extract_text_from_pdf(file):

    # Create a PDF reader object using the uploaded file.
    reader = PdfReader(file)

    # Create an empty string to store the extracted text.
    text = ""

    # Loop through every page of the PDF.
    for page in reader.pages:

        # Extract text from the current page.
        page_text = page.extract_text()

        # Add the extracted page text to the complete text.
        if page_text:
            text += page_text + "\n"

    # Return the complete extracted resume text.
    return text


# Define a function to extract text from a DOCX resume.
def extract_text_from_docx(file):

    # Open the uploaded DOCX file as a Word document.
    document = Document(file)

    # Create an empty string to store the extracted text.
    text = ""

    # Loop through every paragraph in the document.
    for paragraph in document.paragraphs:

        # Get the text from the current paragraph.
        paragraph_text = paragraph.text

        # Add non-empty paragraphs to the complete text.
        if paragraph_text.strip():
            text += paragraph_text + "\n"

    # Return the complete extracted resume text.
    return text


# Define a general function that detects the file type automatically.
def extract_resume_text(file):

    # Get the uploaded file name.
    filename = file.name.lower()

    # Check whether the uploaded file is a PDF.
    if filename.endswith(".pdf"):

        # Extract and return text from the PDF file.
        return extract_text_from_pdf(file)

    # Check whether the uploaded file is a DOCX file.
    elif filename.endswith(".docx"):

        # Extract and return text from the DOCX file.
        return extract_text_from_docx(file)

    # Handle unsupported file types.
    else:

        # Raise an error if the file is neither PDF nor DOCX.
        raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")