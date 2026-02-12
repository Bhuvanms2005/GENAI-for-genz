from app.ingestion.mock_loader import load_health_data
from app.core.llm import llm_call

def anomaly_agent():
    data = load_health_data()

    if not data or not isinstance(data[0], dict):
        return {"error": "Health data not in expected format"}

    alerts = []

    avg_sleep = sum(d["sleep_hours"] for d in data) / len(data)
    avg_steps = sum(d["steps"] for d in data) / len(data)
    avg_calories = sum(d["calories"] for d in data) / len(data)

    if avg_sleep < 6:
        alerts.append("Consistently low sleep duration (<6 hours)")

    if avg_steps < 5000:
        alerts.append("Low daily physical activity (steps below 5000)")

    if avg_calories > 2800:
        alerts.append("High average calorie intake")

    if not alerts:
        return {"status": "No major health anomalies detected"}

    prompt = f"""
    You are a health risk analysis AI.

    The following health anomalies were detected:
    {alerts}

    Explain the risks and suggest corrective actions.
    """

    explanation = llm_call(prompt)

    return {
        "detected_anomalies": alerts,
        "analysis": explanation
    }
