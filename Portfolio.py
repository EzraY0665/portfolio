import streamlit as st

# ===============================
# Page Configuration
# ===============================
st.set_page_config(
    page_title="Ezra Yek | Portfolio",
    page_icon="",
    layout="wide"
)

# ===============================
# CSS + Visibility Fixes
# ===============================
st.markdown("""
<style>
.stApp { background-color: #ffffff; font-family: -apple-system, sans-serif; }
[data-testid="stSidebar"] { background-color: #1d1d1f !important; color: #ffffff !important; }

/* Apple Blue Button */
div.stDownloadButton > button, .stLinkButton > a {
    background-color: #0071e3 !important;
    color: #ffffff !important;
    border-radius: 20px !important;
    border: none !important;
    padding: 10px 20px !important;
    font-weight: 600 !important;
    text-decoration: none !important;
    display: inline-block;
}

/* Typography */
h1, h2, h3, p, span, li, .stMarkdown { color: #1d1d1f !important; }

.top-header {
    background-color: #f5f5f7;
    padding: 25px;
    border-radius: 0 0 20px 20px;
    margin-bottom: 30px;
    border-bottom: 1px solid #d2d2d7;
}

.spec-card {
    background: #f5f5f7;
    border: 1px solid #d2d2d7;
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 12px;
}

.spec-title {
    font-size: 0.7rem;
    color: #0071e3 !important;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# Sidebar
# ===============================
with st.sidebar:
    st.markdown("<h2 style='color:white !important;'>SYSTEM ACCESS</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='color: #a1a1a6; font-size: 0.8rem;'>OPERATOR</div>
    <div style='color: white; font-weight: 600; margin-bottom: 15px;'>Ezra Yek Nai En</div>
    <div style='color: #a1a1a6; font-size: 0.8rem;'>STATUS</div>
    <div style='color: #34c759; font-weight: 600;'>● AVAILABLE FOR INTERNSHIP</div>
    <div style='color: white; font-size: 0.85rem;'>May – Dec 2026</div>
    """, unsafe_allow_html=True)
    st.divider()
    st.link_button("📂 VIEW RESUME & TRANSCRIPT", "https://drive.google.com/drive/folders/1NSOTqV13CA8yGr_vKzIZBWDTTf0uYvZf")

# ===============================
# Top Header
# ===============================
st.markdown("""
<div class="top-header">
    <p style="margin:0; font-size: 0.8rem; font-weight: 600; color: #86868b !important;">
        PORTFOLIO OVERVIEW // PLATFORM ARCHITECTURE CANDIDATE
    </p>
    <h1 style="margin:0; font-size: 2.5rem;">Architecture & Innovation.</h1>
    <p style="margin-top:10px; color: #0071e3 !important; font-weight: 500;">
        Python · C++ · SystemVerilog · Arduino · Raspberry Pi · NI Multisim · PSpice
    </p>
</div>
""", unsafe_allow_html=True)

# ===============================
# Main Tabs
# ===============================
tab1, tab2, tab3 = st.tabs(["[ 01 INVENTIONS ]", "[ 02 ACADEMICS ]", "[ 03 EXPERIENCE ]"])

with tab1:
    st.markdown("## Engineering the future of GPUs.")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### MediCare Mobile App")
        st.video("https://youtu.be/yUmpZJamrjA")
        st.markdown("""
        <div class="spec-grid">
            <div class="spec-card">
                <div class="spec-title">The Vision</div>
                <div class="spec-value"><b>Healthcare, simplified.</b> Developed as a Champion-tier project to connect patients with providers seamlessly.</div>
            </div>
            <div class="spec-card">
                <div class="spec-title">Technical Execution</div>
                <div class="spec-value">
                    • <b>Interface Integration:</b> Engineered deep-links to the NPRA portal for live medication search functionality.<br>
                    • <b>System Logic:</b> Architected tools for BMI calculation and secure health record management.
                </div>
            </div>
            <div class="spec-card">
                <div class="spec-title">Engineering Philosophy</div>
                <div class="spec-value">
                    • <b>System Thinking:</b> Leveraged official databases to provide real-time verification with zero server latency.<br>
                    • <b>Impact:</b> Successfully bridged clinical-grade data with mobile accessibility.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### Sneaker Steriliser")
        st.video("https://youtu.be/2WdHeu2sXKI")
        st.markdown("""
        <div class="spec-grid">
            <div class="spec-card">
                <div class="spec-title">The Vision</div>
                <div class="spec-value"><b>Intelligence in every cycle.</b> A microcontroller-driven automated solution for footwear hygiene, earning a Bronze Prize at IPITEx Bangkok.</div>
            </div>
            <div class="spec-card">
                <div class="spec-title">Technical Execution</div>
                <div class="spec-value">
                    • <b>Sensor Fusion:</b> Orchestrated multiple sensors to monitor and control the sterilization environment in real-time.<br>
                    • <b>Hardware Control:</b> Integrated microcontroller logic with sterilization hardware for 99% bacterial reduction.
                </div>
            </div>
            <div class="spec-card">
                <div class="spec-title">Engineering Philosophy</div>
                <div class="spec-value">
                    • <b>Hardware-Software Co-design:</b> Solved hygiene challenges through rapid prototyping and embedded logic.<br>
                    • <b>Global Standard:</b> Refined for international exhibition and technical scrutiny.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### Automatic Toilet Door (WYIE)")
    st.write("Developed an IoT-enabled system using microcontrollers and sensors to automate facility access, participating three times (2018–2020) in the World Young Inventors Exhibition.")

with tab2:
    st.markdown("## Academic Foundation")
    st.write("**Universiti Teknologi PETRONAS**")
    st.write("B.Eng (Hons) Electrical & Electronics — **CGPA 3.03**")
    
    col_ed1, col_ed2 = st.columns(2)
    with col_ed1:
        st.markdown("""
        <div class="spec-card">
            <div class="spec-title">Key Performance Metrics</div>
            <div class="spec-value">
                • <b>Microprocessor Architecture:</b> A- (Distinction in Foundation/Degree Core).<br>
                • <b>IC Fabrication Workshop:</b> Executed cleanroom photolithography, wet etching, and source diffusion.<br>
                • <b>SPM Excellence:</b> 5A+, 5A, 1A- at SMK Sacred Heart.
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_ed2:
        st.markdown("""
        <div class="spec-card">
            <div class="spec-title">Technical Certifications</div>
            <div class="spec-value">
                • <b>Pearson LCCI Level 2:</b> Certificate in Book-keeping & Accounts.<br>
                • <b>Speaker @ Bengkel Coding:</b> Trained 50 participants in MIT App Inventor development.
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("## Professional & Leadership Experience")
    
    st.markdown("#### Account Assistant | KTS Trading Sdn. Bhd")
    st.write("*May 2022 – Aug 2022*")
    st.write("- Assisted senior accountants in analyzing sales and cost data for over 2,000+ units across Malaysia.")
    st.write("- Streamlined data collection processes, reducing financial reporting time by 10%")
    
    st.divider()
    
    st.markdown("#### Tuition Centre Operator | Ipoh, Perak")
    st.write("*Sep 2022 – Present*")
    st.write("- Independently manage a sole proprietorship providing specialized IGCSE, IB, and Cambridge instruction.")
    st.write("- Handle curriculum design, client relations, and instruction for 5 international/local students.")

# ===============================
# Footer
# ===============================
st.markdown("<p style='text-align:center; margin-top:50px; color: #86868b !important; opacity:0.6;'>Proprietary Portfolio Design | Ezra Yek © 2026</p>", unsafe_allow_html=True)
