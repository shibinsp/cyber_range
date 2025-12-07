# RetroRange - Enterprise Cyber Range Platform
## Architecture Overview

### Executive Summary
RetroRange is a production-grade, enterprise cyber range platform designed for SOC training, incident response testing, red/blue team exercises, and security certification programs. Built with a distinctive retro terminal aesthetic, it combines modern cloud-native architecture with comprehensive orchestration capabilities.

---

## Technology Stack

### Frontend
- **Framework**: React 18 + Vite 5
- **Styling**: Tailwind CSS 3.4 + Custom Retro Terminal Theme
- **State Management**: Redux Toolkit (global state) + React Query (server state)
- **Routing**: React Router v6
- **Real-time**: WebSocket (Socket.io client)
- **Forms**: React Hook Form + Zod validation
- **Charts/Viz**: D3.js, React Flow (topology), Recharts
- **Testing**: Vitest + Playwright

### Backend
- **Framework**: FastAPI 0.104+ (Python 3.11+)
- **ORM**: SQLAlchemy 2.0 (async) + asyncpg
- **Migrations**: Alembic
- **Auth**: OAuth2 + JWT (PyJWT) + RBAC
- **Validation**: Pydantic v2
- **WebSockets**: FastAPI WebSocket + Redis PubSub
- **Task Queue**: Celery + Redis
- **Testing**: pytest + pytest-asyncio

### Data Layer
- **Primary DB**: PostgreSQL 15+ (range database, password: shibin)
- **Search/SIEM**: Elasticsearch 8.x + Kibana
- **Cache/Queue**: Redis 7.x
- **Object Storage**: MinIO (S3-compatible)

### Infrastructure
- **Orchestration**: Kubernetes (production) + Docker Compose (dev)
- **IaC**: Terraform (AWS/GCP/Azure modules)
- **Config Mgmt**: Ansible (Proxmox, sensors, agents)
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus + Grafana
- **Secrets**: HashiCorp Vault / K8s Secrets

### Security & Attack Simulation
- **C2 Framework**: CALDERA (automated adversary emulation)
- **C2 Alternative**: Sliver (implant framework)
- **Network Sim**: GNS3/EVE-NG integration ready
- **Isolation**: Network segmentation, egress filtering, sandboxed VMs

---

## Architecture Patterns

### Layered Architecture
```
┌─────────────────────────────────────────────────────────┐
│                  Marketing Landing Page                 │
│              (SEO-optimized, static-first)              │
└─────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────┐
│                  React SPA (App Shell)                  │
│  ┌──────────┬──────────┬──────────┬─────────────────┐  │
│  │Dashboard │ Scenarios│   SOC    │  Replay/Scoring │  │
│  └──────────┴──────────┴──────────┴─────────────────┘  │
└─────────────────────────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────┐
│              FastAPI Backend (REST + WS)                │
│  ┌──────────┬──────────┬──────────┬─────────────────┐  │
│  │   Auth   │ Scenarios│   VMs    │  Orchestration  │  │
│  └──────────┴──────────┴──────────┴─────────────────┘  │
└─────────────────────────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────┐
│                     Data Layer                          │
│  ┌──────────┬──────────┬──────────┬─────────────────┐  │
│  │PostgreSQL│   Redis  │  Elastic │      MinIO      │  │
│  └──────────┴──────────┴──────────┴─────────────────┘  │
└─────────────────────────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────┐
│              Orchestration & Execution                  │
│  ┌──────────┬──────────┬──────────┬─────────────────┐  │
│  │Terraform │  Ansible │ CALDERA  │  Celery Workers │  │
│  └──────────┴──────────┴──────────┴─────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Key Design Decisions

#### 1. **Async-First Backend**
- All I/O operations use async/await
- asyncpg for PostgreSQL, aioredis for Redis
- Enables high concurrency for WebSocket connections and long-running ops

#### 2. **RBAC with 8 Role Tiers**
- `superadmin`: Platform owner, all permissions
- `admin`: Organization admin, infra management
- `instructor`: Scenario creation, student management
- `red`: Offensive operations, attack simulation
- `blue`: Defensive operations, SOC monitoring
- `analyst`: Read-only analytics, reports
- `student`: Limited scenario participation
- `guest`: Demo/trial access

#### 3. **Event-Driven Architecture**
- Redis PubSub for real-time events (VM status, scenario progress)
- Celery for background jobs (Terraform apply, log ingestion)
- WebSocket channels per user session for live updates

#### 4. **Multi-Tenant Ready**
- `visibility` field on scenarios (public/private/org)
- Row-level security via SQLAlchemy filters
- Org-scoped resources (future: `organization_id` FK)

#### 5. **Replay-Driven Learning**
- PCAP capture on all ranges
- Event timeline reconstruction (network + host telemetry)
- Frame-by-frame replay with annotation support

---

## Security Model

### Network Isolation
- **Range Networks**: Isolated VLANs per scenario
- **Egress Filtering**: Controlled NAT, proxy all external requests
- **Malware Sandbox**: Dedicated VM pools for malicious payloads
- **DMZ**: Sensor agents communicate via secure relay

### Authentication Flow
```
1. User → POST /auth/login (email, password)
2. Backend → Verify bcrypt hash
3. Backend → Generate JWT (access: 15min, refresh: 7d)
4. User → Store tokens (httpOnly cookie + localStorage)
5. User → Authenticated requests with Bearer token
6. Backend → Validate JWT, check RBAC permissions
```

### Secrets Management
- Database credentials → Vault / K8s Secrets
- API keys (CALDERA, Cloud) → Encrypted in PostgreSQL `metadata` jsonb
- User passwords → bcrypt (cost factor: 12)
- JWT signing → RS256 (public/private keypair)

---

## Data Flow Examples

### Scenario Execution
```
1. User clicks "Run Scenario" in UI
2. Frontend → POST /scenarios/{id}/run
3. Backend → Create scenario_history record
4. Backend → Enqueue Celery task: terraform_apply
5. Worker → Execute Terraform (provision VMs)
6. Worker → Publish Redis event: "scenario.terraform.complete"
7. Backend WebSocket → Push update to frontend
8. Backend → Enqueue Celery task: ansible_configure
9. Worker → Run Ansible playbooks (install agents, tools)
10. Worker → Publish Redis event: "scenario.ready"
11. Backend → Start CALDERA operation (if red team scenario)
12. Agents → Stream logs to Elasticsearch
13. Frontend → Display live SOC view (logs, alerts)
14. Scenario completes → Calculate scores → Update DB
15. Frontend → Show results + Replay link
```

### Log Ingestion Pipeline
```
1. VM agents → Send logs via Filebeat/Logstash
2. Logstash → Parse, normalize, enrich
3. Logstash → Bulk index to Elasticsearch (sysmon-*, zeek-*)
4. Celery worker → Periodic sync check (postgres ↔ elastic)
5. Frontend SOC page → Query Elastic via backend proxy
6. Kibana → Embedded dashboards for deep analysis
```

---

## Scalability & Performance

### Horizontal Scaling
- **Frontend**: Static CDN (Cloudflare) + App shell on S3/Netlify
- **Backend**: Kubernetes HPA (target: 70% CPU, 2-20 replicas)
- **PostgreSQL**: Read replicas for reporting queries
- **Elasticsearch**: 3-node cluster (min), shard per index pattern
- **Redis**: Cluster mode (6 nodes: 3 master, 3 replica)
- **MinIO**: Distributed mode (4+ nodes)

### Caching Strategy
- **Redis**: User sessions, API response cache (5min TTL)
- **Browser**: Service worker for static assets
- **CDN**: Marketing site, public assets (1yr cache)

### Load Testing Targets
- **Concurrent Users**: 500+ (app), 10,000+ (landing)
- **Scenarios Running**: 50+ simultaneous
- **VMs Managed**: 2,000+ (distributed across Proxmox clusters)
- **Log Ingestion**: 10GB/day (Elastic hot tier)

---

## Deployment Environments

### 1. Local Development
- Docker Compose (all services)
- Hot reload (Vite, FastAPI --reload)
- Seed data via Alembic migrations + Python script

### 2. Staging
- Kubernetes (minikube or k3s)
- Terraform: provision cloud resources
- Ansible: configure worker nodes
- CI deploys on merge to `develop`

### 3. Production
- Kubernetes (EKS/GKE/AKS)
- Terraform: multi-AZ, auto-scaling groups
- Ansible: immutable infra (no SSH config drift)
- Blue/Green deployments
- Monitoring: Prometheus + Grafana + PagerDuty

---

## Monitoring & Observability

### Metrics (Prometheus)
- API latency (p50, p95, p99)
- Request rate, error rate
- DB connection pool usage
- Celery queue depth
- VM provisioning time

### Logging (ELK Stack)
- Application logs (structured JSON)
- Audit logs (immutable trail)
- Security events (auth failures, privilege escalation)

### Tracing (Jaeger - optional)
- Distributed traces for scenario execution
- Correlate frontend → backend → worker → infra

### Alerts
- API error rate >5% (PagerDuty)
- Terraform job failures (Slack)
- Elasticsearch disk >80% (email)
- CALDERA agent disconnected (Dashboard banner)

---

## Compliance & Auditing

### Audit Logs
- Every API call logged: actor, action, resource, timestamp
- PostgreSQL `audit_logs` table (immutable, append-only)
- Weekly export to S3 Glacier (compliance retention)

### Data Privacy
- User PII: email (encrypted at rest if required by policy)
- Scenario artifacts: customer data never mixed with platform logs
- GDPR: user deletion cascade (soft delete, 30-day retention)

### Security Standards
- OWASP Top 10 mitigations (SQL injection, XSS, CSRF)
- Dependency scanning: Snyk / GitHub Dependabot
- Container scanning: Trivy / Anchore
- Penetration testing: Annual third-party audit

---

## Development Workflow

### Branch Strategy (GitFlow)
- `main`: production releases (tags: v1.0.0)
- `develop`: integration branch
- `feature/*`: new features
- `hotfix/*`: urgent production fixes

### Code Quality
- **Linting**: ESLint (frontend), Ruff (backend)
- **Formatting**: Prettier (frontend), Black (backend)
- **Type Checking**: TypeScript strict mode, mypy
- **Pre-commit Hooks**: lint-staged + husky
- **Code Review**: Required approvals (2 reviewers)

### Testing Strategy
- **Unit**: 80%+ coverage (Jest, pytest)
- **Integration**: API contract tests (Postman/Newman)
- **E2E**: Critical user flows (Playwright)
- **Load**: k6 scripts (CI runs on staging)
- **Security**: OWASP ZAP automated scans

---

## Roadmap & Future Enhancements

### Phase 1 (MVP) - Q1 2025
- ✅ Landing page + marketing site
- ✅ User auth + RBAC
- ✅ Scenario library + basic builder
- ✅ VM control panel
- ✅ Live SOC (Elastic integration)
- ✅ Scoring engine

### Phase 2 (Growth) - Q2 2025
- 🔲 Advanced scenario builder (drag-and-drop DAG)
- 🔲 Marketplace (community scenarios)
- 🔲 Replay Studio (PCAP timeline)
- 🔲 Multi-tenant orgs
- 🔲 SSO (SAML, Okta)

### Phase 3 (Enterprise) - Q3 2025
- 🔲 White-label customization
- 🔲 On-prem appliance (ISO image)
- 🔲 Advanced analytics (ML anomaly detection)
- 🔲 Certification tracking
- 🔲 Partner integrations (SIEM vendors)

### Phase 4 (Scale) - Q4 2025
- 🔲 Multi-cloud orchestration (AWS + Azure + GCP)
- 🔲 Federated ranges (geo-distributed)
- 🔲 AI-powered scenario generation
- 🔲 Real-time collaboration (multiplayer SOC)

---

## Getting Started

See individual README files in each directory:
- `frontend/README.md` - React app setup
- `backend/README.md` - FastAPI service
- `infra/README.md` - Infrastructure provisioning
- `docs/deploy.md` - Deployment guide
- `docs/security.md` - Security hardening

**Next Steps:**
1. Run `docker-compose up -d` (starts all services)
2. Run backend migrations: `cd backend && alembic upgrade head`
3. Seed data: `python scripts/seed_data.py`
4. Start frontend: `cd frontend && npm run dev`
5. Visit: http://localhost:5173 (app) + http://localhost:5173/ (marketing)

---

## License
Proprietary - Enterprise License Required for Production Use
© 2025 RetroRange Inc. All rights reserved.
