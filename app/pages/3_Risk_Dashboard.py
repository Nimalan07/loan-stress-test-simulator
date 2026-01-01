import streamlit as st
import plotly.express as px
import pandas as pd
from services.ratio_calculator import calculate_ratios
from services.risk_evaluator import evaluate_risk
st.set_page_config(layout="wide")
st.header("RISK ASSESSMENT DASHBOARD")

if "stressed_data" not in st.session_state or "loan_data" not in st.session_state:
    st.warning("Apply a stress scenario to view risk assessment")
else:
    base = st.session_state["loan_data"]
    stressed = st.session_state["stressed_data"]
    scenario = st.session_state.get("selected_scenario", "—")

    st.subheader("LOAN SUMMARY")

    s1, s2, s3 = st.columns(3)
    with s1:
        st.metric("Loan Amount", f"{base['loan_amount']:,.0f}")
    with s2:
        st.metric("Interest Rate", f"{base['interest_rate']} %")
    with s3:
        st.metric("Scenario", scenario.upper())

    ratios_before = calculate_ratios(base)
    ratios_after = calculate_ratios(stressed)
    risk_status = evaluate_risk(ratios_after)

    st.markdown("---")
    st.subheader("KEY FINANCIAL INDICATORS")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "DSCR",
            ratios_after["DSCR"],
            delta=round(ratios_after["DSCR"] - ratios_before["DSCR"], 2)
        )
        st.caption("Minimum acceptable: 1.20")
        st.caption("Ability of cash flow to cover debt obligations (≥ 1.2 preferred)")


    with c2:
        st.metric(
            "Debt / EBITDA",
            ratios_after["Debt / EBITDA"],
            delta=round(ratios_after["Debt / EBITDA"] - ratios_before["Debt / EBITDA"], 2)
        )
        st.caption("Recommended maximum: 4.00")
        st.caption("Years of operating profit required to repay total debt")


    with c3:
        st.metric(
            "Interest Coverage",
            ratios_after["Interest Coverage"],
            delta=round(
                ratios_after["Interest Coverage"] - ratios_before["Interest Coverage"], 2
            )
        )
        st.caption("Ability of earnings to cover interest payments")


    st.markdown("---")
    st.subheader("OVERALL RISK INTERPRETATION")
    st.caption("Derived from stressed financial ratios and covenant thresholds")

    st.metric("Risk Classification", risk_status)
    st.caption("Indicative guidance for credit risk teams")

    if "High Risk" in risk_status:
        st.error(
            "Risk has increased significantly due to higher debt servicing pressure and reduced cash flow coverage."
        )
    elif "Medium Risk" in risk_status:
        st.warning(
            "Financial buffers have weakened under stress. Continued monitoring is recommended."
        )
    else:
        st.success(
            "The loan remains resilient under the selected stress scenario."
        )

    st.markdown("---")
    st.subheader("WHAT CHANGED UNDER STRESS")

    st.markdown(
        f"""
        - **Interest Rate Impact:** Interest burden increased due to scenario assumptions  
        - **Cash Flow Impact:** Operating cash flow declined under stress  
        - **Coverage Ratios:** Debt servicing buffers reduced compared to baseline  
        """
    )

    st.markdown("---")
    st.subheader("RECOMMENDED ACTIONS")

    if "High Risk" in risk_status:
        st.markdown(
            """
            - Review covenant thresholds and borrower buffers  
            - Consider restructuring or credit enhancement  
            - Increase monitoring frequency  
            """
        )
    elif "Medium Risk" in risk_status:
        st.markdown(
            """
            - Monitor borrower performance closely  
            - Run additional downside scenarios  
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
    st.subheader("POST-STRESS RATIO VISUALIZATION")

    fig = px.bar(
        x=list(ratios_after.keys()),
        y=list(ratios_after.values()),
        color=list(ratios_after.keys()),
        color_discrete_sequence=["#2563eb"],
        title="Financial Ratios After Stress Scenario"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("DOWNLOAD RISK SUMMARY")

    export_df = pd.DataFrame([
        {
            "Scenario": scenario,
            "Risk Level": risk_status,
            "DSCR": ratios_after["DSCR"],
            "Debt / EBITDA": ratios_after["Debt / EBITDA"],
            "Interest Coverage": ratios_after["Interest Coverage"]
        }
    ])

    st.download_button(
        "Download Risk Summary (CSV)",
        export_df.to_csv(index=False),
        file_name="risk_summary.csv",
        mime="text/csv"
    )
