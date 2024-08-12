# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     model
   Description :
   Author :        xiao_liu
   date：          2024/8/12 22:32
-------------------------------------------------
"""
__author__ = 'xiao_liu'

from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class Master:
    def __init__(self):
        self.chatmodel = ChatOpenAI(
            temperature=0.95,
            model="glm-4",
            streaming=True,
            openai_api_key="0481ff5191ecdef1e90e9a7f33e9a507.mQo8gNetWc29IpiG",
            openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
        )
        self.MEMORY_KEY = "chat_history"
        self.SYSTEMPL = ""
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "你是一个助手"
                ),
                (
                    "user",
                    "{input}"
                ),
                MessagesPlaceholder(variable_name="agent_scratchpad")
            ],
        )
        self.memory = ""
        agent = create_openai_tools_agent(
            self.chatmodel,
            tools=[],
            prompt=self.prompt
        )
        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=[],
            verbose=True
        )

    def run(self, query):
        result = self.agent_executor.invoke({"input": query})
        return result
