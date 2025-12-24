def calculate_ratios(data):
    interest_expense = data["loan_amount"] * data["interest_rate"] / 100

    dscr = data["cashflow"] / interest_expense if interest_expense > 0 else 0
    debt_ebitda = data["loan_amount"] / data["ebitda"] if data["ebitda"] > 0 else 0
    interest_coverage = data["ebitda"] / interest_expense if interest_expense > 0 else 0

    return {
        "DSCR": round(dscr, 2),
        "Debt / EBITDA": round(debt_ebitda, 2),
        "Interest Coverage": round(interest_coverage, 2)
    }
