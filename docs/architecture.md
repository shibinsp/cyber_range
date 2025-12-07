# Architecture Documentation

## System Overview

RetroRange is a cloud-native, event-driven cyber range platform.

## Components

### Frontend (React SPA)
- React 18 + Vite
- Redux Toolkit (global state)
- React Query (server state)
- Tailwind CSS (retro theme)
- WebSocket (real-time updates)

### Backend (FastAPI)
- Async/await architecture
- SQLAlchemy 2.0 (async ORM)
- JWT authentication
- RESTful API + WebSocket endpoints

### Data Layer
- PostgreSQL (primary)
- Elasticsearch (logs/SIEM)
- Redis (cache + queue)
- MinIO (object storage)

### Orchestration
- Terraform (infrastructure provisioning)
- Ansible (configuration management)
- CALDERA (adversary emulation)
- Celery (background workers)

## Data Flow

1. User initiates scenario → Frontend POST /scenarios/{id}/run
2. Backend enqueues Terraform job → Celery worker
3. Worker provisions VMs → Updates database
4. Worker publishes event → Redis PubSub
5. Frontend receives update → WebSocket
6. VMs run agents → Logs to Elasticsearch
7. Frontend queries logs → Backend proxy to Elastic
8. Scenario completes → Scoring engine calculates results

## Scalability
- Horizontal: Kubernetes HPA (2-20 backend replicas)
- Database: Read replicas for reports
- Elasticsearch: 3-node cluster minimum
- Redis: Cluster mode (6 nodes)
- CDN: Static assets cached (1yr TTL)

## Deployment Targets
- Development: Docker Compose
- Staging: k3s/minikube
- Production: EKS/GKE/AKS
