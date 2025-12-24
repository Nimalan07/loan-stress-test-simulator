import streamlit as st
st.set_page_config(
    page_title="Loan Stress-Test Simulator",
    layout="wide"
)
st.title("🏦 Loan Stress-Test Simulator")
st.markdown(
    """
    This application allows banks and risk teams to simulate
    economic stress scenarios and evaluate loan safety in real time.
    """
)
st.markdown("### How to use")
st.markdown(
    """
    1. Enter loan and borrower details  
    2. Apply stress scenarios  
    3. Review risk impact and ratios  
    """
)
st.sidebar.success("Select a page to begin")
