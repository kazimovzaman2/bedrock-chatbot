# 🤖 Bedrock Chatbot

A full-stack AI chatbot application built with FastAPI backend and Streamlit frontend, featuring real-time streaming responses and multi-session chat management.

**Backend IP:** `http://44.209.103.240:8000/docs`  
**Frontend IP:** `http://44.209.103.240:8501`

## Demo

https://github.com/user-attachments/assets/a74c6b23-d27d-40a7-9b9f-72ee480cf419

## ✨ Features

- **Real-time Chat Streaming**: Live AI responses as they generate
- **Multi-Session Management**: Create and manage multiple chat conversations
- **Modern UI**: Clean, responsive chat interface with custom styling
- **Docker Ready**: Full containerization with Docker Compose
- **AWS Bedrock Integration**: Powered by Amazon Bedrock AI services
- **Session Persistence**: Chat history maintained during app runtime

## 🏗 Architecture

```
┌─────────────────┐    HTTP Streaming    ┌──────────────────┐
│   Streamlit     │◄──────────────────►  │   FastAPI        │
│   Frontend      │    Port 8501         │   Backend        │
│   (Python)      │                      │   (Python)       │
└─────────────────┘                      └──────────────────┘
                                                │
                                                ▼
                                        ┌──────────────────┐
                                        │   AWS Bedrock    │
                                        │   AI Service     │
                                        └──────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Docker & Docker Compose
- Git

### 1. Clone Repository

```bash
git clone <repo-url>
cd bedrock-chatbot
```

### 2. Configure Environment

Create environment files:

**Backend** (`backend/.env`):

```env
API_KEY=your_bedrock_api_key_here
AWS_REGION=us-east-1
LOG_LEVEL=INFO
```

**Frontend** (`frontend/.env`):

```env
API_URL=http://backend:8000/api/chat/stream
```

### 3. Start Application

```bash
# Build and start all services
docker-compose up --build

# Or run in background
docker-compose up --build -d
```

### 4. Access Applications

- **Frontend (Chat Interface)**: http://localhost:8501
- **Backend (API Docs)**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📁 Project Structure

```
bedrock-chatbot/
├── backend/                 # FastAPI backend service
│   ├── app/                # Application code
│   ├── Dockerfile          # Backend container config
│   ├── requirements.txt    # Python dependencies
│   └── .env               # Backend environment variables
├── frontend/               # Streamlit frontend application
│   ├── app.py             # Main Streamlit app
│   ├── pyproject.toml     # UV project configuration
│   ├── Dockerfile         # Frontend container config
│   └── .env              # Frontend environment variables
├── docker-compose.yml     # Multi-service orchestration
└── README.md             # This file
```

## 🛠 Development Setup

### Local Development (Without Docker)

**Backend:**

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**Frontend:**

```bash
cd frontend
pip install uv  # Modern Python package manager
uv sync
uv run streamlit run app.py
```

## 📡 API Endpoints

| Method | Endpoint           | Description                   |
| ------ | ------------------ | ----------------------------- |
| `POST` | `/api/chat/stream` | Stream chat responses         |
| `GET`  | `/health`          | Health check                  |
| `GET`  | `/docs`            | Interactive API documentation |

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/chat/stream" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hello, how can you help me?"}'
```

## ⚙️ Configuration

### Environment Variables

**Backend Configuration:**

- `AWS_ACCESS_KEY`: AWS access key (required)
- `AWS_SECRET_KEY`: AWS secret key (required)
- `AWS_REGION`: AWS region (default: us-east-1)

**Frontend Configuration:**

- `API_URL`: Backend API endpoint (required)

### Docker Configuration

The application uses Docker Compose with:

- **Bridge Network**: `bedrock_chatbot` for service communication
- **Volume Persistence**: Separate volumes for backend and frontend dependencies
- **Auto-restart**: Services restart automatically on failure
- **Port Mapping**: Backend (8000), Frontend (8501)

## 📊 Monitoring

### Health Checks

```bash
# Check backend health
curl http://localhost:8000/health

# Check frontend accessibility
curl -I http://localhost:8501
```

### Docker Monitoring

```bash
# View resource usage
docker stats

# Check container logs
docker-compose logs -f --tail=100
```
