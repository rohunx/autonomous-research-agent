import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

class Planner:
    def __init__(self, tools):
        self.tools = tools
        self.llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    def plan(self, objective, history):
        tool_descriptions = "\n".join(
            [f"{t.name}: {t.description}" for t in self.tools]
        )

        messages = [
            SystemMessage(
                content="You are an autonomous research agent. "
                        "You must choose the best tool for the task."
            ),
            HumanMessage(
                content=f"""
                    Objective:
                    {objective}
                    
                    Previous actions:
                    {history}
                    
                    Available tools:
                    {tool_descriptions}
                    
                    Respond ONLY in valid JSON with this format:
                    {{
                      "tool": "<tool_name>",
                      "input": "<tool_input>"
                    }}
                    """
            )
        ]

        response = self.llm.invoke(messages)

        return json.loads(response.content)
