import streamlit as st

# Page configuration
st.set_page_config(page_title="Kaam Bhandar", page_icon="💼", layout="centered")

# Bright and tachy CSS
st.markdown(
    """
    <style>
    /* Base background */
    .stApp {
        background-color: #ffffff;
    }

    /* Floating tachy circles */
    .tachy1, .tachy2, .tachy3 {
        position: absolute;
        border-radius: 50%;
        opacity: 0.3;
        z-index: -1;
        animation: float 6s ease-in-out infinite alternate;
    }
    .tachy1 {
        width: 80px; height: 80px; background: #FF6B6B; top: 10%; left: 5%;
    }
    .tachy2 {
        width: 120px; height: 120px; background: #4ECDC4; top: 30%; right: 10%;
    }
    .tachy3 {
        width: 60px; height: 60px; background: #FFD93D; bottom: 15%; left: 20%;
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(20px); }
        100% { transform: translateY(0px); }
    }

    /* Card style for forms */
    .card {
        background: #ffffff;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    /* Gradient buttons */
    .stButton>button {
        background: linear-gradient(90deg, #FF6B6B, #FFD93D, #4ECDC4);
        color: #ffffff;
        font-weight: bold;
        padding: 10px 25px;
        border-radius: 12px;
        border: none;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
    }

    /* Header styling */
    h1 {
        color: #FF6B6B;
        text-align: center;
        font-size: 50px;
        font-weight: bold;
    }
    h3 {
        color: #4ECDC4;
        text-align: center;
        font-size: 28px;
    }

    /* Gradient dividers */
    .gradient-divider {
        width: 100%;
        height: 10px;
        background: linear-gradient(90deg, #FF6B6B, #FFD93D, #4ECDC4);
        border-radius: 5px;
        margin: 20px 0;
    }
    </style>

    <div class="tachy1"></div>
    <div class="tachy2"></div>
    <div class="tachy3"></div>
    """,
    unsafe_allow_html=True
)

# Title and header
st.markdown("<h1>Kaam Bhandar</h1>", unsafe_allow_html=True)
st.markdown("<h3>Find Your Dream Job</h3>", unsafe_allow_html=True)

# Gradient divider
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

# Initialize session state
if "name" not in st.session_state:
    st.session_state.name = ""
if "age" not in st.session_state:
    st.session_state.age = 0
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login section
if not st.session_state.logged_in:
    with st.form(key="login_form"):
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Enter Your Details")
        st.session_state.name = st.text_input("Name")
        st.session_state.age = st.number_input("Age", min_value=0, max_value=120, value=0)

        if st.session_state.age <= 13 and st.session_state.age != 0:
            st.error("Sorry, you must be at least 14 years old to use this app.")

        login_btn = st.form_submit_button("Login")
        if login_btn and st.session_state.age > 13 and st.session_state.name.strip() != "":
            st.session_state.logged_in = True
            st.success(f"Logged in as {st.session_state.name}!")
        st.markdown("</div>", unsafe_allow_html=True)

# Main app after login
else:
    st.success(f"Welcome back, {st.session_state.name}!")
    st.write("What would you like to do today?")
    
    # Gradient separator
    st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Offer a Job"):
            st.switch_page("Jobset")
    with col2:
        if st.button("Look for a Job"):
            st.switch_page("side")

    st.write("---")
    st.markdown("💡 **Tip:** Use the buttons above to navigate through the app.")