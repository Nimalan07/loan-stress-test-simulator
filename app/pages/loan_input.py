import streamlit as st

st.header("Loan and Borrower Details")

st.subheader("Loan Details")
c1, c2, c3 = st.columns(3)

with c1:
    loan_amount = st.number_input("Loan Amount", value=1_000_000.0)
with c2:
    interest_rate = st.slider("Interest Rate (%)", 1.0, 20.0, 8.0)
with c3:
    tenure = st.number_input("Tenure (Years)", value=5)

st.subheader("Borrower Financials")
c4, c5, c6 = st.columns(3)

with c4:
    revenue = st.number_input("Revenue", value=2_000_000.0)
with c5:
    ebitda = st.number_input("EBITDA", value=600_000.0)
with c6:
    cashflow = st.number_input("Cash Flow", value=500_000.0)

if st.button("Save Loan Data", use_container_width=True):
    st.session_state["loan_data"] = {
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "tenure": tenure,
        "revenue": revenue,
        "ebitda": ebitda,
        "cashflow": cashflow
    }
    st.success("Loan data saved successfully")
