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
# Language Selector
# ===============================
language = st.sidebar.selectbox("Select Language | 选择语言", ["English", "中文"])

# ===============================
# CSS + Biome Light Font
# ===============================
st.markdown("""
<style>
/* Biome Light Font */
@font-face {
    font-family: 'Biome Light';
    src: url('https://your-cdn-or-hosted-font/Biome-Light.woff2') format('woff2'),
         url('https://your-cdn-or-hosted-font/Biome-Light.woff') format('woff');
    font-weight: 300;
    font-style: normal;
}

.stApp { 
    background-color: #ffffff; 
    font-family: 'Biome Light', -apple-system, sans-serif; 
}

[data-testid="stSidebar"] { 
    background-color: #1d1d1f !important; 
    color: #ffffff !important; 
}

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
h1, h2, h3, p, span, li, .stMarkdown { 
    color: #1d1d1f !important; 
    font-family: 'Biome Light', -apple-system, sans-serif !important;
}

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
    font-family: 'Biome Light', -apple-system, sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# Sidebar
# ===============================
with st.sidebar:
    st.markdown("<h2 style='color:white !important;'>SYSTEM ACCESS | 系统访问</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='color: #a1a1a6; font-size: 0.8rem;'>FULL NAME / 全名</div>
    <div style='color: white; font-weight: 600; margin-bottom: 15px;'>Ezra Yek Nai En</div>
    <div style='color: #a1a1a6; font-size: 0.8rem;'>STATUS / 状态</div>
    <div style='color: #34c759; font-weight: 550;'>● AVAILABLE FOR INTERNSHIP / 可实习</div>
    <div style='color: white; font-size: 0.85rem;'>May – Dec 2026 / 2026年5月 – 12月</div>
    """, unsafe_allow_html=True)
    st.divider()
    st.link_button("📂 VIEW RESUME & TRANSCRIPT / 简历与成绩单", 
                   "https://drive.google.com/drive/folders/1NSOTqV13CA8yGr_vKzIZBWDTTf0uYvZf")

# ===============================
# Top Header
# ===============================
if language == "English":
    header_title = "Architecture & Innovation."
    header_subtitle = "Python · C++ · SystemVerilog · Arduino · Raspberry Pi · NI Multisim · PSpice"
    portfolio_overview = "PORTFOLIO OVERVIEW"
else:
    header_title = "架构与创新"
    header_subtitle = "Python · C++ · 系统Verilog · Arduino · 树莓派 · NI Multisim · PSpice"
    portfolio_overview = "作品集概览"

st.markdown(f"""
<div class="top-header">
    <p style="margin:0; font-size: 0.8rem; font-weight: 600; color: #86868b !important;">
        {portfolio_overview}
    </p>
    <h1 style="margin:0; font-size: 2.5rem;">{header_title}</h1>
    <p style="margin-top:10px; color: #0071e3 !important; font-weight: 500;">
        {header_subtitle}
    </p>
</div>
""", unsafe_allow_html=True)

# ===============================
# Content Tabs
# ===============================
tab1, tab2, tab3 = st.tabs([
    "01 INVENTIONS / 发明",
    "02 ACADEMICS / 学术",
    "03 EXPERIENCE / 经历"
])

# -------------------------------
# Tab 1: Inventions
# -------------------------------
with tab1:
    st.markdown("## Engineering and Energising the Future." if language=="English" else "## 精工筑世，动力未来")
    col1, col2 = st.columns(2)

    # MediCare
    with col1:
        st.markdown("### MediCare Mobile App" if language=="English" else "### MediCare 应用程序")
        st.video("https://youtu.be/yUmpZJamrjA")
        if language=="English":
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
        else:
            st.markdown("""
            <div class="spec-grid">
                <div class="spec-card">
                    <div class="spec-title">愿景</div>
                    <div class="spec-value"><b>简化医疗.</b> 作为冠军项目开发，旨在无缝连接患者与医疗提供者。</div>
                </div>
                <div class="spec-card">
                    <div class="spec-title">技术执行</div>
                    <div class="spec-value">
                        • <b>接口集成:</b> 连接 NPRA 门户，实现实时药品查询功能。<br>
                        • <b>系统逻辑:</b> 架构 BMI 计算及安全健康记录管理工具。
                    </div>
                </div>
                <div class="spec-card">
                    <div class="spec-title">工程理念</div>
                    <div class="spec-value">
                        • <b>系统思维:</b> 利用官方数据库提供零延迟实时验证。<br>
                        • <b>影响:</b> 成功将临床级数据与移动端可访问性结合。
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Sneaker Steriliser
    with col2:
        st.markdown("### Sneaker Steriliser" if language=="English" else "### 运动鞋消毒器")
        st.video("https://youtu.be/2WdHeu2sXKI")
        if language=="English":
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
        else:
            st.markdown("""
            <div class="spec-grid">
                <div class="spec-card">
                    <div class="spec-title">愿景</div>
                    <div class="spec-value"><b>每个周期的智能.</b> 微控制器驱动的自动化鞋类卫生解决方案，在 IPITEx 曼谷获得铜奖。</div>
                </div>
                <div class="spec-card">
                    <div class="spec-title">技术执行</div>
                    <div class="spec-value">
                        • <b>传感器融合:</b> 多传感器协作，实现实时监控与控制消毒环境。<br>
                        • <b>硬件控制:</b> 微控制器逻辑与消毒硬件结合，实现99%细菌消除。
                    </div>
                </div>
                <div class="spec-card">
                    <div class="spec-title">工程理念</div>
                    <div class="spec-value">
                        • <b>软硬件协同设计:</b> 通过快速原型和嵌入式逻辑解决卫生问题。<br>
                        • <b>国际标准:</b> 为国际展览与技术审查精心优化。
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# -------------------------------
# Tab 2: Academics
# -------------------------------
with tab2:
    st.markdown("## Academic Foundation" if language=="English" else "## 学术背景")
    st.write("**Universiti Teknologi PETRONAS**" if language=="English" else "**马来西亚国油科技大学**")
    st.write("B.Eng (Hons) Electrical & Electronics — **CGPA 3.03**" 
             if language=="English" else "电气与电子工程学士 — **CGPA 3.03**")
    
    col_ed1, col_ed2 = st.columns(2)
    if language=="English":
        st.markdown("""
        <div class="spec-card">
            <div class="spec-title">Key Performance Metrics</div>
            <div class="spec-value">
                • Microprocessor Architecture: A-<br>
                • IC Fabrication Workshop: Photolithography, wet etching, source diffusion.<br>
                • SPM Excellence: 5A+, 5A, 1A-
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="spec-card">
            <div class="spec-title">Technical Certifications</div>
            <div class="spec-value">
                • Pearson LCCI Level 2: Book-keeping & Accounts.<br>
                • Speaker @ Bengkel Coding: Trained 50 participants.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="spec-card">
            <div class="spec-title">关键绩效指标</div>
            <div class="spec-value">
                • 微处理器架构: A-<br>
                • IC 制造工作坊: 光刻, 湿法蚀刻, 材料扩散<br>
                • SPM 优异成绩: 5A+, 5A, 1A-
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="spec-card">
            <div class="spec-title">技术认证</div>
            <div class="spec-value">
                • Pearson LCCI Level 2: 记账与会计证书<br>
                • 编程工作坊讲师: 培训50名学员
            </div>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------
# Tab 3: Experience
# -------------------------------
with tab3:
    st.markdown("## Professional & Leadership Experience" if language=="English" else "## 工作与领导经验")
    
    if language=="English":
        st.markdown("#### Account Assistant | KTS Trading Sdn. Bhd")
        st.write("*May 2022 – Aug 2022*")
        st.write("- Assisted senior accountants in analyzing sales and cost data for over 2,000+ units across Malaysia.")
        st.write("- Streamlined data collection processes, reducing financial reporting time by 10%")
        
        st.divider()
        
        st.markdown("#### Tuition Centre Operator | Ipoh, Perak")
        st.write("*Sep 2022 – Present*")
        st.write("- Independently manage a sole proprietorship providing specialized IGCSE, IB, and Cambridge instruction.")
        st.write("- Handle curriculum design, client relations, and instruction for 5 international/local students.")
    else:
        st.markdown("#### 会计助理 | KTS Trading Sdn. Bhd")
        st.write("*2022年5月 – 2022年8月*")
        st.write("- 协助高级会计分析马来西亚2000多台设备的销售及成本数据。")
        st.write("- 精简数据收集流程，将财务报告时间缩短10%")
        
        st.divider()
        
        st.markdown("#### 补习中心运营者 | 怡保, 霹雳州")
        st.write("*2022年9月 – 至今*")
        st.write("- 独立运营一家提供IGCSE、IB及剑桥课程的教育机构。")
        st.write("- 负责课程设计、客户关系及5名学生的教学。")

# ===============================
# Footer
# ===============================
st.markdown("<p style='text-align:center; margin-top:50px; color: #86868b !important; opacity:0.6;'>Proprietary Portfolio Design | Ezra Yek © 2026</p>", unsafe_allow_html=True)






