from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def answer_drafter(state):
    info = state["info"]
    query = state["query"]

    prompt = f""" You are a helpful research assistant.
                 Query: {query}
                 Based on the info below, write a clear and concise answer.
                 Information: {info}
                 Answer:
                """

    response = client.models.generate_content(model="gemini-2.0-flash",contents=prompt)
    return {"answer": response.text}