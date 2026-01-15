import streamlit as st

# Page Configuration
st.set_page_config(page_title="Ezra Yek | Portfolio", page_icon="", layout="wide")

# Custom CSS for Futuristic Glassmorphism & Apple Aesthetic
st.markdown("""
    <style>
    /* Global Background */
    .stApp {
        background-color: #000000;
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Helvetica Neue", sans-serif;
    }

    /* Futuristic Glassmorphism Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(20, 20, 25, 0.7) !important;
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 10px 0 30px rgba(0, 0, 0, 0.5);
    }

    /* Sidebar Text & Icons */
    [data-testid="stSidebar"] section {
        padding-top: 2rem;
    }
    
    .sidebar-header {
        font-size: 1.8rem;
        font-weight: 700;
        background: linear-gradient(180deg, #ffffff 0%, #a1a1a6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
        letter-spacing: -0.05em;
    }

    .contact-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 10px;
        transition: 0.3s ease;
    }
    .contact-card:hover {
        border-color: #2997ff;
        box-shadow: 0 0 15px rgba(41, 151, 255, 0.2);
    }

    /* Global White Text */
    body, p, span, li, label, .stMarkdown {
        color: #f5f5f7 !important;
    }

    /* Apple-style bold headers */
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* Futuristic Skill Capsules with Glow */
    .skill-tag {
        background-color: rgba(29, 29, 31, 0.8);
        border: 1px solid rgba(41, 151, 255, 0.3);
        border-radius: 20px;
        padding: 6px 15px;
        margin: 4px;
        display: inline-block;
        color: #2997ff !important;
        font-size: 0.8rem;
        font-family: "SF Mono", "Fira Code", monospace;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Tech Accents */
    .blue-glow {
        color: #2997ff;
        text-shadow: 0 0 10px rgba(41, 151, 255, 0.5);
        font-weight: bold;
    }

    /* Minimalist Divider */
    hr {
        border-color: rgba(255, 255, 255, 0.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Futuristic Sidebar Content ---
with st.sidebar:
    st.markdown('<div class="sidebar-header">SYSTEM OVERVIEW</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="contact-card">
        <p style='font-size: 0.7rem; color: #a1a1a6 !important; margin:0;'>NAME</p>
        <p style='font-size: 1.1rem; font-weight: 600; margin:0;'>Ezra Yek Nai En</p>
    </div>
    <div class="contact-card">
        <p style='font-size: 0.7rem; color: #a1a1a6 !important; margin:0;'>LOCATION</p>
        <p style='font-size: 0.9rem; margin:0;'>Perak, Malaysia</p>
    </div>
    <div class="contact-card">
        <p style='font-size: 0.7rem; color: #a1a1a6 !important; margin:0;'>CONNECT</p>
        <p style='font-size: 0.8rem; margin:0;'>ezrayek9113@gmail.com</p>
        <p style='font-size: 0.8rem; margin:0;'>+6017-369-1389</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown('<p class="blue-glow">STATUS: READY FOR INTERNSHIP</p>', unsafe_allow_html=True)
    st.write("Availability: May - Dec 2026")
    
    st.divider()
    st.markdown("[Linktree Portfolio](https://linktr.ee/EzraY0503)")

# --- Main Hero Section ---
st.markdown("<h1 style='font-size: 4rem; text-align: left; margin-top: -50px;'>Design the impossible.</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.5rem; text-align: left; color: #a1a1a6 !important; max-width: 600px;'>Next-generation GPU and SoC Performance Research.</p>", unsafe_allow_html=True)

# --- Content Sections ---
st.write(" ")
tab1, tab2, tab3 = st.tabs(["[ 01 INVENTIONS ]", "[ 02 ACADEMICS ]", "[ 03 CORE STACK ]"])

with tab1:
    st.markdown("## Where code meets physical reality.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<p class='blue-glow'>PROJECT_01: MEDICARE</p>", unsafe_allow_html=True)
        st.write("Solving health accessibility with high-efficiency mobile design.")
        st.video("https://youtu.be/yUmpZJamrjA")
    
    with col2:
        st.markdown("<p class='blue-glow'>PROJECT_02: SNEAKER STERILISER</p>", unsafe_allow_html=True)
        st.write("Award-winning hardware integration using multi-sensor feedback.")
        st.video("https://youtu.be/2WdHeu2sXKI")

with tab2:
    st.markdown("## Analytical Rigor.")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("Universiti Teknologi PETRONAS")
        st.markdown("### B.Eng (Hons) Electrical & Electronics")
        st.write("Current CGPA: **3.03**")
    with col_b:
        st.write("Distinctions:")
        st.markdown("""
        - **Microprocessor Architecture:** A-
        - **Structured Programming:** B+
        - **Mixed Signal Systems:** B+
        """)

with tab3:
    st.markdown("## Technical Stack")
    
    skills = ["Python", "C++", "SystemVerilog", "NI Multisim", "PSpice", "Eagle", "IC Fabrication", "ARM Architecture", "RTOS"]
    
    skill_html = ""
    for skill in skills:
        skill_html += f'<div class="skill-tag">{skill}</div>'
    st.markdown(skill_html, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### Experience Highlights")
    st.write("Data analysis for **2000+ units** at KTS Trading. Managing high-stakes curriculum design for **IGCSE/IB** students.")



# Footer
st.markdown("<p style='text-align: center; margin-top: 50px; opacity: 0.4;'>Proprietary Portfolio Design | 2026</p>", unsafe_allow_html=True)