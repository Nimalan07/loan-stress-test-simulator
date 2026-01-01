
# 📊 Loan Stress Test Simulator

An interactive loan stress-testing and risk assessment dashboard designed to support credit decision-making in lending institutions.

This tool allows users to evaluate how loans perform under different economic stress scenarios using transparent, rule-based financial analysis.

# 🚀 Overview

Loan stress testing is often done using static spreadsheets, making it slow, error-prone, and difficult to explain.
This project provides a simple, explainable, and interactive alternative that reflects real-world credit risk workflows.

The simulator enables:

Rapid scenario analysis

Clear before-and-after comparisons

Actionable risk interpretation

# 🎯 Key Features

Loan & Borrower Input

Loan amount, interest rate, tenure

Revenue, EBITDA, and cash flow

Predefined Stress Scenarios

Baseline

Mild, Moderate, and Severe stress

Rate shock only

Revenue shock only

Cost inflation

Risk Metrics

DSCR (Debt Service Coverage Ratio)

Debt / EBITDA

Interest Coverage Ratio

Risk Classification

Low, Medium, or High Risk

Clear interpretation and recommended actions

Exportable Output

Downloadable risk summary (CSV)

# 🧠 Why This Approach?

Explainable – no black-box models

Practical – mirrors how banks assess loan risk

Scalable by design – logic can extend to portfolio-level analysis

Safe for demos – uses synthetic, representative data

# 🏗️ Tech Stack

- Frontend & App Framework: Streamlit

- Data Handling: Pandas

- Visualization: Plotly

- Logic: Rule-based financial analysis

## 📁 Project Structure

```text
loan-stress-test-simulator/
├── app/
│   ├── MAIN.py
│   ├── pages/
│   │   ├── LOAN_INPUT.py
│   │   ├── SCENARIO_TEST.py
│   │   └── RISK_DASHBOARD.py
│   ├── services/
|   |   ├── __init__.py
│   │   ├── stress_engine.py
│   │   ├── ratio_calculator.py
│   │   └── risk_evaluator.py
│   ├── utils/
|   |   ├── __init__.py
│   │   ├── constants.py
│   │   └── validator.py
│   └── data/
|       └── scenarios.json
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── README.md
```


# ▶️ How to Run Locally
pip install -r requirements.txt
streamlit run app/main.py

# 🌐 Live Demo

👉 Deployed App:
Add your Streamlit Cloud URL here

# 🔮 Future Enhancements

Portfolio-level stress testing

ML-based advisory risk signals (optional, explainable)

PDF risk reports

Integration with internal bank data sources

# 🏦 Intended Users

Credit Risk Teams

Loan Operations

Portfolio Managers

Lending Analysts

# 📌 Disclaimer

This project uses synthetic data and simplified assumptions for demonstration purposes only.
It is not intended to replace formal credit approval systems.

🏁 Final Note

This project focuses on clarity, explainability, and real-world applicability — key requirements for risk-sensitive financial decision tools.
