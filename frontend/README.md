# Bedrock Chatbot Frontend

A modern, interactive frontend for the Bedrock Chatbot application built with **Streamlit**. Features multi-session chat management, real-time streaming responses, and an intuitive user interface for seamless conversations with AI.

## 🚀 Features

- **Multi-Session Chat Management**: Create, switch between, and manage multiple chat conversations
- **Real-time Streaming**: Live streaming responses from the backend API
- **Responsive Design**: Modern chat interface with custom styling and smooth interactions
- **Session Persistence**: Chat history maintained across sessions during app runtime
- **Interactive UI**: Intuitive chat bubbles, timestamps, and user-friendly navigation
- **Error Handling**: Robust error handling with user-friendly error messages
- **Docker Ready**: Containerized deployment with optimized build process

## 📋 Prerequisites

- **Python**: 3.12 or higher
- **Backend Service**: The backend API must be running and accessible
- **Docker**: Latest stable version (optional, for containerized deployment)

## 🛠 Installation & Setup

### Local Development Setup

1. **Navigate to Frontend Directory**

   ```bash
   cd frontend
   ```

2. **Install UV Package Manager** (Recommended)

   ```bash
   # Install UV (modern Python package manager)
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Or using pip
   pip install uv
   ```

3. **Install Dependencies**

   ```bash
   # Using UV (recommended)
   uv sync

   # Or using traditional pip
   pip install -r requirements.txt
   ```

4. **Configure Environment**

   Create a `.env` file in the frontend directory:

   ```env
   # Backend API Configuration
   API_URL=http://localhost:8000/api/chat/stream

   # Optional Streamlit Configuration
   STREAMLIT_SERVER_PORT=8501
   STREAMLIT_SERVER_ADDRESS=0.0.0.0
   ```

5. **Start Development Server**

   ```bash
   # Using UV
   uv run streamlit run app.py

   # Or using traditional method
   streamlit run app.py
   ```

   🌐 **Access the Application**: `http://localhost:8501`

## 🎯 Features Overview

### Chat Session Management

- **Create New Chats**: Start fresh conversations with the "➕ New Chat" button
- **Session Switching**: Click any chat in the sidebar to switch between conversations
- **Auto-Naming**: Chat sessions are automatically named based on the first message
- **Delete Sessions**: Remove unwanted chat sessions (minimum one session retained)
- **Persistent History**: All messages are stored in session state during app runtime

### Real-time Chat Experience

- **Streaming Responses**: Watch AI responses appear in real-time as they're generated
- **Message Timestamps**: Each message includes a timestamp for reference
- **Visual Chat Bubbles**: Modern chat interface with user and bot message distinction
- **Loading Indicators**: Visual feedback during API requests with "Bot is typing..." spinner

### User Interface

- **Responsive Layout**: Optimized for various screen sizes
- **Custom Styling**: Modern CSS styling for an enhanced user experience
- **Sidebar Navigation**: Easy access to chat history and session management
- **Input Handling**: Enter key support and dedicated send button
- **Error Display**: User-friendly error messages for connection issues

## 📡 API Integration

The frontend communicates with the backend through HTTP streaming:

### Request Format

```json
{
  "query": "User's message here"
}
```

### Response Handling

- Establishes streaming connection to `/api/chat/stream`
- Processes chunked responses in real-time
- Updates UI progressively as response streams in
- Handles connection errors and timeouts gracefully

### Example API Configuration

```python
# Environment configuration
API_URL = "http://backend:8000/api/chat/stream"  # Docker
# API_URL = "http://localhost:8000/api/chat/stream"  # Local development
```

## ⚙️ Configuration

### Environment Variables

| Variable                   | Required | Default   | Description                             |
| -------------------------- | -------- | --------- | --------------------------------------- |
| `API_URL`                  | ✅       | -         | Backend API endpoint for chat streaming |
| `STREAMLIT_SERVER_PORT`    | ❌       | `8501`    | Port for Streamlit server               |
| `STREAMLIT_SERVER_ADDRESS` | ❌       | `0.0.0.0` | Server bind address                     |

### Streamlit Configuration

Create a `.streamlit/config.toml` file for advanced configuration:

```toml
[server]
port = 8501
address = "0.0.0.0"
headless = true

[theme]
primaryColor = "#007bff"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"

[browser]
gatherUsageStats = false
```

## 🏗 Architecture

### File Structure

```
frontend/
├── app.py                   # Main Streamlit application
├── pyproject.toml          # UV/Python project configuration
├── Dockerfile              # Container configuration
├── .env.example           # Environment template
├── .streamlit/            # Streamlit configuration
│   └── config.toml
├── requirements.txt       # Traditional pip requirements (generated)
└── README.md             # This file
```

### Key Components

1. **Session Management**: Handles multiple chat sessions with UUID-based identification
2. **Message Storage**: In-memory storage of chat history using Streamlit session state
3. **API Client**: HTTP streaming client using `httpx` for real-time communication
4. **UI Components**: Custom CSS styling for modern chat interface
5. **Error Handling**: Comprehensive error handling for network and API issues

### State Management

```python
# Session state structure
st.session_state = {
    "chat_sessions": {
        "session_uuid": {
            "title": "Chat title",
            "messages": [
                {
                    "role": "user|bot",
                    "content": "message content",
                    "timestamp": "HH:MM"
                }
            ],
            "created_at": "YYYY-MM-DD HH:MM"
        }
    },
    "current_session_id": "active_session_uuid",
    "input_key": 0  # For input widget refresh
}
```
