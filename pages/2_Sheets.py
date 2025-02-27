# st.set_page_config(page_title="Dataframes", page_icon="📊")


import streamlit as st
st.header("Dataframes")

def render_dataframes():
    if "result" not in st.session_state:
        st.error("No result found in session state.")
        return

    result = st.session_state["result"]

    st.subheader("Financial Metrics:")


    financial_metrics = result.get("financial_metrics", {})
    st.write(f"Revenue (Sales): {financial_metrics.get('Revenue (Sales)', 'N/A')}")
    st.write(f"Net Income: {financial_metrics.get('Net Income', 'N/A')}")
    st.write(f"EBITDA: {financial_metrics.get('EBITDA', 'N/A')}")
    st.write(f"Gross Margin: {financial_metrics.get('Gross Margin', 'N/A')}")
    st.write(f"Operating Margin: {financial_metrics.get('Operating Margin', 'N/A')}")
    st.write(f"Net Profit Margin: {financial_metrics.get('Net Profit Margin', 'N/A')}")
    st.write(f"Free Cash Flow (FCF): {financial_metrics.get('Free Cash Flow (FCF)', 'N/A')}")
    st.write(f"Debt-to-Equity Ratio: {financial_metrics.get('Debt-to-Equity Ratio', 'N/A')}")
    st.write(f"Current Ratio: {financial_metrics.get('Current Ratio', 'N/A')}")

    st.subheader("Valuation Metrics:")
    valuation_metrics = result.get("valuation_metrics", {})
    st.write(f"Price-to-Earnings Ratio (P/E): {valuation_metrics.get('Price-to-Earnings Ratio (P/E)', 'N/A')}")
    st.write(f"Price-to-Book Ratio (P/B): {valuation_metrics.get('Price-to-Book Ratio (P/B)', 'N/A')}")
    st.write(f"Enterprise Value (EV): {valuation_metrics.get('Enterprise Value (EV)', 'N/A')}")
    st.write(f"EV/EBITDA: {valuation_metrics.get('EV/EBITDA', 'N/A')}")
    st.write(f"Dividend Yield: {valuation_metrics.get('Dividend Yield', 'N/A')}")
    st.write(f"PEG Ratio: {valuation_metrics.get('PEG Ratio', 'N/A')}")

    st.subheader("Operational Metrics:")
    operational_metrics = result.get("operational_metrics", {})
    st.write(f"Return on Equity (ROE): {operational_metrics.get('Return on Equity (ROE)', 'N/A')}")
    st.write(f"Return on Assets (ROA): {operational_metrics.get('Return on Assets (ROA)', 'N/A')}")
    st.write(f"Inventory Turnover: {operational_metrics.get('Inventory Turnover', 'N/A')}")
    st.write(f"Accounts Receivable Turnover: {operational_metrics.get('Accounts Receivable Turnover', 'N/A')}")
    st.write(f"Employee Productivity: {operational_metrics.get('Employee Productivity', 'N/A')}")
    
    st.subheader("Growth Metrics:")
    st.write(f"Revenue Growth Rate: {result.get('growth_metrics', {}).get('Revenue Growth Rate', 'N/A')}")
    st.write(f"Earnings Growth Rate: {result.get('growth_metrics', {}).get('Earnings Growth Rate', 'N/A')}")
    st.write(f"Five Year Revenue Growth Rate: {result.get('growth_metrics', {}).get('Five Year Revenue Growth Rate', 'N/A')}")
    st.write(f"Five Year Earnings Growth Rate: {result.get('growth_metrics', {}).get('Five Year Earnings Growth Rate', 'N/A')}")
    st.write(f"Quarterly Revenue Growth Rate: {result.get('growth_metrics', {}).get('Quarterly Revenue Growth Rate', 'N/A')}")
    st.write(f"Quarterly Earnings Growth Rate: {result.get('growth_metrics', {}).get('Quarterly Earnings Growth Rate', 'N/A')}")

    growth_rates = result.get('growth_metrics', {}).get('Revenue Growth Rates', {})


    st.subheader("Balance Sheet:")
    st.dataframe(result.get("balance_sheet", "N/A"))

    st.subheader("Income Statement:")
    st.dataframe(result.get("income_statement", "N/A"))

    st.subheader("Cash Flow:")
    st.dataframe(result.get("cash_flow", "N/A"))

    st.subheader("Price History:")
    st.dataframe(result.get("price_history"))

render_dataframes()