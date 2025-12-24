import streamlit as st

st.header("Loan and Borrower Input")

loan_amount = st.number_input("Loan Amount", min_value=0.0, value=1_000_000.0)
interest_rate = st.slider("Interest Rate (%)", 1.0, 20.0, 8.0)
tenure = st.number_input("Tenure (Years)", min_value=1, value=5)

revenue = st.number_input("Annual Revenue", min_value=0.0, value=2_000_000.0)
ebitda = st.number_input("EBITDA", min_value=0.0, value=600_000.0)
cashflow = st.number_input("Annual Cash Flow", min_value=0.0, value=500_000.0)

if st.button("Save Data"):
    st.session_state["loan_data"] = {
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "tenure": tenure,
        "revenue": revenue,
        "ebitda": ebitda,
        "cashflow": cashflow
    }
    st.success("Data saved successfully")
