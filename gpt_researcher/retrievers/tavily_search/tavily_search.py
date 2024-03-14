# Tavily API Retriever

# libraries
import os
from tavily import TavilyClient
from duckduckgo_search import DDGS


class TavilySearch():
    """
    Tavily API Retriever
    """
    def __init__(self, query):
        """
        Initializes the TavilySearch object
        Args:
            query:
        """
        self.query = query
        self.api_key = self.get_api_key()
        self.client = TavilyClient(self.api_key)

    def get_api_key(self):
        """
        Gets the Tavily API key
        Returns:

        """
        # Get the API key
        try:
            api_key = os.environ["TAVILY_API_KEY"]
        except:
            raise Exception("Tavily API key not found. Please set the TAVILY_API_KEY environment variable. "
                            "You can get a key at https://app.tavily.com")
        return api_key
    
    def search(self, max_results=7):
        """
        Searches the query
        Returns:
        """
        try:
            # Search the query using Tavily API
            results = self.client.search(self.query, search_depth="advanced", max_results=max_results)
            # Return the results
            search_response = [{"href": obj["url"], "body": obj["content"]} for obj in results.get("results", [])]
        except Exception as e:
            try:
                # Fallback to DuckDuckGo search
                ddg = DDGS()
                search_response = ddg.text(self.query, region='wt-wt', max_results=max_results)
            except Exception as e:
                # Handle the fallback exception
                print("Fallback search failed:", str(e))
                search_response = []
        return search_response
