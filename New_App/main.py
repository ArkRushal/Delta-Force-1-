import streamlit as st
from New_App.pages import Jobset, side

st.title("Simple Job Search App")
st.header("Find Your Dream Job")

if "name" not in st.session_state:
    st.session_state.name = ""
if "age" not in st.session_state:
    st.session_state.age = 0
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.error("You're not logged in. Please Login to continue.")
    st.write("Please enter your name to get started.")
    st.session_state.name = st.text_input("Enter your name here")
    st.write("Please enter your age.")
    st.session_state.age = st.number_input("Enter your age here", min_value=0, max_value=120, value=0)
    if st.session_state.age <= 13:
        st.error("Sorry, you must be at least 14 years old to use this app.")

    if st.button("Login"):
        st.session_state.logged_in = True
        st.success(f"Logged in as {st.session_state.name}.")
else:
    st.write(f"Welcome back, {st.session_state.name}!")
    st.write(f"Would you like to offer a job, or look for a job?")
    offer_job = st.button("Offer a Job")
    look_for_job = st.button("Look for a Job")
    if offer_job:
        st.switch_page("pages/Jobset.py")
    elif look_for_job:
        st.switch_page("pages/side.py")
