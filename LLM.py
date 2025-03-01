
from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI

# import openai
# from dotenv import load_dotenv

# openai.api_key=os.getenv("open_ai_api")
# openai.Completion.create(
#     model="gpt-4o-mini",
    
# )



# if not os.environ.get("OPENAI_API_KEY"):
#   os.environ["OPENAI_API_KEY"] = getpass.getpass("enter the api key")



# model = ChatOpenAI(model="gpt-4")

def User_query_processing(user_query):
    parsing_query=f"""
    You are an assistant for financial analysis. Extract the following details from the query in string format:
    which is used to get relavant data from yahoo apis
    match to the revalent company name in india
    - "company": The name of the company.
    "user Query":"{user_query}"
    provide the respone only in string format which used to get data from yahoo apis
    return only company symbol
    """
    return parsing_query


def generate_company_detail_info(company_name, sector, industry, website, description, live_price, pe_ratio):
    prompt = f"""
    The following details describe a company. Use this information to provide an in-depth analysis of the company, including any additional insights from your knowledge base or database:

    - **Company Name**: {company_name}
    - **Sector**: {sector}
    - **Industry**: {industry}
    - **Website**: {website}
    - **Description**: {description}
    - **Live Price**: ${live_price:.2f}
    - **P/E Ratio**: {pe_ratio:.2f}

    Discuss the company's market position, recent trends in its industry, its financial health, and how its P/E ratio compares to competitors. Additionally, provide your insights into the company's future potential and any notable achievements.
    """
    return prompt

def User_query_processing_pe(user_query):
    parsing_query = f"""
    You are an assistant specializing in financial data extraction. Extract the following details 
    from the user's query in JSON format:
    
    - "company": The name of the company mentioned in the query.
    - "metric": The financial metric requested (e.g., P/E ratio).
    - "start_date": The start date for the time period (if mentioned).
    - "end_date": The end date for the time period (if mentioned).
    
    Ensure the response includes:
    - If a date range is not specified, default to "start_date": null and "end_date": null.
    - Provide the response only in JSON format.

    "User Query": "{user_query}"
    """
    return parsing_query


llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0.6,
    groq_api_key="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"
    # other params...
)
