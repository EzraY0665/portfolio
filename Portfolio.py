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
/* Global Background - Set to White */
.stApp {
    background-color: #ffffff;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif;
}

/* Sidebar Styling - Dark for Contrast */
[data-testid="stSidebar"] {
    background-color: #1d1d1f !important; 
    color: #ffffff !important;
}

/* Sidebar Button - White Text on Blue Background */
div.stDownloadButton > button, .cta-button, .stLinkButton > a {
    background-color: #0071e3 !important;
    color: #ffffff !important;
    border-radius: 20px !important;
    border: none !important;
    padding: 10px 20px !important;
    font-weight: 600 !important;
    text-decoration: none !important;
    display: inline-block;
    text-align: center;
}

/* Top Column/Header Area Text */
.top-header {
    background-color: #f5f5f7;
    padding: 25px;
    border-radius: 0 0 20px 20px;
    margin-bottom: 30px;
    border-bottom: 1px solid #d2d2d7;
}

/* ALL MAIN TEXT - Black for White Background */
h1, h2, h3, p, span, li, label, .stMarkdown {
    color: #1d1d1f !important; 
}

/* Spec Cards */
.spec-card {
    background: #f5f5f7;
    border: 1px solid #d2d2d7;
    border-radius: 14px;
    padding: 16px;
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
    <div style='color: #a1a1a6; font-size: 0.8rem;'>FULL NAME</div>
    <div style='color: white; font-weight: 600; margin-bottom: 15px;'>Ezra Yek Nai En </div>
    
    <div style='color: #a1a1a6; font-size: 0.8rem;'>STATUS</div>
    <div style='color: #34c759; font-weight: 600;'>● ACTIVE FOR INTERNSHIP </div>

    <div style='color: #a1a1a6; font-size: 0.8rem;'>INTERNSHIP PERIOD</div>
    <div style='color: white; font-weight: 600; margin-bottom: 15px;'>May 2026 - December 2026 </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Updated Sidebar Button
    st.link_button("📂 VIEW RESUME & TRANSCRIPT", "https://drive.google.com/drive/folders/1NSOTqV13CA8yGr_vKzIZBWDTTf0uYvZf")

# ===============================
# Top Header Column
# ===============================
st.markdown("""
<div class="top-header">
    <p style="margin:0; font-size: 0.8rem; font-weight: 600; color: #86868b !important;">
        PORTFOLIO OVERVIEW // 2026 INTERNSHIP APPLICATION
    </p>
    <h1 style="margin:0; font-size: 2.5rem;">Architecture & Innovation.</h1>
</div>
""", unsafe_allow_html=True)

# ===============================
# Main Content
# ===============================
tab1, tab2 = st.tabs(["[ 01 INVENTIONS ]", "[ 02 ACADEMICS ]"])

with tab1:
    st.markdown("## Engineering the future of GPUs. ") 
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### MediCare Mobile App")
        st.video("https://youtu.be/yUmpZJamrjA")
        st.markdown("""
        <div class="spec-grid">
            <div class="spec-card">
                <div class="spec-title">The Vision</div>
                <div class="spec-value"><b>Healthcare, simplified.</b> Developed as a Champion-tier project to bridge the gap between patients and providers.</div>
            </div>
            <div class="spec-card">
                <div class="spec-title">Key Intelligence</div>
                <div class="spec-value">BMI Analysis · Medical Records Vault · NPRA Verification.</div>
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
                <div class="spec-value"><b>Intelligence in every cycle.</b> Utilizing microcontrollers and multi-sensor feedback for automated hygiene.</div>
            </div>
            <div class="spec-card">
                <div class="spec-title">Technical Achievement</div>
                <div class="spec-value">Bronze Prize at IPITEx Bangkok for hardware-software integration.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("## Academic Foundation")
    st.write("**Universiti Teknologi PETRONAS**")
    st.write("B.Eng (Hons) Electrical & Electronics — **CGPA 3.03** ")
    
    st.markdown("""
    <div class="spec-card">
        <div class="spec-title">Key Performance Metrics</div>
        <div class="spec-value">
            • <b>Microprocessor & Computer Architecture:</b> A- (Distinction)<br>
            • <b>Integrated Circuit Fabrication:</b> Hands-on cleanroom experience in photolithography and etching.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<p style='text-align:center; margin-top:50px; color: #86868b !important;'>Proprietary Portfolio Design | 2026</p>", unsafe_allow_html=True)