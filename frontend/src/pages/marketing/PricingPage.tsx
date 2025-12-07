import { Link } from 'react-router-dom'

export default function PricingPage() {
  return (
    <div className="min-h-screen bg-terminal-bg">
      {/* Hero Section with Background Effects */}
      <section className="relative overflow-hidden bg-terminal-bg bg-neon-grid hero-gradient pt-20 pb-16">
        <div className="scanlines absolute inset-0 opacity-30" />
        <div className="section-container relative z-10">
          <div className="text-center max-w-4xl mx-auto">
            {/* Intro Text */}
            <p className="font-mono text-lg md:text-xl text-terminal-text-secondary mb-8 animate-fade-in">
              Automated scoring. Frame-by-frame PCAP replay with timeline.
            </p>
            
            {/* Pricing Tiers */}
            <h1 className="font-retro text-3xl md:text-4xl lg:text-5xl text-terminal-primary mb-12 text-glow-green animate-fade-in delay-100">
              PRICING_TIERS
            </h1>
          </div>
        </div>
      </section>

      {/* Pricing Cards */}
      <section className="section-container -mt-8">
        <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          {[
            { name: 'FREE_EVAL', price: '$0', features: ['1 Concurrent Scenario', '5 VMs', '7-Day Trial'] },
            { name: 'TEAM', price: '$499', popular: true, features: ['10 Scenarios', '50 VMs', 'SIEM Integration'] },
            { name: 'ENTERPRISE', price: 'Custom', features: ['Unlimited', 'On-Prem', 'White-Label'] },
          ].map((tier, idx) => (
            <div 
              key={idx} 
              className={`card-retro text-center transition-all duration-300 animate-slide-up ${tier.popular ? 'border-terminal-neon shadow-glow-pink' : ''}`}
              style={{ animationDelay: `${(idx + 1) * 100}ms` }}
            >
              {tier.popular && (
                <div className="badge-retro bg-terminal-neon text-terminal-bg mb-4 mx-auto">MOST_POPULAR</div>
              )}
              <h3 className="font-terminal text-2xl text-terminal-primary mb-2">{tier.name}</h3>
              {tier.price === 'Custom' ? (
                <p className="font-retro text-2xl text-terminal-accent mb-2">Custom</p>
              ) : (
                <p className="font-retro text-4xl text-terminal-accent mb-6">{tier.price}</p>
              )}
              <ul className="space-y-2 mb-6 font-mono text-sm text-terminal-text-secondary text-left">
                {tier.features.map((f, i) => (
                  <li key={i}>&gt; {f}</li>
                ))}
              </ul>
              <Link to="/app/register" className="btn-retro w-full block text-center">
                SELECT
              </Link>
            </div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="section-container text-center pb-20">
        <div className="terminal-panel max-w-3xl mx-auto animate-fade-in delay-300">
          <h2 className="font-terminal text-2xl md:text-3xl text-terminal-primary mb-4">
            &gt; READY_TO_DEPLOY?
          </h2>
          <p className="font-mono text-lg text-terminal-text-secondary mb-8">
            Join 500+ security teams training on RetroRange.
          </p>
          <Link to="/app/register" className="btn-retro btn-retro-lg inline-block">
            START FREE TRIAL
          </Link>
        </div>
      </section>
    </div>
  )
}
