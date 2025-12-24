import streamlit as st
import plotly.express as px
from services.ratio_calculator import calculate_ratios
from services.risk_evaluator import evaluate_risk

st.header("Risk Dashboard")

if "stressed_data" not in st.session_state:
    st.warning("Please apply a stress scenario first")
else:
    ratios = calculate_ratios(st.session_state["stressed_data"])
    risk_status = evaluate_risk(ratios)

    st.subheader("Overall Risk Status")
    st.metric("Risk Level", risk_status)

    st.subheader("Key Financial Ratios")
    st.write(ratios)

    fig = px.bar(
        x=list(ratios.keys()),
        y=list(ratios.values()),
        title="Ratios After Stress Scenario"
    )
    st.plotly_chart(fig, use_container_width=True)
