from app.core.llm import llm_call

def structured_scaledown(health_data: dict) -> str:
    logs = health_data["daily_logs"]

    raw_text = ""
    for d in logs:
        raw_text += (
            f"Date: {d['date']}, "
            f"Steps: {d['steps']}, "
            f"Sleep: {d['sleep_hours']}h, "
            f"Calories: {d['calories']}, "
            f"HR: {d['heart_rate_avg']}\n"
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
