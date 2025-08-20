# Bedrock Chatbot Backend

A FastAPI-powered backend service that provides streaming chat capabilities for the Bedrock Chatbot application. This service handles real-time conversation processing and exposes RESTful APIs for seamless frontend integration.

## 🚀 Features

- **High-Performance API**: Built with FastAPI for optimal performance and automatic OpenAPI documentation
- **Streaming Responses**: Real-time chat streaming for enhanced user experience
- **Containerized Deployment**: Docker and Docker Compose support for consistent environments
- **Configuration Management**: Environment-based configuration with `.env` file support
- **Development Ready**: Hot-reload capabilities for efficient development workflow

## 📋 Prerequisites

- **Python**: 3.12 or higher
- **Docker**: Latest stable version (optional, for containerized deployment)
- **Docker Compose**: V2+ (optional, for orchestrated deployment)

## 🛠 Installation & Setup

### Local Development Setup

1. **Clone and Navigate**

   ```bash
   git clone https://github.com/kazimovzaman2/bedrock-chatbot
   cd backend
   ```

2. **Create Virtual Environment**

   ```bash
   # Create virtual environment
   python -m venv .venv

   # Activate virtual environment
   # On Linux/macOS:
   source .venv/bin/activate

   # On Windows:
   .venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   uv sync
   ```

4. **Configure Environment**

   Create a `.env` file in the backend directory:

   ```env
   # Required API Configuration
   AWS_ACCESS_KEY=your_access_key_here
   AWS_SECRET_ACCESS_KEY=your_secret_key_here
   AWS_REGION=your_aws_region_here
   BEDROCK_MODEL_ID=your_bedrock_model_id_here
   ```

5. **Start Development Server**

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

   🌐 **Access Points:**

   - API Base: `http://127.0.0.1:8000`
   - Interactive Docs: `http://127.0.0.1:8000/docs`
   - OpenAPI Schema: `http://127.0.0.1:8000/openapi.json`

> ⚠️ **Important**: When running in Docker, services should communicate using container names (e.g., `http://backend:8000`) rather than `localhost`.

## 📡 API Reference

### Chat Streaming Endpoint

**`POST /api/chat/stream`**

Processes user queries and returns streaming chat responses.

#### Request Format

```json
{
  "query": "What is Amazon Bedrock?"
}
```

#### Example Usage

**cURL:**

```bash
curl -X POST "http://localhost:8000/api/chat/stream" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hello, how can you help me?"}'
```

**Python:**

```python
import httpx

async with httpx.AsyncClient() as client:
    async with client.stream(
        "POST",
        "http://localhost:8000/api/chat/stream",
        json={"query": "What is AWS Bedrock?"}
    ) as response:
        async for chunk in response.aiter_text():
            print(chunk, end="")
```

### Health Check

Test if the service is running:

```bash
curl -X GET "http://localhost:8000/health"
```

## 🏗 Development

### Code Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── routers/             # API route handlers
│   ├── api/                 # Business logic
│   ├── core/                # Data models
│   └── schemas/             # Utility functions
├── pyproject.toml           # Python dependencies
├── Dockerfile               # Container configuration
├── .env.example             # Environment template
└── README.md                # This file
```
