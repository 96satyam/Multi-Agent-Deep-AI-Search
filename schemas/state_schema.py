from typing import TypedDict, Optional

class GraphState(TypedDict, total=False):
    """
    Represents the state carried across the nodes in the LangGraph.
    
    """
    question: str                        
    search_result: Optional[str]         
    final_answer: Optional[str]          
