import streamlit as st
from pages.Jobset import Fulltime, Parttime, Internship, Remote

if "name" not in st.session_state:
    st.session_state.name = ""
if "age" not in st.session_state:
    st.session_state.age = 0
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "min_salary" not in st.session_state:
    st.session_state.min_salary = 0

def display_jobs(job_type_label):
    """Display jobs filtered by job type and minimum salary"""
    min_salary = st.session_state.min_salary
    st.write(f"Showing {job_type_label} job listings (Min Salary: ${min_salary}/hour):")
    
    try:
        with open("Fulltimejobs.txt", "r", encoding="utf-8") as f:
            jobs = f.readlines()
            job_count = 0
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
                Companyname = parts[5] if len(parts) > 5 else "N/A"
                
                try:
                    salary_num = float(Jobsalary) if Jobsalary else 0
                except ValueError:
                    salary_num = 0
                
                if salary_num >= min_salary:
                    job_count += 1
                    st.subheader(Jobname)
                    st.write(f"{Companyname}")
                    st.write(f"Description: {Jobdesc}")
                    st.write(f"Location: {Jobloc}")
                    st.write(f"Salary per hour: ${Jobsalary}")
                    st.write(f"Contact Information: {Contactinfo}")
                    st.divider()
            
            if job_count == 0:
                st.info(f"No {job_type_label} jobs found matching your salary requirement.")
    except FileNotFoundError:
        st.warning("Job database not found. No jobs to display yet.")

st.header(f"Welcome {st.session_state.name} to the Simple Job Search App!")
st.write("Use the filters below to find job listings that match your preferences.")

st.subheader("Filters")
st.session_state.min_salary = st.number_input(
    "Minimum Salary (per hour):",
    min_value=0,
    value=st.session_state.min_salary,
    step=1,
    key="min_salary_filter"
)

time = ["", "Full-time", "Part-time", "Internship", "Remote"]
jobtype = st.selectbox(
    "Select Job Type", 
    time,
    index=0,
    key="side_jobtype"
)

if jobtype == "Full-time":
    display_jobs("Full-time")
elif jobtype == "Part-time":
    display_jobs("Part-time")
elif jobtype == "Internship":
    display_jobs("Internship")
elif jobtype == "Remote":
    display_jobs("Remote")
