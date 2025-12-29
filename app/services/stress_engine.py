def apply_stress(data, rate_increase, revenue_drop, cost_increase):
    stressed = data.copy()

    stressed["interest_rate"] += rate_increase
    stressed["revenue"] *= (1 - revenue_drop / 100)
    stressed["ebitda"] *= (1 - cost_increase / 100)
    stressed["cash_flow"] *= (1 - cost_increase / 100)

    return stressed
