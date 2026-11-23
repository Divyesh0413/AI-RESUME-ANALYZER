

# Import Streamlit to manage user sessions and secrets.
import streamlit as st

# Import the Supabase client creation function.
from supabase import create_client

# Create a function to get a session-specific Supabase client.
def get_supabase_client():

    # Check whether this user already has a Supabase client.
    if "supabase" not in st.session_state:

        # Read the Supabase project URL.
        supabase_url = st.secrets["SUPABASE_URL"]

        # Read the Supabase publishable key.
        supabase_key = st.secrets["SUPABASE_KEY"]

        # Create a separate client for this Streamlit session.
        st.session_state.supabase = create_client(
            supabase_url,
            supabase_key
        )

    # Return the current user's Supabase client.
    return st.session_state.supabase
