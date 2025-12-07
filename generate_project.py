#!/usr/bin/env python3
"""
RetroRange - Project Generator Script
Generates all frontend, backend, and infrastructure files for the enterprise cyber range platform
"""

import os
from pathlib import Path
from typing import Dict, List

# Project root
BASE_DIR = Path(__file__).parent

def create_file(path: str, content: str):
    """Create a file with the given content, creating directories as needed"""
    file_path = BASE_DIR / path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content)
    print(f"✅ Created: {path}")

def generate_frontend_files():
    """Generate all frontend component and page files"""

    # Redux Store
    create_file("frontend/src/features/store.ts", """import { configureStore } from '@reduxjs/toolkit'
import authReducer from './auth/authSlice'
import scenariosReducer from './scenarios/scenariosSlice'
import vmsReducer from './vms/vmsSlice'
import uiReducer from './ui/uiSlice'

export const store = configureStore({
  reducer: {
    auth: authReducer,
    scenarios: scenariosReducer,
    vms: vmsReducer,
    ui: uiReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false,
    }),
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch
""")

    # Auth Slice
    create_file("frontend/src/features/auth/authSlice.ts", """import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface User {
  id: string
  email: string
  role: string
}

interface AuthState {
  user: User | null
  token: string | null
  isAuthenticated: boolean
  loading: boolean
}

const initialState: AuthState = {
  user: null,
  token: localStorage.getItem('token'),
  isAuthenticated: !!localStorage.getItem('token'),
  loading: false,
}

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    setCredentials: (state, action: PayloadAction<{ user: User; token: string }>) => {
      state.user = action.payload.user
      state.token = action.payload.token
      state.isAuthenticated = true
      localStorage.setItem('token', action.payload.token)
    },
    logout: (state) => {
      state.user = null
      state.token = null
      state.isAuthenticated = false
      localStorage.removeItem('token')
    },
  },
})

export const { setCredentials, logout } = authSlice.actions
export default authSlice.reducer
""")

    # UI Slice
    create_file("frontend/src/features/ui/uiSlice.ts", """import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface UIState {
  sidebarOpen: boolean
  commandPaletteOpen: boolean
  theme: 'retro' | 'dark' | 'light'
}

const initialState: UIState = {
  sidebarOpen: true,
  commandPaletteOpen: false,
  theme: 'retro',
}

const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    toggleSidebar: (state) => {
      state.sidebarOpen = !state.sidebarOpen
    },
    toggleCommandPalette: (state) => {
      state.commandPaletteOpen = !state.commandPaletteOpen
    },
    setTheme: (state, action: PayloadAction<'retro' | 'dark' | 'light'>) => {
      state.theme = action.payload
    },
  },
})

export const { toggleSidebar, toggleCommandPalette, setTheme } = uiSlice.actions
export default uiSlice.reducer
""")

    # Scenarios Slice
    create_file("frontend/src/features/scenarios/scenariosSlice.ts", """import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface Scenario {
  id: string
  name: string
  description: string
  status: 'draft' | 'active' | 'completed'
}

interface ScenariosState {
  scenarios: Scenario[]
  loading: boolean
}

const initialState: ScenariosState = {
  scenarios: [],
  loading: false,
}

const scenariosSlice = createSlice({
  name: 'scenarios',
  initialState,
  reducers: {
    setScenarios: (state, action: PayloadAction<Scenario[]>) => {
      state.scenarios = action.payload
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload
    },
  },
})

export const { setScenarios, setLoading } = scenariosSlice.actions
export default scenariosSlice.reducer
""")

    # VMs Slice
    create_file("frontend/src/features/vms/vmsSlice.ts", """import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface VM {
  id: string
  name: string
  status: 'running' | 'stopped' | 'error'
  ip: string
}

interface VMsState {
  vms: VM[]
  loading: boolean
}

const initialState: VMsState = {
  vms: [],
  loading: false,
}

const vmsSlice = createSlice({
  name: 'vms',
  initialState,
  reducers: {
    setVMs: (state, action: PayloadAction<VM[]>) => {
      state.vms = action.payload
    },
    updateVMStatus: (state, action: PayloadAction<{ id: string; status: string }>) => {
      const vm = state.vms.find(v => v.id === action.payload.id)
      if (vm) {
        vm.status = action.payload.status as any
      }
    },
  },
})

export const { setVMs, updateVMStatus } = vmsSlice.actions
export default vmsSlice.reducer
""")

    # API Service
    create_file("frontend/src/services/api.ts", """import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')
      window.location.href = '/app/login'
    }
    return Promise.reject(error)
  }
)

export default api
""")

    # Landing Page (Hero Marketing Page)
    create_file("frontend/src/pages/marketing/LandingPage.tsx", """import { Link } from 'react-router-dom'
import { Terminal, Zap, Shield, BarChart3, Play, ArrowRight } from 'lucide-react'

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-terminal-bg">
      {/* Hero Section */}
      <section className="relative overflow-hidden bg-neon-grid hero-gradient pt-20 pb-32">
        <div className="scanlines absolute inset-0 opacity-30" />

        <div className="section-container relative z-10">
          <div className="text-center max-w-4xl mx-auto">
            <h1 className="font-retro text-4xl md:text-5xl lg:text-6xl text-terminal-primary mb-6 animate-fade-in text-glow-green">
              RETRORANGE
            </h1>
            <p className="font-terminal text-xl md:text-2xl text-terminal-accent mb-4 animate-slide-up">
              &gt; ENTERPRISE_CYBER_RANGE.EXE
            </p>
            <p className="font-mono text-lg md:text-xl text-terminal-text-secondary mb-8 max-w-3xl mx-auto animate-slide-up delay-100">
              Automated scenario-based security training for SOCs, red/blue teams,
              and incident responders. Real attacks. Real defenses. Zero risk.
            </p>

            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center animate-slide-up delay-200">
              <Link to="/app/register" className="btn-retro btn-retro-lg group">
                <Play className="inline-block mr-2 w-5 h-5" />
                TRY DEMO
                <ArrowRight className="inline-block ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </Link>
              <Link to="/contact" className="btn-retro btn-retro-lg btn-retro-accent">
                <Terminal className="inline-block mr-2 w-5 h-5" />
                CONTACT SALES
              </Link>
            </div>

            {/* Terminal Demo */}
            <div className="mt-12 terminal-panel max-w-2xl mx-auto text-left animate-zoom-in delay-300">
              <div className="flex items-center gap-2 mb-4">
                <div className="w-3 h-3 rounded-full bg-terminal-danger"></div>
                <div className="w-3 h-3 rounded-full bg-terminal-warning"></div>
                <div className="w-3 h-3 rounded-full bg-terminal-success"></div>
                <span className="ml-auto font-terminal text-sm text-terminal-text-muted">
                  terminal.retrorange.com
                </span>
              </div>
              <div className="font-terminal text-sm space-y-2">
                <div><span className="text-terminal-accent">$</span> retrorange scenario create --type apt29</div>
                <div className="text-terminal-text-muted">[+] Provisioning infrastructure...</div>
                <div className="text-terminal-text-muted">[+] Deploying VMs (10/10)</div>
                <div className="text-terminal-success">[✓] Scenario ready. ID: scn_7f8a9b2c</div>
                <div><span className="text-terminal-accent">$</span> retrorange scenario start scn_7f8a9b2c</div>
                <div className="text-terminal-warning">[!] Attack sequence initiated</div>
                <div className="cursor-typewriter"></div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="section-container">
        <h2 className="font-retro text-3xl md:text-4xl text-center text-terminal-primary mb-16 text-glow-green">
          KEY_CAPABILITIES
        </h2>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {[
            {
              icon: Zap,
              title: 'Automated Scenarios',
              description: 'Pre-built attack chains from MITRE ATT&CK. Deploy in minutes, not days.',
            },
            {
              icon: Shield,
              title: 'Enterprise Orchestration',
              description: 'Terraform + Ansible + CALDERA. Full infrastructure-as-code.',
            },
            {
              icon: BarChart3,
              title: 'Real-time Telemetry',
              description: 'Live SIEM integration. Elasticsearch + Kibana dashboards.',
            },
            {
              icon: Terminal,
              title: 'Scoring & Replay',
              description: 'Automated scoring. Frame-by-frame PCAP replay with timeline.',
            },
          ].map((feature, idx) => (
            <div key={idx} className="card-retro group">
              <feature.icon className="w-12 h-12 text-terminal-primary mb-4 group-hover:text-terminal-accent transition-colors" />
              <h3 className="font-terminal text-lg text-terminal-primary mb-2 uppercase">
                {feature.title}
              </h3>
              <p className="font-mono text-sm text-terminal-text-secondary">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* Pricing Teaser */}
      <section className="section-container bg-terminal-panel/30">
        <h2 className="font-retro text-3xl md:text-4xl text-center text-terminal-primary mb-8 text-glow-green">
          PRICING_TIERS
        </h2>
        <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          {[
            { name: 'FREE_EVAL', price: '$0', features: ['1 Concurrent Scenario', '5 VMs', '7-Day Trial'] },
            { name: 'TEAM', price: '$499', popular: true, features: ['10 Scenarios', '50 VMs', 'SIEM Integration'] },
            { name: 'ENTERPRISE', price: 'Custom', features: ['Unlimited', 'On-Prem', 'White-Label'] },
          ].map((tier, idx) => (
            <div key={idx} className={`card-retro text-center ${tier.popular ? 'border-terminal-neon' : ''}`}>
              {tier.popular && (
                <div className="badge-retro bg-terminal-neon text-terminal-bg mb-4">MOST_POPULAR</div>
              )}
              <h3 className="font-terminal text-2xl text-terminal-primary mb-2">{tier.name}</h3>
              <p className="font-retro text-4xl text-terminal-accent mb-6">{tier.price}</p>
              <ul className="space-y-2 mb-6 font-mono text-sm text-terminal-text-secondary">
                {tier.features.map((f, i) => (
                  <li key={i}>&gt; {f}</li>
                ))}
              </ul>
              <Link to="/pricing" className="btn-retro w-full">
                SELECT
              </Link>
            </div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="section-container text-center">
        <div className="terminal-panel max-w-3xl mx-auto">
          <h2 className="font-terminal text-2xl md:text-3xl text-terminal-primary mb-4">
            &gt; READY_TO_DEPLOY?
          </h2>
          <p className="font-mono text-lg text-terminal-text-secondary mb-8">
            Join 500+ security teams training on RetroRange.
          </p>
          <Link to="/app/register" className="btn-retro btn-retro-lg">
            START_FREE_TRIAL
          </Link>
        </div>
      </section>
    </div>
  )
}
""")

    print("✅ Frontend files generated")

def generate_backend_files():
    """Generate backend FastAPI files"""

    # Backend directory structure
    os.makedirs(BASE_DIR / "backend/app/api/v1", exist_ok=True)
    os.makedirs(BASE_DIR / "backend/app/core", exist_ok=True)
    os.makedirs(BASE_DIR / "backend/app/models", exist_ok=True)
    os.makedirs(BASE_DIR / "backend/app/schemas", exist_ok=True)
    os.makedirs(BASE_DIR / "backend/app/services", exist_ok=True)
    os.makedirs(BASE_DIR / "backend/app/workers", exist_ok=True)
    os.makedirs(BASE_DIR / "backend/app/db", exist_ok=True)
    os.makedirs(BASE_DIR / "backend/alembic/versions", exist_ok=True)
    os.makedirs(BASE_DIR / "backend/scripts", exist_ok=True)
    os.makedirs(BASE_DIR / "backend/tests/unit", exist_ok=True)

    # Main FastAPI app
    create_file("backend/main.py", """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1 import auth, users, scenarios, vms, topology, logs, scoring

app = FastAPI(
    title="RetroRange API",
    description="Enterprise Cyber Range Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(scenarios.router, prefix="/api/v1/scenarios", tags=["scenarios"])
app.include_router(vms.router, prefix="/api/v1/vms", tags=["vms"])
app.include_router(topology.router, prefix="/api/v1/topology", tags=["topology"])
app.include_router(logs.router, prefix="/api/v1/logs", tags=["logs"])
app.include_router(scoring.router, prefix="/api/v1/scoring", tags=["scoring"])

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "retrorange-api"}

@app.get("/")
async def root():
    return {"message": "RetroRange API v1.0.0"}
""")

    # Config
    create_file("backend/app/core/config.py", """from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App
    APP_NAME: str = "RetroRange"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:shibin@localhost:5432/range"

    # Security
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

    # CORS
    CORS_ORIGINS: list = ["http://localhost:5173", "http://localhost:3000"]

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # Elasticsearch
    ELASTICSEARCH_URL: str = "http://localhost:9200"

    # MinIO
    MINIO_ENDPOINT: str = "localhost:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"

    class Config:
        env_file = ".env"

settings = Settings()
""")

    # Database session
    create_file("backend/app/db/session.py", """from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG, future=True)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
""")

    # User model
    create_file("backend/app/models/user.py", """from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_login = Column(DateTime(timezone=True))
    metadata = Column(JSONB, default={})
""")

    # Requirements
    create_file("backend/requirements.txt", """fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy[asyncio]==2.0.23
asyncpg==0.29.0
alembic==1.12.1
pydantic==2.5.2
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
redis==5.0.1
celery==5.3.4
elasticsearch==8.11.0
minio==7.2.0
httpx==0.25.2
python-dotenv==1.0.0
pytest==7.4.3
pytest-asyncio==0.21.1
""")

    # pyproject.toml
    create_file("backend/pyproject.toml", """[project]
name = "retrorange-backend"
version = "1.0.0"
description = "RetroRange Backend API"
requires-python = ">=3.11"

[tool.black]
line-length = 100
target-version = ['py311']

[tool.ruff]
line-length = 100
select = ["E", "F", "I"]

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
""")

    print("✅ Backend files generated")

def generate_infrastructure_files():
    """Generate infrastructure and DevOps files"""

    # Terraform main
    create_file("infra/terraform/main.tf", """terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC Module
module "vpc" {
  source = "./modules/networking"

  vpc_cidr = var.vpc_cidr
  environment = var.environment
}

# EKS Cluster
module "eks" {
  source = "./modules/k8s"

  cluster_name = "retrorange-${var.environment}"
  vpc_id = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnet_ids
}
""")

    # Docker backend
    create_file("infra/docker/backend.Dockerfile", """FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    postgresql-client \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY backend/ .

# Run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
""")

    # Helm values
    create_file("infra/kubernetes/helm/values.yaml", """# RetroRange Helm Chart Values

replicaCount: 2

image:
  backend:
    repository: retrorange/backend
    tag: latest
    pullPolicy: IfNotPresent
  frontend:
    repository: retrorange/frontend
    tag: latest
    pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: retrorange.example.com
      paths:
        - path: /
          pathType: Prefix

postgresql:
  enabled: true
  auth:
    database: range
    username: postgres
    password: shibin

redis:
  enabled: true
  auth:
    enabled: false

elasticsearch:
  enabled: true
  replicas: 3
""")

    # GitHub Actions CI
    create_file(".github/workflows/ci.yml", """name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          cd backend
          pip install -r requirements.txt
      - name: Run tests
        run: |
          cd backend
          pytest tests/ -v

  test-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
      - name: Install dependencies
        run: |
          cd frontend
          npm ci
      - name: Run tests
        run: |
          cd frontend
          npm run test

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Lint backend
        run: |
          cd backend
          pip install ruff black mypy
          ruff check .
          black --check .
      - name: Lint frontend
        run: |
          cd frontend
          npm ci
          npm run lint
""")

    print("✅ Infrastructure files generated")

def main():
    """Main generator function"""
    print("🚀 Generating RetroRange project files...")
    print("=" * 60)

    generate_frontend_files()
    generate_backend_files()
    generate_infrastructure_files()

    print("=" * 60)
    print("✅ Project generation complete!")
    print()
    print("Next steps:")
    print("1. cd frontend && npm install")
    print("2. cd backend && pip install -r requirements.txt")
    print("3. docker-compose up -d")
    print("4. make quickstart")

if __name__ == "__main__":
    main()
