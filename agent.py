from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from retriever import get_retriever_tool
from tools import search_tool
from memory import get_memory

def build_agent():
    llm = ChatOpenAI(temperature=0)

    tools = [
        search_tool(),
        get_retriever_tool()
    ]

    memory = get_memory()

    agent = initialize_agent(
        tools,
        llm,
        agent="chat-conversational-react-description",
        memory=memory,
        verbose=True
    )

    return agent