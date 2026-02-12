from app.core.llm import llm_call
from app.agents.context import get_health_context

def nutrition_agent():
    health_context = get_health_context()

    prompt = f"""
    You are a professional nutritionist AI.

    Based on the user's long-term health summary below,
    provide:
    1. Key nutrition issues
    2. Daily calorie guidance
    3. Meal planning suggestions
    4. Foods to avoid
    5. Foods to prioritize

    HEALTH SUMMARY:
    {health_context}

    Respond in clear bullet points.
    """

    return llm_call(prompt)
