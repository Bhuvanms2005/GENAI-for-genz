import json

def load_health_data():
    data = []

    for i in range(365):
        entry = {
            "day": i + 1,
            "sleep_hours": 5 + (i % 3) * 0.5,   # 5–6.5 hrs
            "steps": 3000 + (i % 5) * 1000,     # 3000–7000
            "calories": 2200 + (i % 4) * 300,   # 2200–3100
            "heart_rate": 70 + (i % 6) * 3
        }
        data.append(entry)

    return data
