from google import genai

from src.config import GEMINI_API_KEY
from src.database import query_historic_facts
from src.search import get_live_news_context
from src.prompt import QUIZ_PROMPT



client = genai.Client(api_key=GEMINI_API_KEY)


def generate_quiz(sport, difficulty, num_questions=4):
    """
    Generates sports quizzes using ChromaDB + Web Search + Gemini.
    """

    history = query_historic_facts(
        sport=sport,
        query_text=f"{sport} history achievements"
    )

    news = get_live_news_context(sport)

    prompt = QUIZ_PROMPT.format(
        sport=sport,
        difficulty=difficulty,
        num_questions=num_questions,
        history="\n".join(history),
        news=news
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    

    return response.text
