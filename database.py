
# Import SQLite database support.
import sqlite3

# Define the database file name.
DATABASE_NAME = "resume_analyzer.db"


# Create a connection to the database.
def get_connection():

    # Connect to the SQLite database.
    connection = sqlite3.connect(DATABASE_NAME)

    # Return the database connection.
    return connection


# Create the database table.
def initialize_database():

    # Connect to the database.
    connection = get_connection()

    # Create a cursor to execute SQL commands.
    cursor = connection.cursor()

    # Create a table for resume analysis history.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT NOT NULL,
            skills_detected INTEGER NOT NULL,
            top_role TEXT,
            top_match_score REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Save database changes.
    connection.commit()

    # Close the connection.
    connection.close()


# Save resume analysis results.
def save_analysis(file_name, skills_detected, top_role, top_match_score):

    # Connect to the database.
    connection = get_connection()

    # Create a cursor.
    cursor = connection.cursor()

    # Insert analysis details into the table.
    cursor.execute("""
        INSERT INTO analysis_history
        (file_name, skills_detected, top_role, top_match_score)
        VALUES (?, ?, ?, ?)
    """, (file_name, skills_detected, top_role, top_match_score))

    # Save the record.
    connection.commit()

    # Close the connection.
    connection.close()


# Retrieve previous analysis records.
def get_analysis_history():

    # Connect to the database.
    connection = get_connection()

    # Create a cursor.
    cursor = connection.cursor()

    # Fetch all analysis records.
    cursor.execute("""
        SELECT * FROM analysis_history
        ORDER BY created_at DESC
    """)

    # Store the retrieved records.
    records = cursor.fetchall()

    # Close the connection.
    connection.close()

    # Return the records.
    return records
