from assistant.chains.retrieval import AssistantChain
from assistant.vector_stores.pinecone import build_retriever
from assistant.llms.chatgpt import build_llm

def build_assistant():
    retriever = build_retriever()
    llm = build_llm("gpt-4")
    memory = None

    return AssistantChain.from_llm(
        llm=llm,
        memory=memory,
        retriever=retriever
    )