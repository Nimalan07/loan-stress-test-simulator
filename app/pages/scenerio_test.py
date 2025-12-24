import streamlit as st
import json
import os
from services.stress_engine import apply_stress

st.header("Stress Scenario Testing")

base_dir = os.path.dirname(os.path.dirname(__file__))
scenario_path = os.path.join(base_dir, "data", "scenarios.json")

with open(scenario_path) as f:
    scenarios = json.load(f)

if "loan_data" not in st.session_state:
    st.warning("Please enter loan data first")
else:
    scenario_name = st.selectbox(
        "Select Stress Scenario",
        list(scenarios.keys())
    )

    scenario = scenarios[scenario_name]

    rate_shock = scenario["interest_rate_shock"]
    revenue_drop = abs(scenario["revenue_change_pct"])
    cost_increase = scenario["cost_change_pct"]

    st.markdown(f"**Scenario Description:** {scenario['description']}")

    stressed = apply_stress(
        st.session_state["loan_data"],
        rate_shock,
        revenue_drop,
        cost_increase
    )

    st.session_state["stressed_data"] = stressed
    st.success("Stress scenario applied successfully")
