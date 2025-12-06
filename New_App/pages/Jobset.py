import streamlit as st

if "jobs" not in st.session_state:
    st.session_state.jobs = []

def Fulltime():
    subheader = st.subheader("Full-time Job Listings")
    Jobname = st.text_input("Enter the work you're offering:")
    Jobdesc = st.text_area("Enter the job description:")
    Jobloc = st.text_input("Enter the job location:")
    Jobsalary = st.number_input("Enter your offered salary:", min_value=0, key="full_jobsalary")
    Contactinfo = st.text_input("Enter your contact information (email or phone):")
    if Jobname and Contactinfo and Jobdesc and Jobloc and Jobsalary > 0:
        st.success("Job offered successfully!")
        open("Fulltimejobs.txt", "a").write(f"{Jobname}|{Jobdesc}|{Jobloc}|{Jobsalary}|{Contactinfo}\n")
    
    return Jobname, Jobdesc, Jobloc, Jobsalary, Contactinfo

def Parttime():
    subheader = st.subheader("Part-time Job Listings")
    Jobname = st.text_input("Enter the work you're offering:")
    Jobdesc = st.text_area("Enter the job description:")
    Jobloc = st.text_input("Enter the job location:")
    Jobsalary = st.number_input("Enter your offered salary:", min_value=0, key="part_jobsalary")
    Contactinfo = st.text_input("Enter your contact information (email or phone):")
    if Jobname and Contactinfo and Jobdesc and Jobloc and Jobsalary > 0:
        st.success("Job offered successfully!")
        open("Fulltimejobs.txt", "a").write(f"{Jobname}|{Jobdesc}|{Jobloc}|{Jobsalary}|{Contactinfo}\n")
    
    return Jobname, Jobdesc, Jobloc, Jobsalary, Contactinfo

def Internship():
    subheader = st.subheader("Internship Job Listings")
    Jobname = st.text_input("Enter the work you're offering:")
    Jobdesc = st.text_area("Enter the job description:")
    Jobloc = st.text_input("Enter the job location:")
    Jobsalary = st.number_input("Enter your offered salary:", min_value=0, key="intern_jobsalary")
    Contactinfo = st.text_input("Enter your contact information (email or phone):")
    if Jobname and Contactinfo and Jobdesc and Jobloc and Jobsalary > 0:
        st.success("Job offered successfully!")
        open("Fulltimejobs.txt", "a").write(f"{Jobname}|{Jobdesc}|{Jobloc}|{Jobsalary}|{Contactinfo}\n")
    
    return Jobname, Jobdesc, Jobloc, Jobsalary, Contactinfo

def Remote():
    subheader = st.subheader("Remote Job Listings")
    Jobname = st.text_input("Enter the work you're offering:")
    Jobdesc = st.text_area("Enter the job description:")
    Jobloc = st.text_input("Enter the job location:")
    Jobsalary = st.number_input("Enter your offered salary:", min_value=0, key="remote_jobsalary")
    Contactinfo = st.text_input("Enter your contact information (email or phone):")
    if Jobname and Contactinfo and Jobdesc and Jobloc and Jobsalary > 0:
        st.success("Job offered successfully!")
        open("Fulltimejobs.txt", "a").write(f"{Jobname}|{Jobdesc}|{Jobloc}|{Jobsalary}|{Contactinfo}\n")
    
    return Jobname, Jobdesc, Jobloc, Jobsalary, Contactinfo
    

def jobset_page():
    st.header("What type of job would you like to offer?")
    time = ["", "Full-time", "Part-time", "Internship", "Remote"]
    jobtype = st.selectbox(
        "Select Job Type", 
        time,
        index=0,
        key="jobset_jobtype"
    )
    if jobtype == "Full-time":
        Fulltime()
        st.write("We'll send you a notification when a candidate applies.")
    elif jobtype == "Part-time":
        Parttime()
        st.write("We'll send you a notification when a candidate applies.")
    elif jobtype == "Internship":
        Internship()
        st.write("We'll send you a notification when a candidate applies.")
    elif jobtype == "Remote":
        Remote()
        st.write("We'll send you a notification when a candidate applies.")


if __name__ == "__main__":
    jobset_page()