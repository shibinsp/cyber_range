-- RetroRange Database Initialization
-- This script runs automatically when PostgreSQL container starts

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";  -- For text search

-- Grant permissions
GRANT ALL PRIVILEGES ON DATABASE range TO postgres;

-- Create initial schema (Alembic will manage migrations after this)
-- This is just to ensure the database is properly set up
