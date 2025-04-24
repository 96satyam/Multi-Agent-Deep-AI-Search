import streamlit as st
from main import build_graph

# Streamlit
st.set_page_config(page_title="Multi-Agent Deep AI Search", layout="centered")


st.title(" Deep AI Search Agents using Tavily and LangGraph")


st.markdown("""
    ### Welcome to the Multi-Agent Deep AI Search App!""")

# User Input 
question = st.text_input(
    " What would you like to know?",
    placeholder="e.g., What are the AI agents in LangGraph?",
    label_visibility="collapsed",

)

# Answer
if st.button("Find  Answer") and question:
    with st.spinner(" Agents are searching and crafting an answer..."):
        try:
            # Building the LangGraph and invoking it with the user's question

            graph = build_graph()
            result = graph.invoke({"question": question})

            # The response
            if "final_answer" in result:
                st.success(" Answer crafted successfully!")
                st.markdown("###  Final Answer :")
                st.write(result["final_answer"])

                # Optionally show raw search results for transparency

                if "search_result" in result:
                    with st.expander(" You can view Raw Search Results here"):
                        st.code(result["search_result"], language="markdown")
            else:
                st.warning("No final answer was generated. Please try again.")

        except Exception as e:
            st.error("Something unexpected happened.")
            st.exception(e)

# --- Footer Section ---
st.markdown("---")
st.caption("Built by Satyam Tiwari  using LangGraph, LangChain, and Streamlit.")
st.caption("Thanks for providing this opportunity to build this app!")