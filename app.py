"""
=========================================================
SRSentinel AI
Main Streamlit Application
=========================================================
"""

import os
import streamlit as st

# ==========================================================
# Project Modules
# ==========================================================

from modules.document_reader import DocumentReader
from modules.nlp_processor import NLPProcessor
from modules.predictor import Predictor
from modules.ambiguity_detector import AmbiguityDetector
from modules.requirement_classifier import RequirementClassifier
from modules.quality_score import QualityScore
from modules.explainable_ai import ExplainableAI
from modules.suggestion_generator import SuggestionGenerator
from modules.report_generator import ReportGenerator

# ==========================================================
# Dashboard Charts
# ==========================================================

from charts.pie_chart import create_pie_chart
from charts.gauge_chart import create_gauge_chart
from charts.quality_bar import create_quality_bar
from charts.impact_chart import create_impact_chart

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="SRSentinel AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# Assets Folder
# ==========================================================

os.makedirs("assets", exist_ok=True)

# ==========================================================
# Custom CSS
# ==========================================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.main{
    background:#F5F7FB;
}

.dashboard-header{
    background:linear-gradient(90deg,#4F46E5,#2563EB);
    padding:30px;
    border-radius:20px;
    color:white;
    margin-bottom:20px;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    text-align:center;
}

.section-title{
    font-size:26px;
    font-weight:bold;
    margin-top:25px;
    margin-bottom:15px;
    color:#1E293B;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# Initialize Modules
# ==========================================================

reader = DocumentReader()
nlp = NLPProcessor()
predictor = Predictor()
classifier = RequirementClassifier()
ambiguity_detector = AmbiguityDetector()
quality_calculator = QualityScore()
xai = ExplainableAI()
suggestion_generator = SuggestionGenerator()
report_generator = ReportGenerator()

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("🤖 SRSentinel AI")

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ Upload SRS Document")
    st.write("✅ NLP Processing")
    st.write("✅ Requirement Classification")
    st.write("✅ Ambiguity Detection")
    st.write("✅ ML Prediction")
    st.write("✅ Explainable AI")
    st.write("✅ PDF Report")

    st.markdown("---")

    st.subheader("Technology")

    st.write("• Python")
    st.write("• NLP")
    st.write("• Machine Learning")
    st.write("• Streamlit")
    st.write("• Explainable AI")

    st.markdown("---")

    st.subheader("Developed By")

    st.write("Bhoomi Joshi")
    st.write("Jhanvi Pangam")
    st.write("Aaiman Khan")

# ==========================================================
# Header
# ==========================================================

st.markdown("""

<div class="dashboard-header">

<h1>🤖 SRSentinel AI</h1>

<h4>
AI-Based Software Requirement Specification Quality Analyzer
</h4>

<p>
Natural Language Processing • Machine Learning • Explainable AI
</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# Upload Section
# ==========================================================

st.markdown(
    "<div class='section-title'>📂 Upload SRS Document</div>",
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose PDF / DOCX / TXT File",
    type=["pdf", "docx", "txt"]
)

# ==========================================================
# Process Uploaded File
# ==========================================================

if uploaded_file is not None:

    try:

        with st.spinner("📖 Reading document..."):

            document_text = reader.read_document(uploaded_file)

    except Exception as e:

        st.error(f"Error reading document: {e}")
        st.stop()

    if not document_text.strip():

        st.error("No readable text found in the document.")
        st.stop()

    st.success("✅ Document uploaded successfully.")

    # ======================================================
    # Extracted Text
    # ======================================================

    st.markdown(
        "<div class='section-title'>📄 Extracted Text</div>",
        unsafe_allow_html=True
    )

    with st.expander("View Extracted Text"):

        st.text_area(
            "Document",
            document_text,
            height=300
        )

    # ======================================================
    # NLP Processing
    # ======================================================

    with st.spinner("🧠 Performing NLP Processing..."):

        cleaned_text = nlp.clean_text(document_text)

    st.success("✅ NLP Processing Completed")
    with st.expander("View Cleaned Text"):

        st.text_area(
            "Cleaned Text",
            cleaned_text,
            height=250
        )

    # ==========================================================
    # Document Statistics
    # ==========================================================

    total_words = len(document_text.split())
    total_characters = len(document_text)
    total_lines = len(document_text.splitlines())

    st.markdown(
        "<div class='section-title'>📊 Document Statistics</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Words",
            total_words
        )

    with col2:
        st.metric(
            "Characters",
            total_characters
        )

    with col3:
        st.metric(
            "Lines",
            total_lines
        )

    st.divider()

    # ==========================================================
    # Machine Learning Prediction
    # ==========================================================

    with st.spinner("🤖 Predicting SRS Quality..."):

        prediction_report = predictor.generate_prediction_report(
            cleaned_text
        )

    st.success("✅ Machine Learning Prediction Completed")

    # ==========================================================
    # Requirement Classification
    # ==========================================================

    with st.spinner("📑 Classifying Requirements..."):

        classifier_report = classifier.generate_report(
            document_text
        )

    statistics = classifier_report["statistics"]

    # ==========================================================
    # Ambiguity Detection
    # ==========================================================

    with st.spinner("🔍 Detecting Ambiguous Words..."):

        ambiguity_report = ambiguity_detector.generate_report(
            document_text
        )

    # ==========================================================
    # Quality Score
    # ==========================================================

    quality_report = quality_calculator.generate_report(

        total_requirements=statistics["total"],

        ambiguous_words=ambiguity_report["count"],

        functional=statistics["functional"],

        non_functional=statistics["non_functional"]

    )

    # ==========================================================
    # Explainable AI
    # ==========================================================

    xai_report = xai.generate_report(

        quality=prediction_report["quality"],

        quality_score=quality_report["quality_score"],

        ambiguity_count=ambiguity_report["count"],

        functional=statistics["functional"],

        non_functional=statistics["non_functional"]

    )

    # ==========================================================
    # Suggestions
    # ==========================================================

    suggestion_report = suggestion_generator.generate_report(

        ambiguous_words=ambiguity_report["ambiguous_words"],

        functional_count=statistics["functional"],

        non_functional_count=statistics["non_functional"],

        quality_score=quality_report["quality_score"]

    )

    # ==========================================================
    # AI Dashboard
    # ==========================================================

    st.markdown(
        "<div class='section-title'>📊 AI Analysis Dashboard</div>",
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Prediction",
            prediction_report["quality"]
        )

    with c2:
        st.metric(
            "Confidence",
            f"{prediction_report['confidence']}%"
        )

    with c3:
        st.metric(
            "Quality Score",
            f"{quality_report['quality_score']}/100"
        )

    with c4:
        st.metric(
            "Grade",
            quality_report["grade"]
        )

    st.divider()
    # ==========================================================
    # Requirement Statistics
    # ==========================================================

    st.markdown(
        "<div class='section-title'>📋 Requirement Statistics</div>",
        unsafe_allow_html=True
    )

    s1, s2, s3, s4 = st.columns(4)

    s1.metric(
        "Total Requirements",
        statistics["total"]
    )

    s2.metric(
        "Functional",
        statistics["functional"]
    )

    s3.metric(
        "Non Functional",
        statistics["non_functional"]
    )

    s4.metric(
        "Ambiguous Words",
        ambiguity_report["count"]
    )

    st.divider()

    # ==========================================================
    # Overall Quality Score
    # ==========================================================

    st.markdown(
        "<div class='section-title'>⭐ Overall Quality Score</div>",
        unsafe_allow_html=True
    )

    st.progress(
        int(quality_report["percentage"])
    )

    st.success(
        f"Quality Score : {quality_report['quality_score']}/100"
    )

    st.divider()

    # ==========================================================
    # Dashboard Charts
    # ==========================================================

    st.markdown(
        "<div class='section-title'>📊 Dashboard Charts</div>",
        unsafe_allow_html=True
    )

    pie_chart = create_pie_chart(
        statistics["functional"],
        statistics["non_functional"],
        statistics["others"]
    )

    gauge_chart = create_gauge_chart(
        quality_report["quality_score"]
    )

    quality_bar = create_quality_bar(
        quality_report["quality_score"]
    )

    impact_chart = create_impact_chart(
        ambiguity_report["ambiguity_score"],
        quality_report["quality_score"]
    )

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.plotly_chart(
            gauge_chart,
            use_container_width=True
        )

    with row1_col2:
        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.plotly_chart(
            quality_bar,
            use_container_width=True
        )

    with row2_col2:
        st.plotly_chart(
            impact_chart,
            use_container_width=True
        )

    st.divider()

    # ==========================================================
    # Analysis Tabs
    # ==========================================================

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📄 Extracted Text",
        "📑 Classification",
        "⚠ Ambiguity",
        "🧠 Explainable AI",
        "💡 Suggestions"
    ])

    # ==========================================================
    # TAB 1
    # ==========================================================

    with tab1:

        st.subheader("Extracted SRS Document")

        st.text_area(
            "Document",
            document_text,
            height=400
        )

    # ==========================================================
    # TAB 2
    # ==========================================================

    with tab2:

        st.subheader("Functional Requirements")

        if classifier_report["functional_requirements"]:

            for item in classifier_report["functional_requirements"]:
                st.success(item)

        else:

            st.info("No Functional Requirements detected.")

        st.subheader("Non Functional Requirements")

        if classifier_report["non_functional_requirements"]:

            for item in classifier_report["non_functional_requirements"]:
                st.info(item)

        else:

            st.info("No Non Functional Requirements detected.")

        st.subheader("Other Requirements")

        if classifier_report["other_requirements"]:

            for item in classifier_report["other_requirements"]:
                st.warning(item)

        else:

            st.success("No Other Requirements detected.")

    # ==========================================================
    # TAB 3
    # ==========================================================

    with tab3:

        st.subheader("Ambiguity Analysis")

        st.metric(
            "Ambiguous Words",
            ambiguity_report["count"]
        )

        st.metric(
            "Severity",
            ambiguity_report["severity"]
        )

        st.metric(
            "Ambiguity Score",
            ambiguity_report["ambiguity_score"]
        )

        if ambiguity_report["count"] == 0:

            st.success(
                "No ambiguity detected in the document."
            )

        else:

            for word in ambiguity_report["ambiguous_words"]:
                st.error(word)
    # ==========================================================
    # TAB 4
    # ==========================================================

    with tab4:

        st.subheader("🧠 Explainable AI")

        st.write("### Positive Indicators")

        for item in xai_report["positive_indicators"]:
            st.success(item)

        st.write("### Negative Indicators")

        for item in xai_report["negative_indicators"]:
            st.warning(item)

        st.write("### Feature Importance")

        st.json(
            xai_report["feature_importance"]
        )

        st.write("### AI Explanation")

        st.info(
            xai_report["explanation"]
        )

    # ==========================================================
    # TAB 5
    # ==========================================================

    with tab5:

        st.subheader("💡 Improvement Suggestions")

        st.write("### Ambiguity Suggestions")

        for item in suggestion_report["ambiguity_suggestions"]:
            st.write("•", item)

        st.write("### Functional Suggestions")

        for item in suggestion_report["functional_suggestions"]:
            st.write("•", item)

        st.write("### Non Functional Suggestions")

        for item in suggestion_report["non_functional_suggestions"]:
            st.write("•", item)

        st.write("### Improvement Checklist")

        for item in suggestion_report["improvement_checklist"]:
            st.success(item)

        st.write("### Best Practices")

        for item in suggestion_report["best_practices"]:
            st.write("✔", item)

    st.divider()

    # ==========================================================
    # Generate PDF Report
    # ==========================================================

    st.subheader("📄 Download Analysis Report")

    try:

        pdf = report_generator.generate_report(

            original_text=document_text,

            prediction=prediction_report,

            classification=classifier_report,

            ambiguity=ambiguity_report,

            quality=quality_report,

            xai=xai_report,

            suggestions=suggestion_report

        )

        st.download_button(

            "⬇ Download PDF Report",

            data=pdf,

            file_name="SRSentinel_AI_Report.pdf",

            mime="application/pdf"

        )

    except Exception as e:

        st.error(f"PDF Generation Error : {e}")

    st.divider()
    # ==========================================================
# FINAL FOOTER SECTION
# ==========================================================

st.markdown(
    """
    <div style="
    text-align:center;
    padding:20px;
    background:white;
    color:#1E293B;
    border-radius:15px;
    margin-top:20px;
    ">

    <h3 style="color:#2563EB;">
    🤖 SRSentinel AI
    </h3>

    <p>
    AI-Based Software Requirement Specification Quality Analyzer
    </p>

    <p>
    Built using NLP • Machine Learning • Explainable AI
    </p>

    <hr>

    <b style="color:#1E293B;">
    Developed By
    </b>

    Bhoomi Joshi (24CA1054)<br>
    Jhanvi Pangam (24CA1053)<br>
    Aaiman Khan (24CA1061)

    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# END OF APPLICATION
# ==========================================================

