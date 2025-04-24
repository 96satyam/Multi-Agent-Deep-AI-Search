from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from utils.prompt import answer_prompt
from schemas.state_schema import GraphState

# LLM 

ai_model = ChatOpenAI(
    temperature=0.2, 
    model="gpt-3.5-turbo", 
    max_tokens=2000
)

response_chain = LLMChain(llm=ai_model, prompt=answer_prompt)

def answer_node(state: GraphState) -> dict:
    query_text = state.get("question", "")
    web_context = state.get("search_result", "")

    if not web_context:
        return {"final_answer": " No data available from search."}

    try:
        response = response_chain.run({
            "question": query_text,
            "search_result": web_context
        })
    except Exception as e:
        response = f" Failed to generate answer due to: {str(e)}"

    return {"final_answer": response}
