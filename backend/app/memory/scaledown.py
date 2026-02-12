from app.core.llm import llm_call

def structured_scaledown(health_data) -> str:
    # ✅ FIX: handle both list and dict input safely
    if isinstance(health_data, list):
        logs = health_data
    else:
        logs = health_data.get("daily_logs", [])

    raw_text = ""
    for d in logs:
        raw_text += (
            f"Date: {d.get('date')}, "
            f"Steps: {d.get('steps')}, "
            f"Sleep: {d.get('sleep_hours')}h, "
            f"Calories: {d.get('calories')}, "
            f"HR: {d.get('heart_rate_avg')}\n"
        )

    prompt = f"""
    You are a medical health analysis AI.

    Given long-term daily health logs, generate a compressed
    health memory including:
    - Activity trends
    - Sleep patterns
    - Nutrition behavior
    - Cardiovascular signals
    - Risks & improvements

    Keep under 250 words.

    DATA:
    {raw_text}
    """

    return llm_call(prompt)
