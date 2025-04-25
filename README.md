# 🧠 LangGraph Research Assistant using Streamlit

A multi-agent research assistant built using **LangGraph**, deployed with **Streamlit**, designed to take a user query, conduct contextual research, and return a coherent answer.

---

## 🔥 Features

- 🌐 ResearchAgent: Gathers relevant data for a given query.
- ✍️ AnswerAgent: Drafts a human-readable response.
- 🔄 Stateful processing: Powered by LangGraph's state machine.
- 💻 Clean UI: Built with Streamlit.
- 🔐 `.env` support for secure key management.

---

## 📦 Tech Stack

- Python
- LangGraph
- Streamlit
- dotenv
- LLM APIs (OpenAI or compatible)

---

## 🚀 How It Works

```mermaid
graph LR
    A[User Query] --> B[ResearchAgent]
    B --> C[AnswerAgent]
    C --> D[Streamlit Output]
