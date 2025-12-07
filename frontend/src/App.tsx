import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import { useSelector } from 'react-redux'
import type { RootState } from './features/store'

// Marketing Pages
import LandingPage from './pages/marketing/LandingPage'
import AboutPage from './pages/marketing/AboutPage'
import UseCasesPage from './pages/marketing/UseCasesPage'
import PricingPage from './pages/marketing/PricingPage'
import ContactPage from './pages/marketing/ContactPage'
import TermsPage from './pages/marketing/TermsPage'
import PrivacyPage from './pages/marketing/PrivacyPage'

// App Pages
import LoginPage from './pages/app/auth/LoginPage'
import RegisterPage from './pages/app/auth/RegisterPage'
import DashboardPage from './pages/app/DashboardPage'
import TopologyPage from './pages/app/TopologyPage'
import ScenariosPage from './pages/app/scenarios/ScenariosPage'
import ScenarioBuilderPage from './pages/app/scenarios/ScenarioBuilderPage'
import ScenarioRunPage from './pages/app/scenarios/ScenarioRunPage'
import VMsPage from './pages/app/vms/VMsPage'
import SOCPage from './pages/app/soc/SOCPage'
import ReplayPage from './pages/app/replay/ReplayPage'
import ScoringPage from './pages/app/scoring/ScoringPage'
import AdminPage from './pages/app/admin/AdminPage'
import SettingsPage from './pages/app/SettingsPage'

// Layouts
import MarketingLayout from './components/layouts/MarketingLayout'
import AppLayout from './components/layouts/AppLayout'
import ProtectedRoute from './components/auth/ProtectedRoute'

function App() {
  const { isAuthenticated } = useSelector((state: RootState) => state.auth)

  return (
    <Router>
      <Routes>
        {/* Marketing Routes */}
        <Route element={<MarketingLayout />}>
          <Route path="/" element={<LandingPage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/use-cases" element={<UseCasesPage />} />
          <Route path="/pricing" element={<PricingPage />} />
          <Route path="/contact" element={<ContactPage />} />
          <Route path="/terms" element={<TermsPage />} />
          <Route path="/privacy" element={<PrivacyPage />} />
        </Route>

        {/* Auth Routes */}
        <Route path="/app/login" element={isAuthenticated ? <Navigate to="/app/dashboard" /> : <LoginPage />} />
        <Route path="/app/register" element={isAuthenticated ? <Navigate to="/app/dashboard" /> : <RegisterPage />} />

        {/* Protected App Routes */}
        <Route element={<ProtectedRoute><AppLayout /></ProtectedRoute>}>
          <Route path="/app/dashboard" element={<DashboardPage />} />
          <Route path="/app/topology" element={<TopologyPage />} />
          <Route path="/app/scenarios" element={<ScenariosPage />} />
          <Route path="/app/scenarios/new" element={<ScenarioBuilderPage />} />
          <Route path="/app/scenarios/:id/edit" element={<ScenarioBuilderPage />} />
          <Route path="/app/scenarios/:id/run" element={<ScenarioRunPage />} />
          <Route path="/app/vms" element={<VMsPage />} />
          <Route path="/app/soc" element={<SOCPage />} />
          <Route path="/app/replay" element={<ReplayPage />} />
          <Route path="/app/scoring" element={<ScoringPage />} />
          <Route path="/app/admin" element={<AdminPage />} />
          <Route path="/app/settings" element={<SettingsPage />} />
        </Route>

        {/* Catch-all redirect */}
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </Router>
  )
}

export default App
