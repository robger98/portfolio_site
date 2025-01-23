from langchain_openai import ChatOpenAI
# from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from rich import print
from typing import List
import getpass
import os
from .data_model.models import Message

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass(prompt="Enter your OpenAI API key: ")

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

def convert_to_langchain_msg_types(chat_history: List[Message]):
    output = []
    for message in chat_history:
        if message.role == 'assistant':
            output.append(AIMessage(message.content))
        else:
            output.append(HumanMessage(message.content))
    return output

def simple_response_chain(messages: List[Message]):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant. Please respond to the following messages as if you were a helpful assistant.",
            ),
            ("human", "{input}"),
        ]
    )

    # contextualize_q_system_prompt = (
    #     "Given a chat history, rephrase on the human question. Do NOT answer the question, only rephrase. Additionally, your response should only include the rephraseded question, with no explaination or pleasantries. The chat history is as follows:"
    # )

    contextualize_q_system_prompt = (
        "You are a helpful assistant. Given a chat history and a user input, " 
        "please respond to the human input as if you were a helpful assistant. "
        "Always respond in proper markdown format"
    )

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    chain = contextualize_q_prompt | llm 
    temp = chain.invoke({'input': messages[-1].content, 'chat_history': convert_to_langchain_msg_types(messages[:-1])})
    print(temp)
    return Message(role='assistant', content=temp.content)

def send(messages: List[Message]):
    return simple_response_chain(messages)
