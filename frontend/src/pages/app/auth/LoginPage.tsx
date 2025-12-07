import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useDispatch } from 'react-redux'
import { setCredentials } from '@/features/auth/authSlice'
import Button from '@/components/common/Button'
import { Terminal } from 'lucide-react'

export default function LoginPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()
  const dispatch = useDispatch()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    // Demo: auto-login
    dispatch(setCredentials({ user: { id: '1', email, role: 'admin' }, token: 'demo_token' }))
    navigate('/app/dashboard')
  }

  return (
    <div className="min-h-screen bg-terminal-bg flex items-center justify-center p-4">
      <div className="terminal-panel max-w-md w-full">
        <div className="text-center mb-8">
          <Terminal className="w-16 h-16 text-terminal-primary mx-auto mb-4" />
          <h1 className="font-retro text-2xl text-terminal-primary">RETRORANGE</h1>
        </div>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="block font-terminal text-sm text-terminal-primary mb-2">EMAIL</label>
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} className="input-retro" required />
          </div>
          <div>
            <label className="block font-terminal text-sm text-terminal-primary mb-2">PASSWORD</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className="input-retro" required />
          </div>
          <Button type="submit" className="w-full">LOGIN</Button>
        </form>
        <div className="mt-6 text-center font-mono text-sm">
          <Link to="/app/register" className="text-terminal-accent">Register</Link>
        </div>
      </div>
    </div>
  )
}
