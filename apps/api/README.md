```bash
# Start the DB container (from root of the repo)
sudo docker compose up db

# Install backend dependencies
cd apps/api
uv sync

# Start FastAPI dev server
uv run fastapi dev
```
