import streamlit as st

if "jobs" not in st.session_state:
    st.session_state.jobs = []

def Fulltime():
    subheader = st.subheader("Full-time Job Listings")
    Companyname = st.text_input("Enter your company's name:", key="full_companyname")
    Jobname = st.text_input("Enter the work you're offering:", key="full_jobname")
    Jobdesc = st.text_area("Enter the job description:", key="full_jobdesc")
    Jobloc = st.text_input("Enter the job location:", key="full_jobloc")
    Jobsalary = st.number_input("Enter your offered salary:", min_value=0, key="full_jobsalary")
    Contactinfo = st.text_input("Enter your contact information (email or phone):", key="full_contactinfo")
    if Jobname and Contactinfo and Jobdesc and Jobloc and Jobsalary > 0:
        st.success("Job offered successfully!")
        open("Fulltimejobs.txt", "a").write(f"{Jobname}|{Jobdesc}|{Jobloc}|{Jobsalary}|{Contactinfo}|{Companyname}\n")
    
    return Jobname, Jobdesc, Jobloc, Jobsalary, Contactinfo, Companyname

def Parttime():
    subheader = st.subheader("Part-time Job Listings")
    Companyname = st.text_input("Enter your company's name:", key="part_companyname")
    Jobname = st.text_input("Enter the work you're offering:", key="part_jobname")
    Jobdesc = st.text_area("Enter the job description:", key="part_jobdesc")
    Jobloc = st.text_input("Enter the job location:", key="part_jobloc")
    Jobsalary = st.number_input("Enter your offered salary:", min_value=0, key="part_jobsalary")
    Contactinfo = st.text_input("Enter your contact information (email or phone):", key="part_contactinfo")
    if Jobname and Contactinfo and Jobdesc and Jobloc and Jobsalary > 0:
        st.success("Job offered successfully!")
        open("Fulltimejobs.txt", "a").write(f"{Jobname}|{Jobdesc}|{Jobloc}|{Jobsalary}|{Contactinfo}|{Companyname}\n")
    
    return Jobname, Jobdesc, Jobloc, Jobsalary, Contactinfo, Companyname

def Internship():
    subheader = st.subheader("Internship Job Listings")
    Companyname = st.text_input("Enter your company's name:", key="intern_companyname")
    Jobname = st.text_input("Enter the work you're offering:", key="intern_jobname")
    Jobdesc = st.text_area("Enter the job description:", key="intern_jobdesc")
    Jobloc = st.text_input("Enter the job location:", key="intern_jobloc")
    Jobsalary = st.number_input("Enter your offered salary:", min_value=0, key="intern_jobsalary")
    Contactinfo = st.text_input("Enter your contact information (email or phone):", key="intern_contactinfo")
    if Jobname and Contactinfo and Jobdesc and Jobloc and Jobsalary > 0:
        st.success("Job offered successfully!")
        open("Fulltimejobs.txt", "a").write(f"{Jobname}|{Jobdesc}|{Jobloc}|{Jobsalary}|{Contactinfo}|{Companyname}\n")
    
    return Jobname, Jobdesc, Jobloc, Jobsalary, Contactinfo, Companyname

def Remote():
    subheader = st.subheader("Remote Job Listings")
    Companyname = st.text_input("Enter your company's name:", key="remote_companyname")
    Jobname = st.text_input("Enter the work you're offering:", key="remote_jobname")
    Jobdesc = st.text_area("Enter the job description:", key="remote_jobdesc")
    Jobloc = st.text_input("Enter the job location:", key="remote_jobloc")
    Jobsalary = st.number_input("Enter your offered salary:", min_value=0, key="remote_jobsalary")
    Contactinfo = st.text_input("Enter your contact information (email or phone):", key="remote_contactinfo")
    if Jobname and Contactinfo and Jobdesc and Jobloc and Jobsalary > 0:
        st.success("Job offered successfully!")
        open("Fulltimejobs.txt", "a").write(f"{Jobname}|{Jobdesc}|{Jobloc}|{Jobsalary}|{Contactinfo}|{Companyname}\n")
    
    return Jobname, Jobdesc, Jobloc, Jobsalary, Contactinfo, Companyname
    

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
