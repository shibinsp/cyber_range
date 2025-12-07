import { Outlet } from 'react-router-dom'

export default function AppLayout() {
  return (
    <div className="min-h-screen bg-terminal-bg flex">
      <aside className="w-64 bg-terminal-panel border-r border-terminal-border p-4">
        <h2 className="font-retro text-terminal-primary">RETRORANGE</h2>
      </aside>
      <main className="flex-1 p-8"><Outlet /></main>
    </div>
  )
}
