from langchain.agents import load_tools
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
import os

os.environ['OPENAI_API_KEY']="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"
os.environ['SERPAPI_API_KEY']="9b6d38f8be21c4345ff295ea0e5d020d05cfecb189e76ed19b8881e5f7459557"

llm = OpenAI(temperature=0)
tool_name = ["serpapi"]
tools = load_tools(tool_name)

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
agent.run("What is LangChain?")

