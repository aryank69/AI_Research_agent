from langchain.tools import Tool

def search_tool():
    def search(query):
        return f"Simulated external search results for: {query}"

    return Tool(
        name="Search Tool",
        func=search,
        description="Useful for answering general knowledge queries"
    )