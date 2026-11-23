# Import Streamlit for creating the web application.
import streamlit as st

# Import the resume text extraction function.
from resume_parser import extract_resume_text

# Import the resume text cleaning function.
from text_cleaner import clean_resume_text

# Import functions for skill extraction.
from skill_extractor import load_skill_dictionary
from skill_extractor import extract_skills
from skill_extractor import categorize_skills

# Import functions for job matching.
from job_matcher import load_job_roles
from job_matcher import match_resume_to_jobs

# Import the learning roadmap function.
from roadmap_generator import generate_roadmap

# Import the Supabase client helper.
from supabase_client import get_supabase_client

# Import the authentication page.
from auth import show_auth_page

# Import Pandas for displaying database records in a table.
import pandas as pd

# Import Plotly Express for creating interactive charts.
import plotly.express as px

# Configure the Streamlit page.
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Create a Supabase client for the current Streamlit browser session.
supabase = get_supabase_client()

# Check whether the current user is authenticated.
if not st.session_state.get("logged_in", False):

    # Display the login and signup interface for unauthenticated users.
    show_auth_page(supabase)

    # Stop the application until the user logs in.
    st.stop()

# Display the signed-in user's account controls in the sidebar.
with st.sidebar:

    # Show the authenticated user's email address when available.
    st.caption(f"Signed in as: {st.session_state.get('user_email', 'User')}")

    # Provide a logout button for the current user.
    if st.button("Log out", use_container_width=True):

        # Sign out from the Supabase authentication session.
        supabase.auth.sign_out()

        # Clear only authentication and analysis state for this browser session.
        for state_key in [
            "logged_in",
            "user_id",
            "user_email",
            "resume_skills",
            "categorized_skills",
            "job_results",
        ]:

            # Remove the selected session-state value when it exists.
            st.session_state.pop(state_key, None)

        # Refresh the application and return to the login page.
        st.rerun()


# Add custom CSS to improve the appearance of the application.
st.markdown(
    """
    <style>

    /* Remove unnecessary top padding from the main page. */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Style the main application title. */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.2rem;
    }

    /* Style the subtitle below the main title. */
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        opacity: 0.75;
        margin-bottom: 2rem;
    }

    /* Style information cards used throughout the application. */
    .info-card {
        padding: 1.2rem;
        border-radius: 15px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 1rem;
    }

    /* Style the disclaimer box. */
    .disclaimer {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 193, 7, 0.5);
        margin-top: 2rem;
    }
    /* Create equal-height cards for job recommendations. */
    .job-card {
        min-height: 210px;
        padding: 1.4rem;
        border-radius: 16px;
        border: 1px solid rgba(128, 128, 128, 0.30);
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    /* Style individual skill chips. */
    .skill-chip {
        display: inline-block;
        padding: 0.45rem 0.8rem;
        margin: 0.25rem;
        border-radius: 999px;
        border: 1px solid rgba(128, 128, 128, 0.30);
        font-size: 0.9rem;
        font-weight: 600;
    }

    /* Style the missing skill box. */
    .missing-box {
        padding: 0.8rem 1rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 80, 100, 0.35);
        margin: 0.8rem 0;
    }

    /* Style the roadmap skill heading. */
    .roadmap-skill {
        padding: 0.7rem 0;
        font-size: 1.05rem;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Display the main application title.
st.markdown(
    '<div class="main-title">📄 AI Resume Analyzer</div>',
    unsafe_allow_html=True
)


# Display the application subtitle.
st.markdown(
    '<div class="subtitle">'
    'Analyze your resume, discover matching job roles, '
    'identify skill gaps, and build a learning roadmap.'
    '</div>',
    unsafe_allow_html=True
)


# Display the application workflow.
st.markdown(
    """
    <div class="Job-card">
        <b>Resume → Skills → Job Matching → Skill Gaps → Learning Roadmap</b>
    </div>
    """,
    unsafe_allow_html=True
)


# Create the resume upload section.
st.subheader("📤 Upload Your Resume")


# Allow the user to upload PDF or DOCX files.
uploaded_file = st.file_uploader(
    "Choose your resume",
    type=["pdf", "docx"],
    help="Upload a PDF or DOCX resume."
)


# Continue only when the user uploads a resume.
if uploaded_file is not None:

    # Display the uploaded file name.
    st.success(f"Uploaded: {uploaded_file.name}")

    # Create the Analyze Resume button.
    analyze_button = st.button(
        "🔍 Analyze Resume",
        use_container_width=True
    )

    # Run the analysis only when the button is clicked.
    if analyze_button:

        # Show a progress spinner while processing the resume.
        with st.spinner("Analyzing your resume..."):

            # Extract text from the uploaded resume.
            extracted_text = extract_resume_text(uploaded_file)

            # Check whether any text was extracted.
            if not extracted_text.strip():

                # Display an error when no text is found.
                st.error(
                    "No readable text was found in the uploaded resume."
                )

                # Stop the current Streamlit execution.
                st.stop()

            # Clean and normalize the extracted resume text.
            cleaned_text = clean_resume_text(extracted_text)

            # Load the controlled skill dictionary.
            skill_data = load_skill_dictionary()

            # Extract skills from the cleaned resume.
            resume_skills = extract_skills(
                cleaned_text,
                skill_data
            )

            # Categorize the extracted skills.
            categorized_skills = categorize_skills(
                resume_skills,
                skill_data
            )

            # Load all available job roles.
            job_roles = load_job_roles()

            # Compare the resume with all job roles.
            job_results = match_resume_to_jobs(
                resume_skills,
                job_roles
            )

            # Select the highest-matching role for database storage.
            if job_results:
                top_role = job_results[0]["role"]
                top_match_score = job_results[0]["match_score"]
            else:
                top_role = "No matching role"
                top_match_score = 0

            # Save the resume analysis summary in the authenticated user's Supabase history.
            try:

                # Insert the analysis record with the current user's authenticated ID.
                supabase.table("resume_history").insert({
                    "user_id": st.session_state["user_id"],
                    "file_name": uploaded_file.name,
                    "skills_detected": len(resume_skills),
                    "top_role": top_role,
                    "top_match_score": top_match_score
                }).execute()

            # Handle database errors without hiding the analysis results.
            except Exception as error:

                # Inform the user that the analysis worked but history could not be saved.
                st.error(f"Analysis completed, but history could not be saved: {error}")

            # Store the analysis results in Streamlit session state.
            st.session_state["resume_skills"] = resume_skills
            st.session_state["categorized_skills"] = categorized_skills
            st.session_state["job_results"] = job_results

        # Display a success message after analysis.
        st.success("Resume analysis completed successfully!")


# Display results only when analysis data exists.
if "job_results" in st.session_state:

    # Retrieve stored resume skills.
    resume_skills = st.session_state["resume_skills"]

    # Retrieve stored categorized skills.
    categorized_skills = st.session_state["categorized_skills"]

    # Retrieve stored job matching results.
    job_results = st.session_state["job_results"]


    # Add a horizontal separator.
    st.divider()


    # Create the main results heading.
    st.header("📊 Resume Analysis")


    # Create three columns for summary metrics.
    col1, col2, col3 = st.columns(3)


    # Display the total number of detected skills.
    with col1:

        # Show the skill count as a metric.
        st.metric(
            "Skills Detected",
            len(resume_skills)
        )


    # Display the number of analyzed job roles.
    with col2:

        # Show the job role count as a metric.
        st.metric(
            "Job Roles Analyzed",
            len(job_results)
        )


    # Display the highest available skill-match score.
    with col3:

        # Find the highest match score.
        highest_score = max(
            result["match_score"]
            for result in job_results
        )

        # Display the highest score.
        st.metric(
            "Highest Skill Match",
            f"{highest_score}%"
        )


    # Add a separator before the skills section.
    st.divider()


    # Create the extracted skills section.
    st.subheader("🧩 Extracted Skills")


    # Check whether any skills were detected.
    if resume_skills:

        # Create an empty string to store the skill chips.
        skill_chips = ""

        # Loop through every detected skill.
        for skill in resume_skills:

            # Create a visual chip for the current skill.
            skill_chips += (
                f'<span class="skill-chip">{skill}</span>'
            )

        # Display all detected skills as visual chips.
        st.markdown(
            skill_chips,
            unsafe_allow_html=True
        )

    else:

        # Inform the user when no skills were detected.
        st.warning(
            "No skills from the current skill dictionary were detected."
        )


    # Display categorized skills.
    if categorized_skills:

        # Create an expandable section for skill categories.
        with st.expander("View Skills by Category"):

            # Loop through every skill category.
            for category, skills in categorized_skills.items():

                # Display the category name.
                st.markdown(f"**{category}**")

                # Display the skills in that category.
                st.write(", ".join(skills))


    # Add a separator before job matching.
    st.divider()


    # Create the top job recommendations section.
    st.subheader("🏆 Top 3 Job Role Matches")


    # Select the top three job roles from the sorted results.
    top_three_roles = job_results[:3]


    # Create three columns for the top three roles.
    top_col1, top_col2, top_col3 = st.columns(3)


    # Store the three columns in a list for easier processing.
    top_columns = [top_col1, top_col2, top_col3]


    # Loop through the top three job roles.
    for column, result in zip(top_columns, top_three_roles):

        # Display each role inside its own column.
        with column:

            # Create a visual card for the recommended role.
            st.markdown(
                f"""
                <div class="info-card">
                    <h3>💼 {result['role']}</h3>
                    <h2>{result['match_score']}%</h2>
                    <p>Skill Match</p>
                </div>
                """,
                unsafe_allow_html=True
            )


    # Add a separator after the top three recommendations.
    st.divider()


    # Create the job comparison chart section.
    st.subheader("📈 Job Role Match Comparison")


    # Create a list of job role names.
    role_names = [
        result["role"]
        for result in job_results
    ]


    # Create a list of match scores.
    match_scores = [
        result["match_score"]
        for result in job_results
    ]


    # Create a dictionary containing the chart data.
    chart_data = {
        "Job Role": role_names,
        "Match Score": match_scores
    }


    # Create an interactive horizontal bar chart.
    figure = px.bar(
        chart_data,
        x="Match Score",
        y="Job Role",
        orientation="h",
        text="Match Score",
        title="Resume Skill Match by Job Role"
    )


    # Display the percentage value on each bar.
    figure.update_traces(
        texttemplate="%{text}%",
        textposition="outside"
    )


    # Set the chart's X-axis range from 0 to 100.
    figure.update_xaxes(
        range=[0, 100],
        title="Match Score (%)"
    )


    # Set the Y-axis title.
    figure.update_yaxes(
        title="Job Role"
    )


    # Display the interactive chart.
    st.plotly_chart(
        figure,
        use_container_width=True
    )


    # Add a separator before detailed analysis.
    st.divider()


    # Create the detailed job matching section.
    st.subheader("💼 Detailed Job Role Analysis")


    # Display every available job role.
    for result in job_results:

        # Create two columns for the role name and score.
        role_col, score_col = st.columns([3, 1])


        # Display the job role name.
        with role_col:

            # Show the current job role.
            st.markdown(
                f"### {result['role']}"
            )


        # Display the match score.
        with score_col:

            # Show the current match score.
            st.metric(
                "Match",
                f"{result['match_score']}%"
            )


        # Display a visual progress bar for the match score.
        st.progress(
            int(result["match_score"])
        )


        # Check whether the job role has missing skills.
        if result["missing_skills"]:

            # Create a formatted list of missing skills.
            missing_skills_text = ", ".join(
                result["missing_skills"]
            )

            # Display missing skills inside a dedicated box.
            st.markdown(
                f"""
                <div class="missing-box">
                    <b>❌ Missing Skills</b><br>
                    {missing_skills_text}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            # Display a success message when no skills are missing.
            st.success(
                "No missing skills from the current role dictionary."
            )


        # Create an expandable learning roadmap section.
        with st.expander(
            f"🗺️ Learning Roadmap — {result['role']}"
        ):

            # Generate the roadmap using the missing skills.
            roadmap = generate_roadmap(
                result["missing_skills"]
            )


            # Check whether roadmap items exist.
            if roadmap:

                # Loop through every roadmap item.
                for item in roadmap:

                                        # Display the skill as a roadmap heading.
                    st.markdown(
                        f"""
                        <div class="roadmap-skill">
                            📚 {item['skill'].title()}
                            — {item['level']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                    # Display every recommended learning topic.
                    for topic in item["topics"]:

                        # Display the current learning topic.
                        st.markdown(
                            f"- {topic}"
                        )

            else:

                # Display a message when no additional learning is required.
                st.success(
                    "No additional roadmap items are required."
                )


        # Add spacing between job roles.
        st.write("")



    # Display the responsible-AI disclaimer.
    st.markdown(
        """
        <div class="disclaimer">
        <b>⚠️ Important:</b><br>
        This application provides an estimated skill-match analysis
        based on the information detected in the resume and the
        configured job-role requirements. It is intended as a
        guidance tool and should not be used as an automatic hiring
        or rejection decision.
        </div>
        """,
        unsafe_allow_html=True
    )
# Display the signed-in user's saved analysis history from Supabase.
st.divider()
st.subheader("🗃️ Your Previous Analysis History")

# Retrieve only the current authenticated user's history through Supabase Row Level Security.
try:

    # Fetch the current user's records, newest first.
    history_response = (
        supabase.table("resume_history")
        .select("file_name, skills_detected, top_role, top_match_score, created_at")
        .order("created_at", desc=True)
        .execute()
    )

    # Read the returned history records.
    analysis_history = history_response.data or []

    # Display the history when records are available.
    if analysis_history:

        # Convert the Supabase records into a DataFrame.
        history_df = pd.DataFrame(analysis_history)

        # Number only the records returned for the currently signed-in user.
        history_df.insert(0, "No.", range(1, len(history_df) + 1))

        # Rename database columns to user-friendly display names.
        history_df = history_df.rename(columns={
            "file_name": "Resume File",
            "skills_detected": "Skills Detected",
            "top_role": "Top Matching Role",
            "top_match_score": "Top Match Score (%)",
            "created_at": "Analyzed At"
        })

        # Display the formatted analysis history.
        st.dataframe(
            history_df,
            hide_index=True,
            use_container_width=True
        )

    else:

        # Show a message when the current user has no saved history.
        st.info("You have not saved any resume analyses yet.")

# Handle Supabase history retrieval errors.
except Exception as error:

    # Display the database error to the signed-in user.
    st.error(f"Could not load your analysis history: {error}")

# Add spacing before the reset button.
st.write("")

# Create a reset button for analyzing another resume.
if st.button(
    "🔄 Analyze Another Resume",
    use_container_width=True
):

    # Clear only the current resume analysis results.
    for state_key in ["resume_skills", "categorized_skills", "job_results"]:
        st.session_state.pop(state_key, None)

    # Reload the application while keeping the user logged in.
    st.rerun()