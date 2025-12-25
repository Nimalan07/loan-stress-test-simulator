import streamlit as st
import json
import os
from services.stress_engine import apply_stress

st.header("Stress Scenario Selection")

base_dir = os.path.dirname(os.path.dirname(__file__))
scenario_path = os.path.join(base_dir, "data", "scenarios.json")

with open(scenario_path) as f:
    scenarios = json.load(f)

if "loan_data" not in st.session_state:
    st.warning("Please enter loan data first")
else:
    scenario_name = st.selectbox(
        "Choose Scenario",
        list(scenarios.keys())
    )

    scenario = scenarios[scenario_name]

    st.info(scenario["description"])

    stressed = apply_stress(
        st.session_state["loan_data"],
        scenario["interest_rate_shock"],
        abs(scenario["revenue_change_pct"]),
        scenario["cost_change_pct"]
    )

    if st.button("Apply Stress Scenario", use_container_width=True):
        st.session_state["stressed_data"] = stressed
        st.success("Stress scenario applied")
