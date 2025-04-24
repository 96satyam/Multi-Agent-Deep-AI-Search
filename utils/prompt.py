from langchain.prompts import PromptTemplate

answer_prompt = PromptTemplate(
    input_variables=["search_result", "question"],
    template="""
You are a highly intelligent assistant. Based on the following search results, craft a well-structured and informative answer to the question. Make sure to provide a clear, concise, and insightful response, utilizing all relevant information from the search results. If the answer is not fully clear, mention any uncertainties or areas that require further exploration.

--- Search Results ---
{search_result}

--- Question ---
{question}

--- Answer (Provide a detailed and well-thought-out response):"""
)
