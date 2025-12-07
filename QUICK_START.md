# 🚀 RetroRange - Quick Start Guide

## One-Command Setup (Recommended)

```bash
make quickstart
```

This will:
1. Start all Docker services (PostgreSQL, Redis, Elasticsearch, Kibana, MinIO)
2. Install frontend and backend dependencies
3. Run database migrations
4. Seed initial data
5. Start development servers

---

## Manual Setup

### Step 1: Start Infrastructure
```bash
docker-compose up -d
```

Wait ~30 seconds for services to be healthy.

### Step 2: Install Dependencies
```bash
# Frontend
cd frontend && npm install

# Backend
cd ../backend && pip install -r requirements.txt
```

### Step 3: Initialize Database
```bash
cd backend
alembic upgrade head          # Run migrations
python scripts/seed_data.py   # Create admin user
```

### Step 4: Start Servers
```bash
# Terminal 1: Backend
cd backend
uvicorn main:app --reload --port 8000

# Terminal 2: Frontend
cd frontend
npm run dev
```

---

## Access Points

| Service | URL | Credentials |
|---------|-----|-------------|
| **Landing Page** | http://localhost:5173 | - |
| **App Login** | http://localhost:5173/app/login | admin@retrorange.local / Admin123! |
| **API Docs** | http://localhost:8000/docs | - |
| **Kibana** | http://localhost:5601 | - |
| **MinIO Console** | http://localhost:9001 | minioadmin / minioadmin |
| **PostgreSQL** | localhost:5432 | postgres / shibin |

---

## Database

- **Name:** `range`
- **User:** `postgres`
- **Password:** `shibin`
- **Connection String:** `postgresql+asyncpg://postgres:shibin@localhost:5432/range`

---

## Common Commands

```bash
# Development
make dev                 # Start all services
make test                # Run tests
make lint                # Lint code
make format              # Format code

# Database
make migrate             # Run migrations
make seed                # Seed data
make db-reset            # Reset database

# Docker
make docker-up           # Start containers
make docker-down         # Stop containers
make docker-logs         # View logs

# Deployment
make build               # Build for production
make deploy-staging      # Deploy to staging
make deploy-prod         # Deploy to production

# Utilities
make health              # Check service health
make logs                # View application logs
make shell-db            # Open PostgreSQL shell
make shell-redis         # Open Redis CLI
```

---

## Verify Installation

```bash
# Check Docker services
docker-compose ps

# All services should show "healthy" status

# Check backend
curl http://localhost:8000/health
# Should return: {"status":"healthy","service":"retrorange-api"}

# Check frontend
# Open browser: http://localhost:5173
# You should see the retro terminal landing page
```

---

## Troubleshooting

### Services won't start
```bash
docker-compose down -v
docker-compose up -d
```

### Port conflicts
Edit `docker-compose.yml` and change port mappings:
```yaml
ports:
  - "5433:5432"  # Change PostgreSQL to 5433
```

### Database migration fails
```bash
cd backend
alembic stamp head
alembic upgrade head
```

### Frontend build errors
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

---

## Next Steps

1. ✅ **Explore the landing page** - Check out the retro terminal theme
2. ✅ **Log in to the app** - Use admin@retrorange.local / Admin123!
3. ✅ **Browse API docs** - http://localhost:8000/docs
4. ✅ **Check the database** - `make shell-db` then `\dt` to list tables
5. ✅ **Read the docs** - `docs/architecture.md`, `docs/deploy.md`
6. ✅ **Start coding!** - Implement business logic in TODO-marked stubs

---

## File Structure Quick Reference

```
frontend/src/
  pages/marketing/    → Landing page, pricing, etc.
  pages/app/          → Dashboard, scenarios, SOC, etc.
  components/         → Reusable UI components
  features/           → Redux slices
  services/           → API clients

backend/app/
  api/v1/             → API route handlers
  models/             → SQLAlchemy database models
  services/           → Business logic
  workers/            → Celery background jobs
  core/               → Config, security, RBAC

infra/
  docker/             → Dockerfiles
  terraform/          → Infrastructure provisioning
  ansible/            → Configuration management
  kubernetes/         → Helm charts

siem/
  elasticsearch/      → Index templates
  kibana/             → Dashboards
  logstash/           → Log pipelines
```

---

## Development Workflow

1. Create a new feature branch
2. Implement business logic in stub files
3. Write tests
4. Run `make lint` and `make test`
5. Commit and push
6. CI runs automatically (GitHub Actions)
7. Deploy to staging → production

---

## Production Deployment

### Docker Compose (Small Scale)
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Kubernetes (Enterprise)
```bash
cd infra/kubernetes/helm
helm install retrorange . -f values-prod.yaml
```

### Terraform + Ansible (Full Cloud)
```bash
cd infra/terraform/environments/prod
terraform apply

cd ../../../ansible
ansible-playbook -i inventory/prod playbooks/site.yml
```

---

## Support

- **Docs:** `docs/` directory
- **Architecture:** `overview.md` + `architecture.md`
- **Security:** `docs/security.md`
- **Deployment:** `docs/deploy.md`
- **Project Summary:** `PROJECT_SUMMARY.md`

---

**Ready to build the future of cyber training! 🎮🔐**
