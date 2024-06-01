from langchain_community.llms import Ollama

llm = Ollama(model="llama3")
response = llm.invoke("使用中文介绍一下广州")
print(response)