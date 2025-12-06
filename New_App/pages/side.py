import streamlit as st
from pages.Jobset import Fulltime, Parttime, Internship, Remote

if "name" not in st.session_state:
    st.session_state.name = ""
if "age" not in st.session_state:
    st.session_state.age = 0
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.header(f"Welcome {st.session_state.name} to the Simple Job Search App!")
st.write("Use the filters below to find job listings that match your preferences.")
time = ["", "Full-time", "Part-time", "Internship", "Remote"]
jobtype = st.selectbox(
    "Select Job Type", 
    time,
    index=0,
    key="side_jobtype"
)

if jobtype == "Full-time":
    st.write("Showing Full-time job listings:")
    with open("Fulltimejobs.txt", "r", encoding="utf-8") as f:
        jobs = f.readlines()
        for job in jobs:
            line = job.strip()
            if not line:
                continue
            parts = line.split("|")
            Jobname = parts[0] if len(parts) > 0 else ""
            Jobdesc = parts[1] if len(parts) > 1 else ""
            Jobloc = parts[2] if len(parts) > 2 else ""
            Jobsalary = parts[3] if len(parts) > 3 else ""
            Contactinfo = parts[4] if len(parts) > 4 else "N/A"
            st.subheader(Jobname)
            st.write(f"Description: {Jobdesc}")
            st.write(f"Location: {Jobloc}")
            st.write(f"Salary per hour: ${Jobsalary}")
            st.write(f"Contact Information: {Contactinfo}")

elif jobtype == "Part-time":
    st.write("Showing Part-time job listings:")
    with open("Fulltimejobs.txt", "r", encoding="utf-8") as f:
        jobs = f.readlines()
        for job in jobs:
            line = job.strip()
            if not line:
                continue
            parts = line.split("|")
            Jobname = parts[0] if len(parts) > 0 else ""
            Jobdesc = parts[1] if len(parts) > 1 else ""
            Jobloc = parts[2] if len(parts) > 2 else ""
            Jobsalary = parts[3] if len(parts) > 3 else ""
            Contactinfo = parts[4] if len(parts) > 4 else "N/A"
            st.subheader(Jobname)
            st.write(f"Description: {Jobdesc}")
            st.write(f"Location: {Jobloc}")
            st.write(f"Salary: ${Jobsalary}")
            st.write(f"Contact Information: {Contactinfo}")

elif jobtype == "Internship":
    st.write("Showing Internship job listings:")
    with open("Fulltimejobs.txt", "r", encoding="utf-8") as f:
        jobs = f.readlines()
        for job in jobs:
            line = job.strip()
            if not line:
                continue
            parts = line.split("|")
            Jobname = parts[0] if len(parts) > 0 else ""
            Jobdesc = parts[1] if len(parts) > 1 else ""
            Jobloc = parts[2] if len(parts) > 2 else ""
            Jobsalary = parts[3] if len(parts) > 3 else ""
            Contactinfo = parts[4] if len(parts) > 4 else "N/A"
            st.subheader(Jobname)
            st.write(f"Description: {Jobdesc}")
            st.write(f"Location: {Jobloc}")
            st.write(f"Salary: ${Jobsalary}")
            st.write(f"Contact Information: {Contactinfo}")

elif jobtype == "Remote":
    st.write("Showing Remote job listings:")
    with open("Fulltimejobs.txt", "r", encoding="utf-8") as f:
        jobs = f.readlines()
        for job in jobs:
            line = job.strip()
            if not line:
                continue
            parts = line.split("|")
            Jobname = parts[0] if len(parts) > 0 else ""
            Jobdesc = parts[1] if len(parts) > 1 else ""
            Jobloc = parts[2] if len(parts) > 2 else ""
            Jobsalary = parts[3] if len(parts) > 3 else ""
            Contactinfo = parts[4] if len(parts) > 4 else "N/A"
            st.subheader(Jobname)
            st.write(f"Description: {Jobdesc}")
            st.write(f"Location: {Jobloc}")
            st.write(f"Salary: ${Jobsalary}")
            st.write(f"Contact Information: {Contactinfo}")