from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatRequest
from app.core.bedrock_client import bedrock_runtime
from app.core.config import settings

router = APIRouter()


@router.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    def generate():
        response = bedrock_runtime.converse_stream(
            modelId=settings.BEDROCK_MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [{"text": request.query}],
                }
            ],
            inferenceConfig={"maxTokens": 400, "temperature": 0.7, "topP": 0.9},
        )

        stream = response.get("stream")
        for event in stream:
            if "contentBlockDelta" in event:
                text = event["contentBlockDelta"]["delta"].get("text", "")
                if text:
                    yield text

    return StreamingResponse(generate(), media_type="text/event-stream")
