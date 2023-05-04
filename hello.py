import os
os.environ["OPENAI_API_KEY"] = "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"
from langchain.llms import OpenAI

#llm = OpenAI(temperature=0.9)

#text = "What are some of the famous dishes made from pasta"
#print(llm(text))

from langchain.prompts import PromptTemplate

#prompt = PromptTemplate(
#    input_variables=["food"],
#    template="What are 5 countries when you think of {food}?",
#)

#print(prompt.format(food="salad"))

#print(llm(prompt.format(food="curry")))

from langchain.agents import load_tools
from langchain.agents import initialize_agent

llm = OpenAI(temperature=0)

os.environ["SERPAPI_API_KEY"]="9b6d38f8be21c4345ff295ea0e5d020d05cfecb189e76ed19b8881e5f7459557"

tools= load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

agent.run("Who is Manchested United Playing Next? What is the predicted score?")



