import streamlit as st
from utils import (
    calculate_cac,
    calculate_ltv,
    calculate_contribution_margin_per_customer,
    calculate_payback_period,
    calculate_breakeven_volume,
)

st.set_page_config(page_title="Startup Unit Economics Analyzer", layout="centered")

st.title("📊 Startup Unit Economics Analyzer")
st.markdown("Analyze key metrics like **CAC, LTV, Payback Period**, and more to evaluate business viability.")

st.header("🔢 Input Parameters")

col1, col2 = st.columns(2)

with col1:
    marketing_spend = st.number_input("Total Marketing Spend (₹)", min_value=0.0, step=1000.0)
    new_customers = st.number_input("New Customers Acquired", min_value=1, step=1)
    avg_order_value = st.number_input("Average Order Value (₹)", min_value=0.0, step=10.0)
    purchase_frequency = st.number_input("Purchase Frequency (per month)", min_value=0.0, step=0.1)

with col2:
    customer_lifetime = st.number_input("Customer Lifetime (in months)", min_value=1, step=1)
    revenue_per_customer = st.number_input("Revenue per Customer (₹)", min_value=0.0, step=10.0)
    variable_cost_per_customer = st.number_input("Variable Cost per Customer (₹)", min_value=0.0, step=10.0)
    fixed_costs = st.number_input("Monthly Fixed Costs (₹)", min_value=0.0, step=1000.0)

# 🧮 Calculations
cac = calculate_cac(marketing_spend, new_customers)
ltv = calculate_ltv(avg_order_value, purchase_frequency, customer_lifetime)
contribution_margin = calculate_contribution_margin_per_customer(revenue_per_customer, variable_cost_per_customer)
payback_period = calculate_payback_period(cac, contribution_margin)
breakeven_volume = calculate_breakeven_volume(fixed_costs, contribution_margin)

# 📊 Output Section
st.header("📈 Results")

st.metric("Customer Acquisition Cost (CAC)", f"₹{cac:.2f}")
st.metric("Lifetime Value (LTV)", f"₹{ltv:.2f}")
st.metric("Contribution Margin", f"₹{contribution_margin:.2f}")
st.metric("Payback Period (months)", f"{payback_period:.2f}")
st.metric("Break-even Volume (customers)", f"{breakeven_volume:.0f}")

st.markdown("---")
st.caption("Made with ❤️ for startup founders and consulting case prep.")
import matplotlib.pyplot as plt

st.subheader("📉 Payback Timeline Simulation")

if contribution_margin > 0:
    months = list(range(1, int(customer_lifetime)+1))
    cumulative_contribution = [i * contribution_margin for i in months]
    cac_line = [cac] * len(months)

    fig, ax = plt.subplots()
    ax.plot(months, cumulative_contribution, label="Cumulative Contribution", color="green")
    ax.plot(months, cac_line, label="CAC", linestyle="--", color="red")
    ax.set_xlabel("Months")
    ax.set_ylabel("₹")
    ax.set_title("Payback Period Visualization")
    ax.legend()
    st.pyplot(fig)
else:
    st.info("Cannot simulate payback timeline — Contribution Margin is 0 or less.")

