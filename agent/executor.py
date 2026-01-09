class Executor:
    def __init__(self, tools):
        self.tools = {tool.name: tool for tool in tools}

    def execute(self, action):
        tool_name = action["tool"]
        tool_input = action["input"]

        if tool_name not in self.tools:
            return f"Unknown tool: {tool_name}"

        return self.tools[tool_name].run(tool_input)
