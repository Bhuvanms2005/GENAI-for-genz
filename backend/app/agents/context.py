from app.ingestion.mock_loader import load_health_data
from app.memory.scaledown import structured_scaledown

def get_health_context():
    health_data = load_health_data()
    compressed_summary = structured_scaledown(health_data)
    return compressed_summary
