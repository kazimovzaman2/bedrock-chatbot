FROM ghcr.io/astral-sh/uv:bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_INSTALL_DIR=/python \
    UV_PYTHON_PREFERENCE=only-managed

RUN apt-get update -y && \
    apt-get install --no-install-recommends -y clang git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY frontend/ .

RUN uv sync --no-dev


ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

EXPOSE 8501

CMD ["uv", "run", "streamlit", "run", "app.py"]