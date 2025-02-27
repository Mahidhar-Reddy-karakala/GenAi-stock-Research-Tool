import streamlit as st
import json
from LLM import User_query_processing, llm,generate_company_detail_info
from yahoo import get_data  # Assuming `get_data` is correctly implemented as shown earlier
import matplotlib.pyplot as plt
import pandas as pd

# Set page title and icon
st.set_page_config(
    page_title="StockData.ai",
    page_icon="📈",
)

# st.title("Stock Data")

if "balloons_shown" not in st.session_state:
    st.balloons()
    st.session_state["balloons_shown"] = True

# User input
user_input = st.sidebar.text_input("Enter company name :", "")


# result function
@st.cache_data(show_spinner="Fetching data...")
def res(user_input):
    if user_input:
        try:
            # Process user query
            parsed_query = User_query_processing(user_input)
            response = llm.invoke(parsed_query)
            # response = model.invoke(parsed_query)

            # Clean and parse the response
            output = response.content.strip('"')
            result = get_data(output)
            
            # Save result to session state
            st.session_state["result"] = result
            
            # Fetch data using the cleaned output
            display_company_details(result)
            return result
        except Exception as e:
             st.error(f"An error occurred: {e}")
    elif "result" in st.session_state:
        # Display the previously saved result from session state
        display_company_details(st.session_state["result"])
        return st.session_state["result"]


# Display company details for the res function
@st.cache_data(show_spinner="Fetching data...")
def display_company_details(result):
    st.header(f"Company Name: {result.get('long_name', 'N/A')}")
    st.write(f"Market Cap: {result.get('market_cap', 'N/A')} $B")
    st.write(f"Price: {result.get('live_price', 'N/A')}$")
    st.write(f"Sector:{result.get('sector','N/A')}")
    st.write(f"Industry:{result.get('industry','N/A')}")
    st.write(f"Website:{result.get('web','N/A')}")
    # st.write("Business:")
    # st.write(result.get("longBusinessSummary","N/A"))
    parsed_query_2=generate_company_detail_info(result.get('long_name', 'N/A'),result.get("sector","N/A"),result.get("industry","N/A"),result.get("web","N/A"),result.get("longBusinessSummary","N/A"),result.get('live_price', 'N/A'),result.get('pe_ratio', 'N/A'))
    response2=llm.invoke(parsed_query_2)
    # response2=model.invoke(parsed_query_2)
    st.write(response2.content)

# Call the function with the user input
# result = res(user_input) 
if user_input:
    result = res(user_input)
elif "result" in st.session_state:
    display_company_details(st.session_state["result"])
