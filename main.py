from langgraph.graph import StateGraph, END
from schemas.state_schema import GraphState
from agents.research_agent import search_node
from agents.answer_agent import answer_node

def build_graph():
    """
    Constructs and compiles the LangGraph with two primary agents:
    - search_node: Handles web search using Tavily.
    - answer_node: Generates a response based on search results using LLM.
    
    """

    # Initializing the stateful graph .
    workflow = StateGraph(GraphState)
    
    # Processing nodes
    workflow.add_node("search", search_node)
    workflow.add_node("answer", answer_node)

    # flow between nodes

    workflow.set_entry_point("search")
    workflow.add_edge("search", "answer")
    workflow.add_edge("answer", END)

    # Finalized graph
    return workflow.compile()
