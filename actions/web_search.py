from __future__ import annotations
import json
import traceback
from duckduckgo_search import DDGS
from config.config import Config


def web_search(query: str, num_results: int = Config().num_search_queries) -> str:
    print("Searching with query {0}...".format(query))
    search_results = []

    try:
        ddgs = DDGS()
        results = ddgs.text(query)
        if results is None:
            return json.dumps(search_results)
        elif isinstance(results, str) and results.startswith("Error"):
            return json.dumps(search_results)
            
        # Check if "vqd" is empty or None
        if not ddgs.vqd:
            raise AssertionError("Error in getting vqd")
    except AssertionError as e:
        traceback_str = traceback.format_exc()
        print("Ignoring error:", traceback_str)
        return json.dumps(search_results)
    except Exception as e:
        print("Error occurred:", str(e))
        return json.dumps(search_results)

    total_added = 0
    for j in results:
        search_results.append(j)
        total_added += 1
        if total_added >= num_results:
            break

    return json.dumps(search_results, ensure_ascii=False, indent=4)