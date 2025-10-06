FROM astral/uv:0.8-python3.12-bookworm
WORKDIR /services
COPY . .
RUN uv sync
CMD ["uv", "run", "fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000