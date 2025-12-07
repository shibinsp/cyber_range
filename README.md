# 🎮 RetroRange - Enterprise Cyber Range Platform

> **Production-grade cyber security training platform with a retro terminal aesthetic**

[![License](https://img.shields.io/badge/license-Enterprise-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/react-18-61dafb.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-0.104+-009688.svg)](https://fastapi.tiangolo.com/)

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 18+ & npm
- Python 3.11+
- PostgreSQL 15+ (or use Docker)

### 1. Clone & Setup

```bash
# Clone the repository
git clone <repository-url>
cd cyber_range

# Copy environment variables
cp .env.example .env
# Edit .env with your credentials (DB password already set to 'shibin')
```

### 2. Start Infrastructure

```bash
# Start all services (Postgres, Redis, Elasticsearch, MinIO)
docker-compose up -d

# Wait for services to be healthy (~30 seconds)
docker-compose ps
```

### 3. Initialize Database

```bash
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Seed initial data (roles, demo scenarios, admin user)
python scripts/seed_data.py
```

### 4. Start Backend

```bash
# From backend/ directory
uvicorn main:app --reload --port 8000

# Backend available at http://localhost:8000
# API docs at http://localhost:8000/docs
```

### 5. Start Frontend

```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev

# Frontend available at http://localhost:5173
```

### 6. Start Workers (Optional)

```bash
cd backend
celery -A app.workers.tasks worker --loglevel=info
```

---

## 📁 Project Structure

```
cyber_range/
├── frontend/          # React + Vite + Tailwind frontend
│   ├── src/
│   │   ├── pages/    # Marketing + App pages
│   │   ├── components/ # Reusable UI components
│   │   ├── features/ # Redux slices
│   │   └── services/ # API clients
│   └── public/       # Static assets
│
├── backend/          # FastAPI backend
│   ├── app/
│   │   ├── api/      # Route handlers
│   │   ├── models/   # SQLAlchemy models
│   │   ├── schemas/  # Pydantic schemas
│   │   ├── services/ # Business logic
│   │   └── workers/  # Celery tasks
│   ├── alembic/      # DB migrations
│   └── tests/        # Pytest suite
│
├── infra/            # Infrastructure as Code
│   ├── terraform/    # Cloud provisioning
│   ├── ansible/      # Configuration management
│   ├── kubernetes/   # Helm charts
│   └── docker/       # Dockerfiles
│
├── siem/             # Elasticsearch & Kibana configs
│   ├── elasticsearch/ # Index templates
│   └── kibana/       # Dashboards
│
├── replay/           # PCAP replay engine
├── ci/               # GitHub Actions workflows
├── tests/            # E2E & load tests
├── docs/             # Documentation
└── docker-compose.yml
```

---

## 🎨 Features

### Marketing Site
- 🌟 Retro CRT terminal theme with scanlines & neon accents
- 📊 3-tier pricing (Free Eval / Team / Enterprise)
- 🎥 Interactive product tour
- 📱 Fully responsive, WCAG AA accessible
- 🚀 SEO optimized (meta tags, sitemap, structured data)

### Core Platform
- 🔐 **Auth & RBAC**: OAuth2 + JWT, 8 role tiers
- 🎯 **Scenario Builder**: Drag-and-drop attack chain designer
- 💻 **VM Control**: Start/stop/snapshot VMs, interactive consoles
- 🌐 **Network Topology**: Visual graph of range infrastructure
- 📡 **Live SOC**: Real-time log viewer with Elasticsearch
- 🎬 **Replay Studio**: PCAP timeline playback with annotations
- 🏆 **Scoring Engine**: Automated metrics and leaderboards
- 🛠️ **Orchestration**: Terraform & Ansible integration
- ⚔️ **Attack Sim**: CALDERA & Sliver C2 frameworks

### Integrations
- Elasticsearch + Kibana (SIEM)
- MinIO (S3-compatible object storage)
- Redis (caching + job queue)
- CALDERA (adversary emulation)
- Sliver (C2 framework)

---

## 🗄️ Database

**PostgreSQL** database name: `range`
Default credentials (development):
- User: `postgres`
- Password: `shibin`
- Host: `localhost`
- Port: `5432`

**Schema includes:**
- Users, Roles, Permissions
- Scenarios, Scenario History
- Virtual Machines, Topology
- Terraform/Ansible Jobs
- Scoring Results, Audit Logs

See `db/schema.sql` and `db/er_diagram.mmd` for details.

---

## 🔧 Configuration

### Environment Variables

Key variables in `.env`:

```bash
# Database
DATABASE_URL=postgresql+asyncpg://postgres:shibin@localhost:5432/range

# Security
SECRET_KEY=your-secret-key-change-in-production
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15

# Redis
REDIS_URL=redis://localhost:6379/0

# Elasticsearch
ELASTICSEARCH_URL=http://localhost:9200

# MinIO
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin

# CALDERA
CALDERA_URL=http://localhost:8888
CALDERA_API_KEY=your-caldera-key
```

See `.env.example` for full list.

---

## 🧪 Testing

### Unit Tests
```bash
# Backend
cd backend
pytest tests/unit -v --cov=app

# Frontend
cd frontend
npm run test
```

### Integration Tests
```bash
cd backend
pytest tests/integration -v
```

### E2E Tests
```bash
cd frontend
npm run test:e2e
```

### Load Tests
```bash
cd tests/k6
k6 run scenarios.js
```

---

## 🚢 Deployment

### Docker Compose (Local/Staging)
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Kubernetes (Production)
```bash
cd infra/kubernetes/helm
helm install retrorange . -f values-prod.yaml
```

### Terraform (Cloud Infrastructure)
```bash
cd infra/terraform/environments/prod
terraform init
terraform plan
terraform apply
```

See `docs/deploy.md` for detailed deployment guide.

---

## 📚 Documentation

- [Architecture Overview](overview.md)
- [Deployment Guide](docs/deploy.md)
- [Security Guide](docs/security.md)
- [API Reference](http://localhost:8000/docs) (when running)
- [Operations Runbook](docs/runbook.md)

---

## 🔒 Security

- **Isolation**: All malware/attack VMs run in isolated VLANs
- **Secrets**: HashiCorp Vault or Kubernetes Secrets
- **Auth**: bcrypt password hashing, JWT with refresh tokens
- **RBAC**: Fine-grained permissions per role
- **Audit Logs**: Immutable trail of all actions
- **Compliance**: OWASP Top 10 mitigations, WCAG AA

See `docs/security.md` for hardening checklist.

---

## 🛠️ Development

### Code Quality
```bash
# Frontend linting
cd frontend
npm run lint
npm run format

# Backend linting
cd backend
ruff check .
black .
mypy .
```

### Pre-commit Hooks
```bash
pip install pre-commit
pre-commit install
```

### Database Migrations
```bash
cd backend

# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

---

## 🏗️ Tech Stack

| Layer          | Technology                          |
|----------------|-------------------------------------|
| Frontend       | React 18, Vite, Tailwind CSS        |
| Backend        | FastAPI, SQLAlchemy 2.0, Pydantic   |
| Database       | PostgreSQL 15                       |
| Search         | Elasticsearch 8, Kibana             |
| Cache/Queue    | Redis 7, Celery                     |
| Storage        | MinIO (S3-compatible)               |
| Orchestration  | Terraform, Ansible, Kubernetes      |
| CI/CD          | GitHub Actions                      |
| Monitoring     | Prometheus, Grafana                 |
| Attack Sim     | CALDERA, Sliver                     |

---

## 📊 Performance

**Target Metrics:**
- 500+ concurrent users
- 50+ simultaneous scenarios
- 2,000+ VMs managed
- 10GB/day log ingestion
- <200ms API latency (p95)

---

## 🗺️ Roadmap

- [x] **Q1 2025**: MVP (auth, scenarios, SOC, scoring)
- [ ] **Q2 2025**: Marketplace, advanced builder, multi-tenant
- [ ] **Q3 2025**: White-label, on-prem, SSO, certifications
- [ ] **Q4 2025**: Multi-cloud, AI scenarios, collaboration

---

## 👥 Team Roles

Default admin credentials (created by seed script):
- **Email**: admin@retrorange.local
- **Password**: Admin123! (change immediately)

User roles:
- superadmin, admin, instructor, red, blue, analyst, student, guest

See `docs/security.md` for role permissions matrix.

---

## 📄 License

**Enterprise License** - Proprietary
© 2025 RetroRange Inc. All rights reserved.

Contact: sales@retrorange.com

---

## 🤝 Support

- **Docs**: https://docs.retrorange.com
- **Issues**: GitHub Issues
- **Email**: support@retrorange.com
- **Slack**: #retrorange-community

---

## 🎯 Default Login Credentials (Dev Only)

After running `seed_data.py`:

| Role       | Email                   | Password   |
|------------|-------------------------|------------|
| superadmin | admin@retrorange.local  | Admin123!  |
| instructor | instructor@retrorange.local | Instructor123! |
| red team   | red@retrorange.local    | Red123!    |
| blue team  | blue@retrorange.local   | Blue123!   |
| student    | student@retrorange.local| Student123!|

**⚠️ Change all passwords in production!**

---

## 🚀 Quick Commands (Makefile)

```bash
make setup          # Install all dependencies
make dev            # Start all services in dev mode
make test           # Run all tests
make lint           # Run linters
make migrate        # Run database migrations
make seed           # Seed database
make clean          # Clean build artifacts
make deploy-staging # Deploy to staging
```

---

**Built with ❤️ and ☕ by the RetroRange team**
