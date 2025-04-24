from langchain.tools.tavily_search import TavilySearchResults
from schemas.state_schema import GraphState

tavily = TavilySearchResults()

def fetch_web_results(query: str) -> str:
    try:
        return tavily.run(query)
    except Exception as e:
        
        return f"Search failed due to: {str(e)}"

def search_node(state: GraphState) -> dict:
    user_query = state.get("question", "")
    retrieved_info = fetch_web_results(user_query)
    return {
        "question": user_query,
        "search_result": retrieved_info
    }
