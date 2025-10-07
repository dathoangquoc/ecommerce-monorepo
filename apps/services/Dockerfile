FROM python:3.12-slim

# Copy uv binary from a distroless image
COPY --from=ghcr.io/astral-sh/uv:0.8.23 /uv /uvx /bin/

ENV PATH="/bin:${PATH}"
WORKDIR /services

# Copy project files but ignore host virtualenvs (see .dockerignore)
COPY . .

# Remove any accidental copied virtualenv created on the host to avoid
# importing native extensions built for the host OS/Python (causes
# ModuleNotFoundError for pydantic_core._pydantic_core).
RUN if [ -d ".venv" ]; then rm -rf .venv; fi

# Install build dependencies that some packages may need to compile native
# wheels. Keep them minimal; uv sync will install Python deps into a venv.
RUN apt-get update \
	&& apt-get install -y --no-install-recommends gcc build-essential python3-dev \
	&& rm -rf /var/lib/apt/lists/*

# Sync dependencies and create a proper environment inside the image
RUN uv sync

CMD ["uv", "run", "fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000