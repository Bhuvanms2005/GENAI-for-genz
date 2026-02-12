from app.core.llm import llm_call
from app.agents.context import get_health_context

def goal_agent():
    health_context = get_health_context()

    prompt = f"""
    You are a health goal-setting AI.

    Using the health summary below:
    1. Identify top 3 health priorities
    2. Define SMART health goals
    3. Suggest measurable progress indicators
    4. Recommend a 30-day improvement plan

    HEALTH SUMMARY:
    {health_context}

    Make goals achievable and motivating.
    """

    return llm_call(prompt)
