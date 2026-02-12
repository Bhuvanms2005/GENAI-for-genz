from fastapi import APIRouter
from app.ingestion.mock_loader import load_health_data
from app.memory.scaledown import structured_scaledown

from app.agents.nutrition import nutrition_agent
from app.agents.exercise import exercise_agent
from app.agents.sleep import sleep_agent
from app.agents.goals import goal_agent
from app.agents.doctor import doctor_agent
from app.agents.anomaly import anomaly_agent

router = APIRouter(prefix="/chat")

@router.get("/summary")
def summary():
    data = load_health_data()
    compressed = structured_scaledown(data)
    return {
        "compressed_health_summary": compressed,
        "original_entries": len(data)
    }

@router.get("/nutrition")
def nutrition():
    return {"response": nutrition_agent()}

@router.get("/exercise")
def exercise():
    return {"response": exercise_agent()}

@router.get("/sleep")
def sleep():
    return {"response": sleep_agent()}

@router.get("/goals")
def goals():
    return {"response": goal_agent()}

@router.get("/doctor")
def doctor():
    return {"response": doctor_agent()}
@router.get("/anomalies")
def anomalies():
    return anomaly_agent()
@router.get("/progress")
def progress():
    return {
        "progress_summary": {
            "sleep_consistency": "Improving",
            "activity_level": "Moderate",
            "nutrition_balance": "Needs improvement",
            "overall_score": 72
        }
    }
