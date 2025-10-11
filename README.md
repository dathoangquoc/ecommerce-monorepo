# 🛍️ FastAPI + Next.js E-commerce

Monorepo for an **E-commerce platform** built with:

* **FastAPI** (backend services: auth, catalog, orders, payments)
* **Next.js** (frontend: customer site + admin dashboard)
* **Postgres** (relational DB, migrations via Alembic)
* **Redis** (optional cache/session store)
* **Stripe** (payments + refunds)
* **AWS ECS Fargate** (staging/prod deploy)

---

## 📂 Project Structure

```
.
├── apps/
│   ├── services/        
│   │   ├── auth_service/       # FastAPI: authentication & users
│   │   ├── catalog_service/    # FastAPI: products, categories, media
│   │   ├── order_service/      # FastAPI: cart, orders, inventory
│   │   └── payment_service/    # FastAPI: Stripe integration & webhooks
│   └── web/                    # Next.js frontend 
│
├── infra/
│   ├── docker-compose.yml      # Local dev (Postgres, Redis, services)
│   ├── Dockerfiles/            # Container configs
│   ├── migrations/             # Shared Alembic migration logic
│   └── terraform/              # AWS ECS + RDS + S3 infra configs
│
├── tests/
│   ├── unit/                   # pytest unit tests
│   ├── integration/            # integration tests (testcontainers-python)
│   └── e2e/                    # Playwright/Cypress end-to-end tests
│
├── .github/
│   └── workflows/              # GitHub Actions CI/CD pipelines
│
└── README.md
```

```
.
├── apps
│   ├── api
│   │   ├── src
│   │   │   ├── auth
│   │   │   │   ├── config.py           # Local configs
│   │   │   │   ├── dependencies.py     # FastAPI dependency functions
│   │   │   │   ├── models.py           # SQLAlchemy schemas
│   │   │   │   ├── router.py           # FastAPI router
│   │   │   │   ├── schemas.py          # Pydantic models
│   │   │   │   ├── service.py          # Business logic
│   │   │   │   └── utils.py            # Low-level utilities
│   │   │   ├── catalog
│   │   │   ├── order
│   │   │   └── payment
│   │   ├── tests
│   │   │   └── auth
│   │   │       └── test_utils.py
│   └── web
├── infra
```
---

## 🌱 Local Development

### Requirements

* Python 3.11+
* Node.js 20+
* Docker & Docker Compose

### First-time Setup

```bash
# Clone repo
git clone git@github.com:dathoangquoc/ecommerce-monorepo.git
cd ecommerce-monorepo
```

### Quickstart with Docker

```bash
sudo docker compose up -d
```

### OR Run Backend and Frontend Separately

```bash
# Install backend dependencies
cd apps/services
uv sync

# Run DB migrations
alembic upgrade head

# Start FastAPI dev server
uv run fastapi dev
```

### Running Frontend

```bash
cd apps/web
npm install
npm run dev
```

---

## 🌳 Branching Strategy

* `main` → always **deployable**, protected branch
* `feature/*` → short-lived feature branches
* `fix/*` → bugfix branches
* `release/*` → optional staging releases

---

## 🔐 Environment Variables

Each service loads config via `.env`:

```
# Common
DATABASE_URL=postgresql+psycopg2://user:pass@localhost:5432/shop
REDIS_URL=redis://localhost:6379/0
JWT_SECRET=supersecret
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
AWS_S3_BUCKET=myshop-dev
```

Secrets in production are managed via **AWS Secrets Manager**.

---

## 🧪 Testing

* **Unit tests**: `pytest tests/unit`
* **Integration tests**: run with Docker Compose or testcontainers
* **E2E tests**: Playwright/Cypress against running stack

```bash
pytest -v
npm run test:e2e
```

---

## 🚀 CI/CD

* **GitHub Actions (CI)**: run tests, lint, migrations on every PR
* **GitHub Actions (CD)**: on merge to `main`, build & push Docker images → deploy to ECS Fargate staging
* **Terraform**: AWS infra (RDS, ECS, ALB, S3, Secrets Manager)

---

## 📊 Observability

* **Logs**: structured JSON via loguru → CloudWatch Logs
* **Metrics**: Prometheus client → Grafana dashboards
* **Tracing**: OpenTelemetry → Jaeger / AWS X-Ray

---

## ✅ Launch Checklist

* [ ] HTTPS with ACM
* [ ] Privacy Policy, TOS, SEO tags
* [ ] Stripe live keys enabled
* [ ] Backups verified
* [ ] Load tests pass
