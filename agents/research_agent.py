from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()


tavily_cl = TavilyClient(api_key=os.getenv("TAVILY_API"))

def research_agent(state):
    query = state["query"]

    print(f"Researching: {query}")
    response = tavily_cl.search(query=query, max_results=5)
    results = [ f"Title: {r['title']}\nURL: {r['url']}\nContent: {r['content']}"
              for r in response["results"] ]

    collected_info = "\n\n".join(results)
    return {"info": collected_info, "query": query}
