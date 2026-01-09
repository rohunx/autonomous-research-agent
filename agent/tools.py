import requests


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
            description="Search arXiv for recent academic papers and return abstracts"
        )

    def run(self, input_text):
        url = "http://export.arxiv.org/api/query"
        params = {
            "search_query": input_text,
            "start": 0,
            "max_results": 5
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            return "Failed to fetch papers"

        entries = response.text.split("<entry>")[1:]

        papers = []
        for entry in entries:
            title = entry.split("<title>")[1].split("</title>")[0].strip()
            summary = entry.split("<summary>")[1].split("</summary>")[0].strip()
            papers.append(f"Title: {title}\nAbstract: {summary}")

        return papers


class AnalysisTool(Tool):
    def __init__(self):
        super().__init__(
            name="run_analysis",
            description="Run Python-based data analysis or experiments"
        )

    def run(self, input_text):
        return f"Analysis executed with instructions: {input_text}"

