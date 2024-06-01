from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 构建model
model = Ollama(model="llama3")

# 构建Prompt Templates
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个{lang}语言的专家"),
        ("user", "{text}"),
    ]
)

# 构建构造OutputParsers
parser = StrOutputParser()

chain = prompt_template | model | parser
res = chain.invoke(
    {
        "lang": "python",
        "text": "写一段最简单的代码",
    },
)

print(res)