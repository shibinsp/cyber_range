import { Link } from 'react-router-dom'
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
