.PHONY: help setup dev test lint clean migrate seed deploy-staging deploy-prod docker-up docker-down

# RetroRange - Development Commands
# =============================================================================

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# =============================================================================
# Setup & Installation
# =============================================================================

setup: ## Install all dependencies (backend + frontend)
	@echo "📦 Installing backend dependencies..."
	cd backend && pip install -r requirements.txt
	@echo "📦 Installing frontend dependencies..."
	cd frontend && npm install
	@echo "✅ Setup complete!"

setup-backend: ## Install backend dependencies only
	cd backend && pip install -r requirements.txt

setup-frontend: ## Install frontend dependencies only
	cd frontend && npm install

# =============================================================================
# Development
# =============================================================================

dev: ## Start all services in development mode
	@echo "🚀 Starting development environment..."
	docker-compose up -d
	@echo "⏳ Waiting for services to be healthy..."
	sleep 10
	@echo "🔧 Starting backend (in background)..."
	cd backend && uvicorn main:app --reload --port 8000 &
	@echo "🎨 Starting frontend..."
	cd frontend && npm run dev

dev-backend: ## Start backend only
	cd backend && uvicorn main:app --reload --port 8000

dev-frontend: ## Start frontend only
	cd frontend && npm run dev

dev-workers: ## Start Celery workers
	cd backend && celery -A app.workers.tasks worker --loglevel=info

# =============================================================================
# Docker
# =============================================================================

docker-up: ## Start all Docker services
	docker-compose up -d
	@echo "⏳ Waiting for services..."
	sleep 10
	docker-compose ps

docker-down: ## Stop all Docker services
	docker-compose down

docker-logs: ## Show Docker logs
	docker-compose logs -f

docker-clean: ## Remove all containers, volumes, and images
	docker-compose down -v --rmi all

# =============================================================================
# Database
# =============================================================================

migrate: ## Run database migrations
	cd backend && alembic upgrade head

migrate-create: ## Create new migration (usage: make migrate-create MSG="description")
	cd backend && alembic revision --autogenerate -m "$(MSG)"

migrate-rollback: ## Rollback last migration
	cd backend && alembic downgrade -1

seed: ## Seed database with initial data
	cd backend && python scripts/seed_data.py

db-reset: ## Reset database (drop, create, migrate, seed)
	@echo "⚠️  This will delete all data. Press Ctrl+C to cancel..."
	sleep 3
	docker-compose down postgres
	docker volume rm cyber_range_postgres_data || true
	docker-compose up -d postgres
	sleep 5
	$(MAKE) migrate
	$(MAKE) seed

# =============================================================================
# Testing
# =============================================================================

test: ## Run all tests
	$(MAKE) test-backend
	$(MAKE) test-frontend

test-backend: ## Run backend tests
	cd backend && pytest tests/ -v --cov=app --cov-report=html

test-frontend: ## Run frontend tests
	cd frontend && npm run test

test-e2e: ## Run E2E tests
	cd frontend && npm run test:e2e

test-coverage: ## Generate coverage report
	cd backend && pytest tests/ --cov=app --cov-report=html
	cd frontend && npm run test:coverage
	@echo "📊 Coverage reports generated in backend/htmlcov and frontend/coverage"

# =============================================================================
# Code Quality
# =============================================================================

lint: ## Run all linters
	$(MAKE) lint-backend
	$(MAKE) lint-frontend

lint-backend: ## Lint backend code
	cd backend && ruff check .
	cd backend && black --check .
	cd backend && mypy .

lint-frontend: ## Lint frontend code
	cd frontend && npm run lint

format: ## Format all code
	$(MAKE) format-backend
	$(MAKE) format-frontend

format-backend: ## Format backend code
	cd backend && black .
	cd backend && ruff check --fix .

format-frontend: ## Format frontend code
	cd frontend && npm run format

# =============================================================================
# Build
# =============================================================================

build: ## Build all components
	$(MAKE) build-frontend
	$(MAKE) build-backend

build-frontend: ## Build frontend for production
	cd frontend && npm run build

build-backend: ## Build backend Docker image
	docker build -f infra/docker/backend.Dockerfile -t retrorange/backend:latest .

build-worker: ## Build worker Docker image
	docker build -f infra/docker/worker.Dockerfile -t retrorange/worker:latest .

# =============================================================================
# Deployment
# =============================================================================

deploy-staging: ## Deploy to staging environment
	@echo "🚀 Deploying to staging..."
	cd infra/terraform/environments/staging && terraform apply
	cd infra/kubernetes/helm && helm upgrade --install retrorange . -f values-staging.yaml

deploy-prod: ## Deploy to production (requires confirmation)
	@echo "⚠️  Deploying to PRODUCTION. Press Ctrl+C to cancel..."
	sleep 5
	cd infra/terraform/environments/prod && terraform apply
	cd infra/kubernetes/helm && helm upgrade --install retrorange . -f values-prod.yaml

# =============================================================================
# Utilities
# =============================================================================

clean: ## Clean build artifacts and caches
	@echo "🧹 Cleaning build artifacts..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "node_modules" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "build" -exec rm -rf {} + 2>/dev/null || true
	rm -rf frontend/dist backend/htmlcov frontend/coverage
	@echo "✅ Clean complete!"

logs: ## Show application logs
	@echo "📋 Backend logs:"
	tail -f backend/logs/app.log

shell-backend: ## Open Python shell with app context
	cd backend && python -m IPython

shell-db: ## Open PostgreSQL shell
	docker-compose exec postgres psql -U postgres -d range

shell-redis: ## Open Redis CLI
	docker-compose exec redis redis-cli

# =============================================================================
# Monitoring
# =============================================================================

ps: ## Show running processes
	docker-compose ps

health: ## Check health of all services
	@echo "🏥 Checking service health..."
	@curl -s http://localhost:8000/health || echo "❌ Backend unhealthy"
	@curl -s http://localhost:9200/_cluster/health || echo "❌ Elasticsearch unhealthy"
	@curl -s http://localhost:9000/minio/health/live || echo "❌ MinIO unhealthy"
	@redis-cli -h localhost ping || echo "❌ Redis unhealthy"

stats: ## Show Docker stats
	docker stats --no-stream

# =============================================================================
# Documentation
# =============================================================================

docs-api: ## Open API documentation
	@echo "📖 Opening API docs at http://localhost:8000/docs"
	open http://localhost:8000/docs || xdg-open http://localhost:8000/docs

docs-serve: ## Serve documentation locally
	@echo "📖 Serving documentation at http://localhost:8080"
	cd docs && python -m http.server 8080

# =============================================================================
# Security
# =============================================================================

security-scan: ## Run security scans
	@echo "🔒 Running security scans..."
	cd backend && safety check
	cd frontend && npm audit
	trivy image retrorange/backend:latest

# =============================================================================
# Backup & Restore
# =============================================================================

backup-db: ## Backup database
	@echo "💾 Backing up database..."
	docker-compose exec -T postgres pg_dump -U postgres range > backups/db_$(shell date +%Y%m%d_%H%M%S).sql
	@echo "✅ Backup complete!"

restore-db: ## Restore database (usage: make restore-db FILE=backups/db_20240101_120000.sql)
	@echo "⚠️  This will overwrite the current database. Press Ctrl+C to cancel..."
	sleep 3
	docker-compose exec -T postgres psql -U postgres range < $(FILE)
	@echo "✅ Restore complete!"

# =============================================================================
# Quick Start
# =============================================================================

quickstart: ## Complete setup and start (first-time setup)
	@echo "🎬 QuickStart: Setting up RetroRange..."
	$(MAKE) docker-up
	sleep 10
	$(MAKE) setup
	$(MAKE) migrate
	$(MAKE) seed
	@echo "✅ Setup complete! Starting development servers..."
	$(MAKE) dev

# Default target
.DEFAULT_GOAL := help
