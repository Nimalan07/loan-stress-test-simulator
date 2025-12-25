def apply_stress(data, rate_shock, revenue_drop, cost_increase):
    stressed = data.copy()
    stressed["interest_rate"] += rate_shock
    stressed["revenue"] *= (1 - revenue_drop / 100)
    stressed["ebitda"] *= (1 - cost_increase / 100)
    stressed["cashflow"] *= (1 - cost_increase / 100)
    return stressed
