def calculate_cac(marketing_spend, new_customers):
    if new_customers == 0:
        return 0
    return marketing_spend / new_customers

def calculate_ltv(avg_order_value, purchase_frequency, customer_lifetime):
    return avg_order_value * purchase_frequency * customer_lifetime

def calculate_contribution_margin_per_customer(revenue_per_customer, variable_cost_per_customer):
    return revenue_per_customer - variable_cost_per_customer

def calculate_payback_period(cac, contribution_margin):
    if contribution_margin == 0:
        return float('inf')
    return cac / contribution_margin

def calculate_breakeven_volume(fixed_costs, contribution_margin_per_unit):
    if contribution_margin_per_unit == 0:
        return float('inf')
    return fixed_costs / contribution_margin_per_unit