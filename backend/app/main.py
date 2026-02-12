from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routes.chat import router as chat_router

app = FastAPI(title="Personal Health Coach AI")

# ✅ CORS CONFIGURATION
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ GLOBAL ERROR HANDLER (VERY IMPORTANT)
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    message = str(exc)

    # Handle Gemini quota errors gracefully
    if "Gemini API error 429" in message:
        return JSONResponse(
            status_code=200,
            content={
                "warning": "AI quota temporarily exceeded",
                "message": "Using last known health insights. Please retry shortly."
            },
        )

    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "details": message},
    )

# ✅ ROUTES
app.include_router(chat_router)

# ✅ ROOT HEALTH CHECK
@app.get("/")
def root():
    return {"status": "Health AI Coach running"}
