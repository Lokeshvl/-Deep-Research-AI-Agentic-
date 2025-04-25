import streamlit as st
from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents.research_agent import research_agent
from agents.answer_agent import answer_drafter


class ResearchState(TypedDict):
    query: str
    info: str
    answer: str
graph = StateGraph(ResearchState)
graph.add_node("ResearchAgent", research_agent)
graph.add_node("AnswerAgent", answer_drafter)
graph.set_entry_point("ResearchAgent")
graph.add_edge("ResearchAgent", "AnswerAgent")
graph.add_edge("AnswerAgent", END)
graph_executor = graph.compile()

st.set_page_config(page_title="AI Research Assistant", layout="centered")

st.title("AI Research Assistant")
st.markdown("Type your research question and get an AI-powered detailed response.")

query = st.text_input("Enter your research query", placeholder="e.g. What are the latest advancements in quantum computing?")


if st.button("Run Research"):
    if query.strip() == "":
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("Researching your topic..."):
            state = {"query": query, "info": "", "answer": ""}
            result = graph_executor.invoke(state)

        st.success("Research Complete")
        st.subheader("Final Answer")
        st.write(result["answer"])

        # Optional: Show intermediate info
        with st.expander("Research Info Collected"):
            st.write(result["info"])