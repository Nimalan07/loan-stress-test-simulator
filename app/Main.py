import streamlit as st

st.set_page_config(page_title="Loan Stress-Test Simulator", layout="wide")

st.markdown("""
<style>
.block-container { padding-top: 2rem; }
h1, h2, h3 { color: #0f172a; }
[data-testid="metric-container"] {
    background-color: #f8fafc;
    border: 1px solid #e5e7eb;
    padding: 1rem;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.title("🏦 Loan Stress-Test Simulator")
st.markdown(
    "Simulate economic stress scenarios and evaluate loan risk before losses occur."
)

st.sidebar.success("Select a page to continue")
