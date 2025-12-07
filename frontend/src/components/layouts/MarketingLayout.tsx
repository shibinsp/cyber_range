import { Outlet, Link } from 'react-router-dom'
import { Terminal } from 'lucide-react'

export default function MarketingLayout() {
  return (
    <div className="min-h-screen bg-terminal-bg">
      <header className="border-b border-terminal-border">
        <nav className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
          <Link to="/" className="flex items-center gap-2">
            <Terminal className="w-8 h-8 text-terminal-primary" />
            <span className="font-retro text-xl text-terminal-primary">RETRORANGE</span>
          </Link>
          <div className="flex gap-4">
            <Link to="/app/login" className="font-terminal text-sm text-terminal-primary">LOGIN</Link>
            <Link to="/app/register" className="btn-retro btn-retro-sm">SIGN_UP</Link>
          </div>
        </nav>
      </header>
      <main><Outlet /></main>
    </div>
  )
}
