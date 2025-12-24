import streamlit as st
from services.stress_engine import apply_stress

st.header("Stress Scenario Testing")

if "loan_data" not in st.session_state:
    st.warning("Please enter loan data first")
else:
    rate_shock = st.slider("Interest Rate Increase (%)", 0.0, 5.0, 1.0)
    revenue_drop = st.slider("Revenue Drop (%)", 0.0, 50.0, 10.0)
    cost_increase = st.slider("Cost Increase (%)", 0.0, 30.0, 5.0)

    stressed = apply_stress(
        st.session_state["loan_data"],
        rate_shock,
        revenue_drop,
        cost_increase
    )

    st.session_state["stressed_data"] = stressed
    st.success("Stress scenario applied")
