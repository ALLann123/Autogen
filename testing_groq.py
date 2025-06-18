#!/usr/bin/python3
import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv() 

#configure
config_list=[{
    "model":  "llama-3.3-70b-versatile",
    "api_key":os.getenv("GROQ_API"),
    "api_type":"groq"
}]


#create an AI assistant
assistant=AssistantAgent(
    name="groq_Assistant",
    system_message="You are a helpful AI assistant.",
    llm_config={"config_list":config_list}
)

#create a user proxy agent(no code execution in this example)
user_proxy=UserProxyAgent(
    name="user_proxy",
    code_execution_config=False
)

#start a conversation between agents
user_proxy.initiate_chat(
    assistant,
    message="Hey"
)
