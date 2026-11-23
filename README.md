# AI Resume Analyzer & Job Recommendation System

An NLP-based Streamlit application that analyzes a student's resume, extracts technical skills, compares them with different job roles, identifies missing skills, and generates a learning roadmap.

---

## Project Overview

The **AI Resume Analyzer & Job Recommendation System** is designed to help students understand how well their resume matches different technical job roles.

The application analyzes an uploaded resume and provides:

- Resume text extraction
- Resume text cleaning and normalization
- Technical skill extraction
- Skill categorization
- Job role matching
- Resume-to-job match scores
- Missing skill identification
- Learning roadmap recommendations
- Interactive Streamlit dashboard

> **Note:** This application is designed for educational and career-guidance purposes. It is not an automated hiring or rejection system.

---

**LIVE LINK:-** https://ai-resume-analyzer-yzzzecagxyrj8hy3cst5hu.streamlit.app/

## Project Objective

The main objective of this project is to build an NLP-based application that can analyze resumes and compare their technical skills with predefined job-role requirements.

The system helps users:

1. Understand the technical skills present in their resume.
2. Identify suitable job roles based on detected skills.
3. Understand which skills are missing for a particular role.
4. Get a structured learning roadmap for missing skills.

---

## Key Features

### 1. Resume Upload

Users can upload their resume in:

- PDF format
- DOCX format

The application validates the uploaded file and processes the supported document formats.

---

### 2. Resume Text Extraction

The system extracts text from uploaded resumes using:

- `pypdf` for PDF files
- `python-docx` for DOCX files

The extracted text is then passed to the text-cleaning module.

---

### 3. Text Cleaning and Normalization

The extracted resume text is cleaned and normalized before skill extraction.

The cleaning process includes:

- Converting text to lowercase
- Removing unnecessary characters
- Normalizing spaces
- Preserving important technical symbols
- Removing unnecessary whitespace

This makes skill matching more consistent.

---

### 4. Technical Skill Extraction

The application uses a controlled skill dictionary to identify technical skills mentioned in the resume.

The skills are organized into categories such as:

- Programming
- Machine Learning
- NLP
- Database
- Tools
- Cloud

The extracted skills are displayed in the Streamlit dashboard.

---

### 5. Skill Categorization

Detected skills are grouped into meaningful categories.

For example:

```text
Programming
    Python

Machine Learning
    Machine Learning
    Scikit-learn
    TensorFlow

NLP
    NLP

Tools
    Streamlit
    Git
    GitHub

This helps users understand their technical skill profile.

6. Job Role Matching

The extracted resume skills are compared with predefined requirements for different technical job roles.

The current system analyzes roles such as:

Machine Learning Engineer
AI/ML Engineer
Data Scientist
NLP Engineer
Backend Developer

Each role receives a skill-based match score.

7. Match Score Calculation

The current implementation uses skill overlap between the resume and the job requirements.

The basic calculation is:

Number of Matching Skills
------------------------- × 100
Total Required Skills

For example, if a job role requires 7 skills and the resume contains 5 of them:

5 / 7 × 100 = 71.43%

The resulting percentage represents the proportion of required skills detected in the resume.

8. Top Job Role Recommendations

After analyzing the resume, the application displays the top job-role matches based on the calculated skill match scores.

The dashboard provides:

Job role name
Match percentage
Missing skills

The application also displays an interactive comparison chart.

9. Skill Gap Analysis

For each job role, the system identifies skills that are required by the role but were not detected in the resume.

Example:

Role: Machine Learning Engineer

Missing Skills:
- Docker
- PyTorch

This helps users understand which technical areas they can work on.

10. Learning Roadmap

The application generates a rule-based learning roadmap for missing skills.

Each roadmap provides:

Skill name
Recommended learning level
Topics to study

Example:

Skill: Docker

Level: Beginner

Topics:
- Docker basics
- Images and containers
- Dockerfile
- Docker Compose
11. Interactive Streamlit Dashboard

The application provides an interactive dashboard containing:

Resume upload section
Extracted skills
Skill categories
Number of detected skills
Number of analyzed job roles
Highest match score
Top 3 job-role matches
Interactive job-role comparison chart
Detailed job-role analysis
Missing skills
Learning roadmap
Reset option
Project Workflow
                    Resume Upload
                         |
                         v
                PDF / DOCX Extraction
                         |
                         v
              Text Cleaning & Normalization
                         |
                         v
                Technical Skill Extraction
                         |
                         v
                  Skill Categorization
                         |
                         v
                  Job Role Comparison
                         |
                         v
                  Match Score Calculation
                         |
                         v
                Missing Skill Identification
                         |
                         v
                   Learning Roadmap
                         |
                         v
                  Streamlit Dashboard
Project Architecture
User
 |
 | Upload Resume
 v
app.py
 |
 +----------------------+
 |                      |
 v                      v
resume_parser.py    text_cleaner.py
 |                      |
 |                      |
 +----------+-----------+
            |
            v
    skill_extractor.py
            |
            v
      job_matcher.py
            |
            v
   roadmap_generator.py
            |
            v
     Streamlit Dashboard
Project Structure
AI-RESUME-ANALYZER/
│
├── app.py
├── resume_parser.py
├── text_cleaner.py
├── skill_extractor.py
├── job_matcher.py
├── roadmap_generator.py
│
├── data/
│   ├── job_roles.csv
│   └── skill_dictionary.csv
│
├── sample_resumes/
│
├── reports/
│
├── tests/
│   └── test_cases.csv
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
Module Description
app.py

Main Streamlit application.

Responsibilities:

User interface
Resume upload
Resume analysis
Displaying extracted skills
Displaying job matches
Displaying charts
Displaying missing skills
Displaying learning roadmap
resume_parser.py

Responsible for extracting text from:

PDF files
DOCX files

It automatically detects the uploaded file type and uses the appropriate extraction method.

text_cleaner.py

Responsible for cleaning and normalizing extracted resume text.

It prepares resume text for consistent skill matching.

skill_extractor.py

Responsible for:

Loading the skill dictionary
Detecting skills in resume text
Categorizing detected skills
job_matcher.py

Responsible for:

Loading predefined job roles
Comparing resume skills with job requirements
Calculating match scores
Identifying missing skills
roadmap_generator.py

Responsible for generating learning roadmaps for missing skills using predefined learning topics.

Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Web application and dashboard
pypdf	PDF text extraction
python-docx	DOCX text extraction
Regular Expressions	Text cleaning
Pandas	Data handling
NumPy	Numerical operations
Scikit-learn	Machine learning utilities
Plotly	Interactive visualization
Python Libraries

The project uses the following main Python packages:

streamlit
pypdf
python-docx
pandas
numpy
scikit-learn
plotly

All required dependencies are listed in:

requirements.txt
Installation
Step 1: Clone the Repository
git clone <your-github-repository-url>
Step 2: Open the Project Folder
cd AI-RESUME-ANALYZER
Step 3: Install Required Libraries
python -m pip install -r requirements.txt
Step 4: Run the Application
streamlit run app.py

The Streamlit application will open in the browser.

How to Use
Step 1

Open the Streamlit application.

Step 2

Upload a resume in:

PDF

or

DOCX

format.

Step 3

Click:

Analyze Resume
Step 4

Review the detected technical skills.

Step 5

Check the skill categories.

Step 6

Review the job-role match scores.

Step 7

Check the missing skills for each role.

Step 8

Open the learning roadmap to see recommended topics.

Step 9

Use the reset button to analyze another resume.

Example Output

A sample resume can produce results such as:

Detected Skills:

Python
Machine Learning
Scikit-learn
TensorFlow
NLP
Streamlit
Git
GitHub

Example job-role analysis:

Role: Machine Learning Engineer

Match Score: 71.43%

Missing Skills:
- Docker
- PyTorch

Another example:

Role: Data Scientist

Match Score: 42.86%

Missing Skills:
- Matplotlib
- NumPy
- Pandas
- SQL

The actual results depend on the uploaded resume.

Learning Roadmap Example

For a missing skill such as Docker:

Skill: Docker

Level: Beginner

Topics:

- Docker basics
- Images and containers
- Dockerfile
- Docker Compose

For SQL:

Skill: SQL

Level: Beginner

Topics:

- SELECT queries
- WHERE and ORDER BY
- GROUP BY
- JOIN operations
- Subqueries
Current Matching Approach

The current version uses a controlled skill-overlap approach.

The system compares:

Resume Skills
      |
      v
Required Job Skills
      |
      v
Matching Skills
      |
      v
Match Score

The score represents how many required job skills were detected in the uploaded resume.

This approach is intentionally simple and transparent for the current project version.

Responsible AI

This project is intended for educational and career-guidance purposes.

The system:

Does not make hiring decisions.
Does not automatically reject candidates.
Does not evaluate protected personal attributes.
Focuses on job-related skills and qualifications.
Treats match scores as estimates.
Does not assume that a missing keyword means the applicant lacks the actual ability.
Should not be used as the sole basis for employment decisions.

A resume may contain a skill using different terminology, or a candidate may possess a skill without explicitly mentioning the keyword.

Limitations

The current version has several limitations:

Skill extraction depends on a predefined skill dictionary.
Keyword-based matching may miss skills expressed using different terminology.
Match scores are estimates.
The current roadmap is rule-based.
Scanned or image-based resumes may not extract correctly.
Resume formatting can affect text extraction.
The current system focuses primarily on technical skills.
Job-role requirements are based on predefined datasets.
Future Improvements

The project can be extended with:

Advanced NLP using spaCy
Sentence Transformer embeddings
Semantic similarity matching
Machine learning-based job-role classification
LLM-powered resume feedback
Better education extraction
Better experience extraction
More job roles
More technical skills
Database integration
FastAPI backend
Docker support
Cloud deployment
Resume improvement suggestions
Semantic skill matching
More advanced career recommendations
Testing

The individual modules were tested during development.

The testing process includes:

PDF/DOCX text extraction testing
Text cleaning testing
Skill extraction testing
Skill categorization testing
Job-role matching testing
Missing skill detection testing
Learning roadmap testing
Streamlit application testing

The application was also tested using a sample resume.

Sample Resume

Sample resumes can be placed inside:

sample_resumes/

Only sanitized or non-sensitive resumes should be included in a public GitHub repository.

Data Files
data/skill_dictionary.csv

Contains the controlled technical skill dictionary used by the skill extraction module.

data/job_roles.csv

Contains predefined job roles and their required technical skills.

Responsible Use of Resume Data

Resumes may contain personal and sensitive information.

Users should avoid uploading resumes containing unnecessary personal information when testing or sharing the project.

For public demonstrations, sanitized sample resumes should be used.

Do not commit private resumes or personal information to a public GitHub repository.

Project Outcome

The completed application provides an end-to-end workflow:

Resume
   ↓
Text Extraction
   ↓
Text Cleaning
   ↓
Skill Extraction
   ↓
Skill Categorization
   ↓
Job Role Matching
   ↓
Match Score
   ↓
Skill Gap Analysis
   ↓
Learning Roadmap
   ↓
Interactive Dashboard

The project demonstrates the practical use of:

Python
NLP
Text Processing
Skill Extraction
Data Handling
Rule-Based Recommendation
Similarity/Matching Concepts
Data Visualization
Streamlit


Author

Divyesh Tiwari

B.Tech — Artificial Intelligence & Data Science

Disclaimer

This project is developed for educational and career-guidance purposes.

The job-role match scores and learning recommendations are estimates generated from predefined skills and job-role requirements.

The results should not be considered professional recruitment, hiring, rejection, or employment decisions.




