

import streamlit as st

def render_graphs():
    if "result" not in st.session_state:
        st.error("No result found in session state.")
        return

    result = st.session_state["result"]

    # Display price chart
    st.write("### Stock Price History")
    price_history = result.get("price_history")
    if price_history is not None:
        st.line_chart(price_history["Close"])
    else:
        st.write("Price history data is not available.")

    # Revenue and Net Income Trends
    st.write("### Revenue and Net Income Trends")
    financial_metrics = result.get("financial_metrics", {})
    revenue_history = financial_metrics.get("Revenue History", None)
    net_income_history = financial_metrics.get("Net Income History", None)
    if revenue_history is not None and net_income_history is not None:
        st.line_chart({"Revenue": revenue_history, "Net Income": net_income_history})
    else:
        st.write("Revenue and Net Income data are not available.")

    # Gross Margin and Profit Margin Trends
    st.write("### Gross Margin and Profit Margin Trends")
    gross_margin_history = financial_metrics.get("Gross Margin History", None)
    profit_margin_history = financial_metrics.get("Profit Margin History", None)
    if gross_margin_history is not None and profit_margin_history is not None:
        st.line_chart({"Gross Margin (%)": gross_margin_history, "Profit Margin (%)": profit_margin_history})
    else:
        st.write("Gross Margin and Profit Margin data are not available.")

    # Balance Sheet Composition
    st.write("### Balance Sheet Composition")
    balance_sheet = result.get("balance_sheet")
    if balance_sheet is not None:
        st.bar_chart(balance_sheet)  # Assuming balance sheet data is structured appropriately
    else:
        st.write("Balance sheet data is not available.")

    # Cash Flow Analysis
    st.write("### Cash Flow Analysis")
    cash_flow = result.get("cash_flow")
    if cash_flow is not None:
        st.bar_chart(cash_flow)  # Assuming cash flow data is structured appropriately
    else:
        st.write("Cash flow data is not available.")

    # Stock Price with Moving Averages
    st.write("### Stock Price with Moving Averages")
    if price_history is not None:
        st.line_chart({
            "Stock Price": price_history["Close"],
            "50-Day MA": price_history["Close"].rolling(window=50).mean(),
            "200-Day MA": price_history["Close"].rolling(window=200).mean()
        })
    else:
        st.write("Stock price data is not sufficient for moving averages.")
render_graphs()