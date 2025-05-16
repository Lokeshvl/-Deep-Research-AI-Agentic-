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
- LLM APIs (Gemini or compatible)

---
# Clone the repo
git clone (https://github.com/Lokeshvl/-Deep-Research-AI-Agentic-.git)
cd -Deep-Research-AI-Agentic-

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up your environment
cp .env.example .env
# Then edit `.env` to add your API keys

# Launch the Streamlit app
streamlit run app.py

Deep_Research-AI-Agent/
├── main.py                  # Streamlit frontend
├── agents/
│   ├── research_agent.py   # Info-gathering logic
│   └── answer_agent.py     # Answer generation
├── .env.example            # Environment variable template

## 🚀 How It Works

```mermaid
graph LR
    A[User Query] --> B[ResearchAgent]
    B --> C[AnswerAgent]
    C --> D[Streamlit Output]


