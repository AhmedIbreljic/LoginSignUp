import pickle
from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth

# --- USER AUTHENTICATION ---
names = ["Peter Parker", "Rebecca Miller", "bharath"]
usernames = ["pparker", "rmiller", "bharath"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "SIPL_dashboard", "abcdef")

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")
    st.markdown(hide_bar, unsafe_allow_html=True)

if authentication_status == None:
    st.warning("Please enter your username and password")
    st.markdown(hide_bar, unsafe_allow_html=True)

if authentication_status:
    # ---- SIDEBAR ----
    st.sidebar.title(f"Welcome {name}")

    # Display main content
    st.write("# Welcome to Streamlit!")
    st.subheader("Introduction:")
    st.markdown("1. \n2. \n3. \n4. \n5. \n")
    st.sidebar.success("Select a page above.")

    # Hide Streamlit style
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # Logout button
    authenticator.logout("Logout", "sidebar")
