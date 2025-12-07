# Deployment Guide

## Quick Start (Local Development)

```bash
# 1. Start infrastructure
docker-compose up -d

# 2. Install dependencies
cd frontend && npm install
cd ../backend && pip install -r requirements.txt

# 3. Run migrations
cd backend && alembic upgrade head

# 4. Seed database
python scripts/seed_data.py

# 5. Start servers
# Terminal 1: Backend
cd backend && uvicorn main:app --reload

# Terminal 2: Frontend
cd frontend && npm run dev
```

## Production Deployment

### Option 1: Docker Compose
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Option 2: Kubernetes
```bash
cd infra/kubernetes/helm
helm install retrorange . -f values-prod.yaml
```

### Option 3: Cloud (Terraform)
```bash
cd infra/terraform/environments/prod
terraform init
terraform apply
```

## Default Credentials
- Email: admin@retrorange.local
- Password: Admin123!

⚠️ **Change immediately in production!**
