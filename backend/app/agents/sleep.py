from app.core.llm import llm_call
from app.agents.context import get_health_context

def sleep_agent():
    health_context = get_health_context()

    prompt = f"""
    You are a sleep health specialist AI.

    From the health summary below:
    1. Analyze sleep quality and duration
    2. Identify sleep-related risks
    3. Suggest sleep improvement strategies
    4. Recommend ideal sleep duration

    HEALTH SUMMARY:
    {health_context}

    Be practical and evidence-based.
    """

    return llm_call(prompt)
