import yfinance as yf
import pandas as pd
import yahoo
import streamlit as st
def get_data(ticker):
    result = {}
    # Fetch historical data
    stock_data = yf.download(ticker,start="2020-12-24",end="2024-12-24")
    result["stock_data"] = stock_data
    # Fetch company financial data
    stock_info = yf.Ticker(ticker)
    pe_ratio = stock_info.info.get("trailingPE", None)  # Get trailing P/E ratio if available
    
    result["pe_ratio"] = pe_ratio
    #live price
    live_price = stock_info.history(period="1d").get("Close", pd.Series()).iloc[-1] if not stock_info.history(period="1d").empty else None
    result["live_price"] = live_price

    #info
    info=stock_info.info
    mktCap=info.get("marketCap", None)
    result["market_cap"] = (mktCap/(10**9))
    result["long_name"] = info.get("longName", "Unknown Company")

    result["balance_sheet"] = stock_info.balance_sheet
    result["income_statement"] = stock_info.financials
    result["cash_flow"] = stock_info.cashflow
    result["dividends"] = stock_info.dividends
    result["splits"] = stock_info.splits
    result["price_history"] = stock_info.history(period="1y")
    company_info=stock_info.info
    result["sector"]=company_info.get("sector", "N/A")
    result["industry"]=company_info.get("industry", "N/A")
    result["web"]=company_info.get("website", "N/A")
    result["longBusinessSummary"]=company_info.get("longBusinessSummary", "N/A")
    result["finacial_metrics"]=financial_metrics(ticker)
    result["finacial_metrics"]=financial_metrics(ticker)
    result["valuation_metrics"]=valution_metrics(ticker)
    result["operational_metrics"]=operational_metrics(ticker)
    result["growth_metrics"]=growth_metrics(ticker)
    
    return result

def get_financial_metrics(info):
    financial_metrics = {
        "Revenue (Sales)": info.get("totalRevenue"),
        "Net Income": info.get("netIncomeToCommon"),
        "EBITDA": info.get("ebitda"),
        "Gross Margin": info.get("grossMargins"),
        "Operating Margin": info.get("operatingMargins"),
        "Net Profit Margin": info.get("profitMargins"),
        "Free Cash Flow (FCF)": info.get("freeCashflow"),
        "Debt-to-Equity Ratio": info.get("debtToEquity"),
        "Current Ratio": info.get("currentRatio"),
    }
    return financial_metrics

def financial_metrics(symbol):
    # Create Ticker object
    ticker_symbol = symbol  # Example: Apple Inc.
    ticker = yf.Ticker(ticker_symbol)

    # Extract Financial Metrics
    info = ticker.info
    financial_metrics = get_financial_metrics(info)

    return financial_metrics

def valution_metrics(symbol):
    # Create Ticker object
    ticker_symbol = symbol  # Example: Apple Inc.
    ticker = yf.Ticker(ticker_symbol)

    # Extract Valuation Metrics
    info = ticker.info
    valuation_metrics = {
        "Price-to-Earnings Ratio (P/E)": info.get("trailingPE"),
        "Price-to-Book Ratio (P/B)": info.get("priceToBook"),
        "Enterprise Value (EV)": info.get("enterpriseValue"),
        "EV/EBITDA": info.get("enterpriseToEbitda"),
        "Dividend Yield": info.get("dividendYield"),
        "PEG Ratio": info.get("pegRatio"),
    }

    return valuation_metrics
def operational_metrics(symbol):
    # Create Ticker object
    ticker_symbol = symbol  # Example: Apple Inc.
    ticker = yf.Ticker(ticker_symbol)

    # Extract Operational Metrics
    info = ticker.info
    operational_metrics = {
        "Return on Equity (ROE)": info.get("returnOnEquity"),
        "Return on Assets (ROA)": info.get("returnOnAssets"),
        "Inventory Turnover": None,  # Requires custom calculation from financial data
        "Accounts Receivable Turnover": None,  # Requires revenue and receivables
        "Employee Productivity": None,  # Requires revenue and employee count
    }

    return operational_metrics
def growth_metrics(symbol):
    # Create Ticker object
    ticker_symbol = symbol  # Example: Apple Inc.
    ticker = yf.Ticker(ticker_symbol)

    # Extract Growth Metrics
    info = ticker.info
    growth_metrics = {
        "Revenue Growth Rate": info.get("revenueGrowth"),
        "Earnings Growth Rate": info.get("earningsGrowth"),
        "Five Year Revenue Growth Rate": info.get("fiveYearAvgRevenueGrowth"),
        "Five Year Earnings Growth Rate": info.get("fiveYearAvgEarningsGrowth"),
        "Quarterly Revenue Growth Rate": info.get("quarterlyRevenueGrowth"),
        "Quarterly Earnings Growth Rate": info.get("quarterlyEarningsGrowth"),
    }
    return growth_metrics

