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


# Clone the repo
git clone https://github.com/yourusername/kairon-langgraph-assistant.git
cd kairon-langgraph-assistant

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Add your API keys to .env
cp .env.example .env
# edit .env and fill in the keys

# Run the app
streamlit run app.py


kairon-langgraph-assistant/
├── main.py                  # Streamlit frontend
├── agents/
│   ├── research_agent.py   # Info-gathering logic
│   └── answer_agent.py     # Answer generation
├── .env.example            # Environment variable template

