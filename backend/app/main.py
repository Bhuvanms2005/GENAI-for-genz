from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(title="Personal Health Coach AI")

app.include_router(chat_router)

@app.get("/")
def root():
    return {"status": "Health AI Coach running"}
