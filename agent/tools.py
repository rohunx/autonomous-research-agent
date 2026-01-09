class Tool:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def run(self, input_text):
        raise NotImplementedError


class SearchTool(Tool):
    def __init__(self):
        super().__init__(
            name="search_literature",
            description="Search for relevant academic papers and articles"
        )

    def run(self, input_text):
        return f"Search results for query: {input_text}"


class AnalysisTool(Tool):
    def __init__(self):
        super().__init__(
            name="run_analysis",
            description="Run Python-based data analysis or experiments"
        )

    def run(self, input_text):
        return f"Analysis executed with instructions: {input_text}"

