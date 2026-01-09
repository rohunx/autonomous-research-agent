from agent.agent import ResearchAgent
from dotenv import load_dotenv
import os


if __name__ == "__main__":
    load_dotenv()
    objective = "Research recent methods for improving transformer efficiency"
    agent = ResearchAgent(objective)
    agent.run()
