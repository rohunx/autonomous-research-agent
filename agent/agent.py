from agent.planner import Planner
from agent.executor import Executor
from agent.memory import Memory
from agent.tools import SearchTool, AnalysisTool
from config.settings import MAX_ITERATIONS

class ResearchAgent:
    def __init__(self, objective):
        self.objective = objective
        self.memory = Memory()

        self.tools = [
            SearchTool(),
            AnalysisTool()
        ]

        self.planner = Planner(self.tools)
        self.executor = Executor(self.tools)

    def run(self):
        for step in range(MAX_ITERATIONS):
            retrieved_context = self.memory.search(self.objective)

            action = self.planner.plan(
                self.objective,
                retrieved_context
            )

            result = self.executor.execute(action)

            self.memory.add(result)

            print(f"\n[Step {step + 1}]")
            print("Action:", action)
            print("Result:", str(result)[:500])

