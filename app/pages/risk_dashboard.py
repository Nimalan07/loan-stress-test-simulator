import streamlit as st
import plotly.express as px
from services.ratio_calculator import calculate_ratios
from services.risk_evaluator import evaluate_risk

st.header("RISK ASSESSMENT DASHBOARD")

if "stressed_data" not in st.session_state:
    st.warning("Run a stress scenario to view risk assessment")
else:
    ratios = calculate_ratios(st.session_state["stressed_data"])
    risk_status = evaluate_risk(ratios)

    st.subheader("KEY FINANCIAL INDICATORS")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("DSCR", ratios["DSCR"])
        st.caption("Minimum acceptable level: 1.20")

    with c2:
        st.metric("Debt / EBITDA", ratios["Debt / EBITDA"])
        st.caption("Recommended maximum: 4.00")

    with c3:
        st.metric("Interest Coverage", ratios["Interest Coverage"])
        st.caption("Higher values indicate stronger debt servicing ability")

    st.markdown("---")

    st.subheader("OVERALL RISK EVALUATION")
    st.metric("Risk Classification", risk_status)

    if "High Risk" in risk_status:
        st.error(
            "The loan shows a high likelihood of covenant breach under the selected stress scenario."
        )
    elif "Medium Risk" in risk_status:
        st.warning(
            "The loan remains serviceable but shows reduced financial buffers under stress."
        )
    else:
        st.success(
            "The loan remains resilient under the selected stress scenario."
        )

    st.markdown("---")

    st.subheader("RECOMMENDED ACTIONS")

    if "High Risk" in risk_status:
        st.markdown(
            """
            - Review covenant structure and borrower buffers  
            - Consider credit enhancements or restructuring  
            - Increase monitoring frequency  
            """
        )
    elif "Medium Risk" in risk_status:
        st.markdown(
            """
            - Monitor borrower performance closely  
            - Run additional stress scenarios  
            - Assess downside protection  
            """
        )
    else:
        st.markdown(
            """
            - Continue standard monitoring  
            - No immediate intervention required  
            """
        )

    st.markdown("---")

    st.subheader("POST-STRESS RATIO COMPARISON")

    fig = px.bar(
        x=list(ratios.keys()),
        y=list(ratios.values()),
        color=list(ratios.keys()),
        color_discrete_sequence=["#2563eb"],
        title="Financial Ratios After Stress Scenario"
    )

    st.plotly_chart(fig, use_container_width=True)
