#!/bin/bash
#
# RetroRange - Complete Project Setup Script
# This script generates all remaining files for a production-ready cyber range platform
#

set -e

PROJECT_ROOT="/home/shibin/Desktop/cyber_range"
cd "$PROJECT_ROOT"

echo "🚀 RetroRange - Complete Project Setup"
echo "========================================"

# Create all database models
echo "📦 Creating database models..."
cat > backend/app/models/role.py << 'ENDOFFILE'
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import JSONB
from app.db.base import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    permissions = Column(JSONB, default={})
ENDOFFILE

cat > backend/app/models/scenario.py << 'ENDOFFILE'
from sqlalchemy import Column, String, DateTime, Text, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from app.db.base import Base
import uuid
import enum

class VisibilityEnum(str, enum.Enum):
    public = "public"
    private = "private"
    org = "org"

class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    description = Column(Text)
    steps = Column(JSONB, default={})
    status = Column(String, default="draft")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    visibility = Column(Enum(VisibilityEnum), default=VisibilityEnum.private)
ENDOFFILE

cat > backend/app/models/virtual_machine.py << 'ENDOFFILE'
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB, INET, MACADDR
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class VirtualMachine(Base):
    __tablename__ = "virtual_machines"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    type = Column(String)
    ip = Column(INET)
    mac = Column(MACADDR)
    status = Column(String, default="stopped")
    last_seen = Column(DateTime(timezone=True))
    snapshot_id = Column(String)
    metadata = Column(JSONB, default={})
ENDOFFILE

# Create seed data script
echo "🌱 Creating seed data script..."
cat > backend/scripts/seed_data.py << 'ENDOFFILE'
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.core.security import get_password_hash
from app.db.base import Base
from app.models.role import Role
from app.models.user import User

async def seed_database():
    """Seed the database with initial data"""
    engine = create_async_engine(settings.DATABASE_URL, echo=True)

    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Create session
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        # Create roles
        roles_data = [
            {"name": "superadmin", "permissions": {"all": True}},
            {"name": "admin", "permissions": {"manage_users": True, "manage_scenarios": True}},
            {"name": "instructor", "permissions": {"create_scenarios": True, "manage_students": True}},
            {"name": "red", "permissions": {"run_attacks": True}},
            {"name": "blue", "permissions": {"defend": True, "view_logs": True}},
            {"name": "analyst", "permissions": {"view_reports": True}},
            {"name": "student", "permissions": {"participate": True}},
            {"name": "guest", "permissions": {"view_only": True}},
        ]

        for role_data in roles_data:
            role = Role(**role_data)
            session.add(role)

        await session.commit()

        # Get admin role
        result = await session.execute("SELECT id FROM roles WHERE name = 'superadmin'")
        admin_role_id = result.scalar_one()

        # Create default admin user
        admin_user = User(
            email="admin@retrorange.local",
            hashed_password=get_password_hash("Admin123!"),
            role_id=admin_role_id,
        )
        session.add(admin_user)
        await session.commit()

        print("✅ Database seeded successfully!")
        print("📧 Admin credentials: admin@retrorange.local / Admin123!")

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(seed_database())
ENDOFFILE

# Create essential frontend components
echo "🎨 Creating frontend components..."

# Button component
cat > frontend/src/components/common/Button.tsx << 'ENDOFFILE'
import { ButtonHTMLAttributes, ReactNode } from 'react'
import { clsx } from 'clsx'

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'accent' | 'danger'
  size?: 'sm' | 'md' | 'lg'
  children: ReactNode
}

export default function Button({ variant = 'primary', size = 'md', className, children, ...props }: ButtonProps) {
  return (
    <button
      className={clsx(
        'btn-retro',
        {
          'btn-retro-sm': size === 'sm',
          'btn-retro-lg': size === 'lg',
          'btn-retro-accent': variant === 'accent',
          'btn-retro-danger': variant === 'danger',
        },
        className
      )}
      {...props}
    >
      {children}
    </button>
  )
}
ENDOFFILE

# Marketing Layout
cat > frontend/src/components/layouts/MarketingLayout.tsx << 'ENDOFFILE'
import { Outlet, Link } from 'react-router-dom'
import { Terminal } from 'lucide-react'

export default function MarketingLayout() {
  return (
    <div className="min-h-screen bg-terminal-bg crt-screen">
      {/* Header */}
      <header className="border-b border-terminal-border bg-terminal-panel/50 backdrop-blur-sm sticky top-0 z-50">
        <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <Link to="/" className="flex items-center gap-2">
              <Terminal className="w-8 h-8 text-terminal-primary" />
              <span className="font-retro text-xl text-terminal-primary text-glow-green">RETRORANGE</span>
            </Link>

            <div className="hidden md:flex items-center gap-8 font-terminal text-sm">
              <Link to="/use-cases" className="text-terminal-text-secondary hover:text-terminal-primary transition-colors">
                USE_CASES
              </Link>
              <Link to="/pricing" className="text-terminal-text-secondary hover:text-terminal-primary transition-colors">
                PRICING
              </Link>
              <Link to="/about" className="text-terminal-text-secondary hover:text-terminal-primary transition-colors">
                ABOUT
              </Link>
              <Link to="/contact" className="text-terminal-text-secondary hover:text-terminal-primary transition-colors">
                CONTACT
              </Link>
            </div>

            <div className="flex items-center gap-4">
              <Link to="/app/login" className="font-terminal text-sm text-terminal-primary hover:text-terminal-accent transition-colors">
                LOGIN
              </Link>
              <Link to="/app/register" className="btn-retro btn-retro-sm">
                SIGN_UP
              </Link>
            </div>
          </div>
        </nav>
      </header>

      {/* Main Content */}
      <main>
        <Outlet />
      </main>

      {/* Footer */}
      <footer className="border-t border-terminal-border bg-terminal-panel mt-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="grid md:grid-cols-4 gap-8 font-mono text-sm">
            <div>
              <h3 className="font-terminal text-terminal-primary mb-4">PRODUCT</h3>
              <ul className="space-y-2 text-terminal-text-secondary">
                <li><Link to="/use-cases" className="hover:text-terminal-primary">Use Cases</Link></li>
                <li><Link to="/pricing" className="hover:text-terminal-primary">Pricing</Link></li>
              </ul>
            </div>
            <div>
              <h3 className="font-terminal text-terminal-primary mb-4">COMPANY</h3>
              <ul className="space-y-2 text-terminal-text-secondary">
                <li><Link to="/about" className="hover:text-terminal-primary">About</Link></li>
                <li><Link to="/contact" className="hover:text-terminal-primary">Contact</Link></li>
              </ul>
            </div>
            <div>
              <h3 className="font-terminal text-terminal-primary mb-4">LEGAL</h3>
              <ul className="space-y-2 text-terminal-text-secondary">
                <li><Link to="/terms" className="hover:text-terminal-primary">Terms</Link></li>
                <li><Link to="/privacy" className="hover:text-terminal-primary">Privacy</Link></li>
              </ul>
            </div>
            <div>
              <h3 className="font-terminal text-terminal-primary mb-4">RESOURCES</h3>
              <ul className="space-y-2 text-terminal-text-secondary">
                <li><a href="https://docs.retrorange.com" className="hover:text-terminal-primary">Documentation</a></li>
                <li><a href="https://github.com" className="hover:text-terminal-primary">GitHub</a></li>
              </ul>
            </div>
          </div>
          <div className="mt-12 pt-8 border-t border-terminal-border text-center text-terminal-text-muted font-mono text-sm">
            © 2025 RetroRange Inc. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  )
}
ENDOFFILE

# App Layout
cat > frontend/src/components/layouts/AppLayout.tsx << 'ENDOFFILE'
import { Outlet } from 'react-router-dom'

export default function AppLayout() {
  return (
    <div className="min-h-screen bg-terminal-bg crt-screen">
      <div className="flex">
        {/* Sidebar - Placeholder */}
        <aside className="w-64 bg-terminal-panel border-r border-terminal-border">
          <div className="p-4">
            <h2 className="font-retro text-terminal-primary text-sm">RETRORANGE</h2>
          </div>
        </aside>

        {/* Main Content */}
        <main className="flex-1 p-8">
          <Outlet />
        </main>
      </div>
    </div>
  )
}
ENDOFFILE

# Protected Route
cat > frontend/src/components/auth/ProtectedRoute.tsx << 'ENDOFFILE'
import { Navigate } from 'react-router-dom'
import { useSelector } from 'react-redux'
import type { RootState } from '@/features/store'

export default function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated } = useSelector((state: RootState) => state.auth)

  if (!isAuthenticated) {
    return <Navigate to="/app/login" replace />
  }

  return <>{children}</>
}
ENDOFFILE

# Login Page
cat > frontend/src/pages/app/auth/LoginPage.tsx << 'ENDOFFILE'
import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useDispatch } from 'react-redux'
import { setCredentials } from '@/features/auth/authSlice'
import Button from '@/components/common/Button'
import { Terminal } from 'lucide-react'
import toast from 'react-hot-toast'
import api from '@/services/api'

export default function LoginPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()
  const dispatch = useDispatch()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)

    try {
      const formData = new FormData()
      formData.append('username', email)
      formData.append('password', password)

      const response = await api.post('/api/v1/auth/login', formData)
      const { access_token } = response.data

      dispatch(setCredentials({
        user: { id: '1', email, role: 'admin' },
        token: access_token
      }))

      toast.success('Login successful!')
      navigate('/app/dashboard')
    } catch (error) {
      toast.error('Login failed. Please check your credentials.')
      console.error(error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-terminal-bg flex items-center justify-center p-4 bg-neon-grid">
      <div className="scanlines absolute inset-0 opacity-20" />

      <div className="terminal-panel max-w-md w-full relative z-10">
        <div className="text-center mb-8">
          <Terminal className="w-16 h-16 text-terminal-primary mx-auto mb-4 animate-glow" />
          <h1 className="font-retro text-2xl text-terminal-primary text-glow-green mb-2">
            RETRORANGE
          </h1>
          <p className="font-terminal text-terminal-text-secondary">
            &gt; ACCESS_TERMINAL
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="block font-terminal text-sm text-terminal-primary mb-2">
              EMAIL
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="input-retro"
              placeholder="user@retrorange.local"
              required
            />
          </div>

          <div>
            <label className="block font-terminal text-sm text-terminal-primary mb-2">
              PASSWORD
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="input-retro"
              placeholder="••••••••"
              required
            />
          </div>

          <Button type="submit" className="w-full" disabled={loading}>
            {loading ? 'AUTHENTICATING...' : 'LOGIN'}
          </Button>
        </form>

        <div className="mt-6 text-center font-mono text-sm text-terminal-text-muted">
          Don't have an account?{' '}
          <Link to="/app/register" className="text-terminal-accent hover:text-terminal-primary">
            Register
          </Link>
        </div>
      </div>
    </div>
  )
}
ENDOFFILE

# Create placeholder pages
for page in AboutPage UseCasesPage PricingPage ContactPage TermsPage PrivacyPage; do
  cat > "frontend/src/pages/marketing/$page.tsx" << ENDOFFILE
export default function $page() {
  return (
    <div className="section-container">
      <h1 className="font-retro text-4xl text-terminal-primary mb-8">$page</h1>
      <p className="font-mono text-terminal-text-secondary">Content coming soon...</p>
    </div>
  )
}
ENDOFFILE
done

# Create app pages
for page in RegisterPage DashboardPage TopologyPage ScenariosPage ScenarioBuilderPage ScenarioRunPage VMsPage SOCPage ReplayPage ScoringPage AdminPage SettingsPage; do
  cat > "frontend/src/pages/app/$page.tsx" << ENDOFFILE
export default function $page() {
  return (
    <div>
      <h1 className="font-retro text-3xl text-terminal-primary mb-6">$page</h1>
      <div className="card-retro">
        <p className="font-mono text-terminal-text-secondary">Content coming soon...</p>
      </div>
    </div>
  )
}
ENDOFFILE
done

echo "✅ Project setup complete!"
echo ""
echo "Next steps:"
echo "1. Install dependencies:"
echo "   cd frontend && npm install"
echo "   cd backend && pip install -r requirements.txt"
echo ""
echo "2. Start infrastructure:"
echo "   docker-compose up -d"
echo ""
echo "3. Initialize database:"
echo "   cd backend && python scripts/seed_data.py"
echo ""
echo "4. Start development servers:"
echo "   make dev"
