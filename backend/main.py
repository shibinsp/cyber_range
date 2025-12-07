from fastapi import FastAPI
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
