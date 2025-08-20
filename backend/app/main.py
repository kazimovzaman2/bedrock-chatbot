from fastapi import FastAPI
from app.api.routes import router
from datetime import datetime, timezone


app = FastAPI(title="RAG Chatbot Backend")


app.include_router(router, prefix="/api")

START_TIME = datetime.now(timezone.utc)


@app.get("/health")
async def health_check():
    uptime_seconds = (datetime.now(timezone.utc) - START_TIME).total_seconds()
    return {
        "status": "ok",
        "message": "Backend is running",
        "uptime_seconds": int(uptime_seconds),
    }
