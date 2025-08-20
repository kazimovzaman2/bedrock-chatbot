import streamlit as st
import httpx
import uuid
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="wide")

if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {}

if "current_session_id" not in st.session_state:
    session_id = str(uuid.uuid4())
    st.session_state.current_session_id = session_id
    st.session_state.chat_sessions[session_id] = {
        "title": "New Chat",
        "messages": [],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

if "input_key" not in st.session_state:
    st.session_state.input_key = 0


def create_new_chat():
    """Create a new chat session"""
    session_id = str(uuid.uuid4())
    st.session_state.current_session_id = session_id
    st.session_state.chat_sessions[session_id] = {
        "title": "New Chat",
        "messages": [],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    st.session_state.input_key += 1
    st.rerun()


def switch_chat(session_id):
    """Switch to a different chat session"""
    st.session_state.current_session_id = session_id
    st.session_state.input_key += 1
    st.rerun()


def delete_chat(session_id):
    """Delete a chat session"""
    if len(st.session_state.chat_sessions) > 1:
        del st.session_state.chat_sessions[session_id]
        if st.session_state.current_session_id == session_id:
            st.session_state.current_session_id = list(
                st.session_state.chat_sessions.keys()
            )[0]
        st.rerun()


def update_chat_title(session_id, first_message):
    """Update chat title based on first message"""
    if len(first_message) > 50:
        title = first_message[:50] + "..."
    else:
        title = first_message
    st.session_state.chat_sessions[session_id]["title"] = title


def add_message(session_id, role, content):
    """Add a message to the chat session"""
    st.session_state.chat_sessions[session_id]["messages"].append(
        {
            "role": role,
            "content": content,
            "timestamp": datetime.now().strftime("%H:%M"),
        }
    )


st.markdown(
    """
<style>
.chat-container {
    height: 600px;
    overflow-y: auto;
    padding: 1rem;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    background-color: #fafafa;
    margin-bottom: 1rem;
}

.user-message {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 1rem;
}

.user-message-content {
    background-color: #007bff;
    color: white;
    padding: 0.75rem 1rem;
    border-radius: 18px 18px 5px 18px;
    max-width: 70%;
    word-wrap: break-word;
}

.bot-message {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 1rem;
}

.bot-message-content {
    background-color: #e9ecef;
    color: #333;
    padding: 0.75rem 1rem;
    border-radius: 18px 18px 18px 5px;
    max-width: 70%;
    word-wrap: break-word;
}

.timestamp {
    font-size: 0.75rem;
    color: #666;
    margin-top: 0.25rem;
}

.sidebar-chat-item {
    padding: 0.75rem;
    margin-bottom: 0.5rem;
    border-radius: 8px;
    cursor: pointer;
    border: 1px solid transparent;
}

.sidebar-chat-item:hover {
    background-color: #f8f9fa;
    border-color: #dee2e6;
}

.sidebar-chat-item.active {
    background-color: #e3f2fd;
    border-color: #2196f3;
}

.chat-title {
    font-weight: 500;
    margin-bottom: 0.25rem;
}

.chat-date {
    font-size: 0.75rem;
    color: #666;
}

.new-chat-btn {
    width: 100%;
    margin-bottom: 1rem;
}
</style>
""",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.title("💬 Chat History")

    if st.button("➕ New Chat", key="new_chat", help="Start a new conversation"):
        create_new_chat()

    st.divider()

    for session_id, session_data in st.session_state.chat_sessions.items():
        is_active = session_id == st.session_state.current_session_id

        col1, col2 = st.columns([4, 1])

        with col1:
            if st.button(
                session_data["title"],
                key=f"chat_{session_id}",
                help=f"Created: {session_data['created_at']}",
                use_container_width=True,
            ):
                switch_chat(session_id)

        with col2:
            if len(st.session_state.chat_sessions) > 1:
                if st.button("🗑️", key=f"delete_{session_id}", help="Delete this chat"):
                    delete_chat(session_id)

        if is_active:
            st.markdown("**← Current**")

        st.markdown("---")

current_session = st.session_state.chat_sessions[st.session_state.current_session_id]

st.title("🤖 RAG Chatbot")
st.markdown(f"**Current Chat:** {current_session['title']}")

chat_container = st.container()

with chat_container:
    if current_session["messages"]:
        for message in current_session["messages"]:
            if message["role"] == "user":
                st.markdown(
                    f"""
                <div class="user-message">
                    <div class="user-message-content">
                        {message["content"]}
                        <div class="timestamp">{message["timestamp"]}</div>
                    </div>
                </div>
                """,
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"""
                <div class="bot-message">
                    <div class="bot-message-content">
                        {message["content"]}
                        <div class="timestamp">{message["timestamp"]}</div>
                    </div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

st.markdown("---")

col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.text_input(
        "Ask me anything:",
        placeholder="Type your message here...",
        key=f"user_input_{st.session_state.input_key}",
        label_visibility="collapsed",
    )

with col2:
    send_button = st.button("Send 📤", type="primary", use_container_width=True)

if (send_button or user_input) and user_input.strip():
    print("User input detected:", user_input)
    add_message(st.session_state.current_session_id, "user", user_input)

    if len(current_session["messages"]) == 1:
        print("Updating chat title...")
        update_chat_title(st.session_state.current_session_id, user_input)

    with st.spinner("Bot is typing..."):
        try:
            print("Starting HTTP request to API...")
            print("API URL:", os.getenv("API_URL"))

            full_response = ""
            response_placeholder = st.empty()

            with httpx.stream(
                "POST",
                os.getenv("API_URL"),
                json={"query": user_input},
                timeout=30.0,
            ) as response:
                print("Connection established, streaming response...")
                for chunk in response.iter_text():
                    if chunk:
                        full_response += chunk
                        response_placeholder.markdown(f"**🤖 Bot:** {full_response}")
                        print("Received chunk:", chunk)

            print("Adding bot response to session:", full_response)
            add_message(st.session_state.current_session_id, "bot", full_response)

        except httpx.RequestError as e:
            error_msg = f"Connection error: {str(e)}"
            print(error_msg)
            st.error(error_msg)
            add_message(st.session_state.current_session_id, "bot", error_msg)
        except httpx.TimeoutException:
            error_msg = "Request timed out. Please try again."
            print(error_msg)
            st.error(error_msg)
            add_message(st.session_state.current_session_id, "bot", error_msg)
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            print(error_msg)
            st.error(error_msg)
            add_message(st.session_state.current_session_id, "bot", error_msg)

    print("Incrementing input key and rerunning Streamlit...")
    st.session_state.input_key += 1
    st.rerun()

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "💡 Tip: Use the sidebar to manage your chat sessions"
    "</div>",
    unsafe_allow_html=True,
)
