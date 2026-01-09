from agent.planner import Planner
from agent.executor import Executor
from agent.memory import Memory
from config.settings import MAX_ITERATIONS

class ResearchAgent:
    def __init__(self, objective):
        self.objective = objective
        self.planner = Planner()
        self.executor = Executor()
        self.memory = Memory()

    def run(self):
        for step in range(MAX_ITERATIONS):
            plan = self.planner.plan(
                self.objective,
                self.memory.get()
            )

            result = self.executor.execute(plan)

            self.memory.add(f"Step {step+1}: {plan}")
            self.memory.add(f"Result: {result}")

            print(f"\n[Step {step+1}]")
            print("Plan:", plan)
            print("Result:", result)
