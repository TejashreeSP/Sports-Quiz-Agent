from ddgs import DDGS


def get_live_news_context(sport_name):
    """
    Fetches recent sports information using DuckDuckGo Search.
    """

    search_query = (
        f"{sport_name} latest tournament winners championship news"
    )

    retrieved_text = []

    try:
        with DDGS() as ddgs:

            results = ddgs.text(
                search_query,
                max_results=3
            )

            for index, result in enumerate(results, start=1):

                title = result.get("title", "")
                body = result.get("body", "")

                retrieved_text.append(
                    f"Source {index}\n"
                    f"Title: {title}\n"
                    f"Snippet: {body}"
                )

    except Exception as error:

        return f"Web Search Error: {error}"

    return "\n\n".join(retrieved_text)