from app.core.llm import llm_call
from app.agents.context import get_health_context

def exercise_agent():
    health_context = get_health_context()

    prompt = f"""
    You are a certified fitness coach AI.

    Based on the user's health summary below:
    1. Identify activity level
    2. Recommend a weekly workout plan
    3. Suggest intensity (low/moderate/high)
    4. Mention recovery considerations

    HEALTH SUMMARY:
    {health_context}

    Keep recommendations realistic and safe.
    """

    return llm_call(prompt)
