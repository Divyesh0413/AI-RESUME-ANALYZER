
# Import Streamlit for creating the authentication interface.
import streamlit as st


# Create a function to display the signup and login page.
def show_auth_page(supabase):

    # Display the authentication page heading.
    st.title("Welcome to AI Resume Analyzer")

    # Create separate tabs for login and signup.
    login_tab, signup_tab = st.tabs(["Login", "Sign Up"])

    # Create the login form.
    with login_tab:

        # Ask the user for their email address.
        login_email = st.text_input("Email", key="login_email")

        # Ask the user for their password.
        login_password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        # Create the login button.
        if st.button("Login", key="login_button"):

            # Check that both fields are filled.
            if not login_email or not login_password:
                st.warning("Please enter your email and password.")

            else:
                try:
                    # Authenticate the user with Supabase.
                    response = supabase.auth.sign_in_with_password({
                        "email": login_email,
                        "password": login_password
                    })

                    # Check whether a valid session was created.
                    if response.session:

                        # Store the authenticated user's ID.
                        st.session_state.user_id = response.user.id

                        # Mark the user as logged in.
                        st.session_state.logged_in = True

                        # Refresh the Streamlit application.
                        st.rerun()

                    else:
                        # Show a message if no session was returned.
                        st.error("Login failed. Please try again.")

                except Exception as error:
                    # Display the authentication error.
                    st.error(f"Login failed: {error}")

    # Create the signup form.
    with signup_tab:

        # Ask the new user for their email address.
        signup_email = st.text_input("Email", key="signup_email")

        # Ask the new user to create a password.
        signup_password = st.text_input(
            "Create Password",
            type="password",
            key="signup_password"
        )

        # Create the signup button.
        if st.button("Create Account", key="signup_button"):

            # Check that both fields are filled.
            if not signup_email or not signup_password:
                st.warning("Please enter your email and password.")

            # Check the minimum password length.
            elif len(signup_password) < 6:
                st.warning("Password must contain at least 6 characters.")

            else:
                try:
                    # Register the new user with Supabase.
                    response = supabase.auth.sign_up({
                        "email": signup_email,
                        "password": signup_password
                    })

                    # Check whether email confirmation is required.
                    if response.session:

                        # Store the new user's ID.
                        st.session_state.user_id = response.user.id

                        # Mark the user as logged in.
                        st.session_state.logged_in = True

                        # Refresh the application.
                        st.rerun()

                    else:
                        # Ask the user to confirm their email.
                        st.success(
                            "Account created! Please check your email "
                            "and confirm your account before logging in."
                        )

                except Exception as error:
                    # Display the signup error.
                    st.error(f"Signup failed: {error}")
