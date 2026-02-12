from app.core.llm import llm_call
from app.agents.context import get_health_context

def doctor_agent():
    health_context = get_health_context()

    prompt = f"""
    You are a medical assistant AI preparing a user for a doctor visit.

    Based on the health summary below:
    1. List key symptoms or concerns
    2. Highlight abnormal trends
    3. Suggest questions to ask the doctor
    4. Summarize lifestyle factors affecting health

    HEALTH SUMMARY:
    {health_context}

    Keep it concise and professional.
    """

    return llm_call(prompt)
