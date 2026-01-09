from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage


class Planner:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    def plan(self, objective, history):
        messages = [
            SystemMessage(content="You are a research planning assistant."),
            HumanMessage(
                content=f"""
                    Objective:
                    {objective}

                    Previous actions:
                    {history}

                    What should be the next action?
                    Respond with a single sentence.
                """
            ),
        ]

        response = self.llm.invoke(messages)  # ← Fixed line
        return response.content.strip()