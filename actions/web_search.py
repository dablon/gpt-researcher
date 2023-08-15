from __future__ import annotations
import json
import traceback
from duckduckgo_search import DDGS
from config.config import Config

def web_search(query: str, num_results: int = Config().num_search_queries) -> str:
    """Useful for general internet search queries."""
    print("Searching with query {0}...".format(query))
    search_results = []

    try:
        results = ddgs.text(query)
        results = list(results)
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("Error occurred while searching:")
        print(traceback_str)
        return json.dumps(search_results)

    if results is None:
        print("No results found.")
        return json.dumps(search_results)

    total_added = 0
    for j in results:
        search_results.append(j)
        total_added += 1
        if total_added >= num_results:
            break

    return json.dumps(search_results, ensure_ascii=False, indent=4)
