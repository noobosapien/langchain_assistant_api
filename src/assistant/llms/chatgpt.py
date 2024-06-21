from langchain.chat_models import ChatOpenAI

def build_llm(model):
    return ChatOpenAI(
        model_name=model
    )