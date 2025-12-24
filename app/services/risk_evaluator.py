def evaluate_risk(ratios):
    if ratios["DSCR"] < 1 or ratios["Debt / EBITDA"] > 4:
        return "🔴 High Risk"
    elif ratios["DSCR"] < 1.2:
        return "🟡 Medium Risk"
    else:
        return "🟢 Low Risk"
