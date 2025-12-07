/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        // Retro Terminal Theme
        terminal: {
          bg: '#000000',
          panel: '#051014',
          'panel-light': '#0a1a20',
          primary: '#00FF7F', // Neon green
          'primary-dim': '#00cc66',
          accent: '#00C8FF', // Cyan
          'accent-dim': '#0099cc',
          neon: '#FF00FF', // Magenta/Pink
          'neon-dim': '#cc00cc',
          muted: '#1F1F1F',
          'muted-light': '#2a2a2a',
          danger: '#FF0033',
          'danger-dim': '#cc0029',
          warning: '#FFD700',
          'warning-dim': '#ccac00',
          success: '#00FF7F',
          info: '#00C8FF',
          border: '#00FF7F33',
          'border-dim': '#00FF7F1a',
          text: {
            primary: '#00FF7F',
            secondary: '#00C8FF',
            muted: '#808080',
            inverse: '#000000',
          },
        },
      },
      fontFamily: {
        retro: ['"Press Start 2P"', 'cursive'],
        terminal: ['"VT323"', 'monospace'],
        mono: ['"IBM Plex Mono"', 'Consolas', 'Monaco', 'monospace'],
        sans: ['system-ui', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
      },
      fontSize: {
        xxs: '0.65rem',
        xs: '0.75rem',
        sm: '0.875rem',
        base: '1rem',
        lg: '1.125rem',
        xl: '1.25rem',
        '2xl': '1.5rem',
        '3xl': '1.875rem',
        '4xl': '2.25rem',
        '5xl': '3rem',
        '6xl': '3.75rem',
        retro: {
          xs: '0.5rem',
          sm: '0.625rem',
          base: '0.75rem',
          lg: '1rem',
          xl: '1.25rem',
        },
      },
      animation: {
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'glow': 'glow 2s ease-in-out infinite alternate',
        'scan': 'scan 8s linear infinite',
        'flicker': 'flicker 0.15s infinite',
        'blink': 'blink 1s step-end infinite',
        'typewriter': 'typewriter 4s steps(40) 1s infinite',
        'slide-up': 'slideUp 0.5s ease-out',
        'slide-down': 'slideDown 0.5s ease-out',
        'fade-in': 'fadeIn 0.6s ease-out',
        'zoom-in': 'zoomIn 0.5s ease-out',
      },
      keyframes: {
        glow: {
          '0%': {
            textShadow: '0 0 5px #00FF7F, 0 0 10px #00FF7F, 0 0 15px #00FF7F',
            boxShadow: '0 0 5px #00FF7F, 0 0 10px #00FF7F',
          },
          '100%': {
            textShadow: '0 0 10px #00FF7F, 0 0 20px #00FF7F, 0 0 30px #00FF7F',
            boxShadow: '0 0 10px #00FF7F, 0 0 20px #00FF7F',
          },
        },
        scan: {
          '0%': { transform: 'translateY(-100%)' },
          '100%': { transform: 'translateY(100%)' },
        },
        flicker: {
          '0%, 100%': { opacity: '1' },
          '41.99%': { opacity: '1' },
          '42%': { opacity: '0.8' },
          '43%': { opacity: '1' },
          '45.99%': { opacity: '1' },
          '46%': { opacity: '0.8' },
          '46.99%': { opacity: '1' },
        },
        blink: {
          '0%, 50%': { opacity: '1' },
          '50.01%, 100%': { opacity: '0' },
        },
        typewriter: {
          '0%': { width: '0' },
          '50%': { width: '100%' },
          '100%': { width: '0' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        zoomIn: {
          '0%': { transform: 'scale(0.95)', opacity: '0' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
      },
      boxShadow: {
        'glow-sm': '0 0 5px currentColor, 0 0 10px currentColor',
        glow: '0 0 10px currentColor, 0 0 20px currentColor',
        'glow-lg': '0 0 15px currentColor, 0 0 30px currentColor',
        'glow-green': '0 0 10px #00FF7F, 0 0 20px #00FF7F, 0 0 30px #00FF7F',
        'glow-cyan': '0 0 10px #00C8FF, 0 0 20px #00C8FF, 0 0 30px #00C8FF',
        'glow-pink': '0 0 10px #FF00FF, 0 0 20px #FF00FF, 0 0 30px #FF00FF',
        retro: 'inset 0 0 0 1px #00FF7F, 0 0 10px #00FF7F33',
        'retro-hover': 'inset 0 0 0 2px #00FF7F, 0 0 15px #00FF7F66',
      },
      borderWidth: {
        3: '3px',
        5: '5px',
      },
      spacing: {
        18: '4.5rem',
        88: '22rem',
        100: '25rem',
        112: '28rem',
        128: '32rem',
      },
      backdropBlur: {
        xs: '2px',
      },
      backgroundImage: {
        'grid-pattern': "url('data:image/svg+xml,%3Csvg width=\"40\" height=\"40\" xmlns=\"http://www.w3.org/2000/svg\"%3E%3Cpath d=\"M0 20h40M20 0v40\" stroke=\"%2300FF7F\" stroke-width=\"0.5\" fill=\"none\" opacity=\"0.1\"/%3E%3C/svg%3E')",
        'scanline': "repeating-linear-gradient(0deg, rgba(0, 255, 127, 0.05) 0px, transparent 1px, transparent 2px, rgba(0, 255, 127, 0.05) 3px)",
        'crt-overlay': "repeating-linear-gradient(0deg, rgba(0, 0, 0, 0.15), rgba(0, 0, 0, 0.15) 1px, transparent 1px, transparent 2px)",
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
    // Custom plugin for CRT effects
    function ({ addUtilities }) {
      addUtilities({
        '.crt-effect': {
          position: 'relative',
          '&::before': {
            content: '""',
            position: 'absolute',
            top: '0',
            left: '0',
            width: '100%',
            height: '100%',
            background: 'repeating-linear-gradient(0deg, rgba(0, 0, 0, 0.15), rgba(0, 0, 0, 0.15) 1px, transparent 1px, transparent 2px)',
            pointerEvents: 'none',
            zIndex: '1000',
          },
        },
        '.text-glow': {
          textShadow: '0 0 10px currentColor, 0 0 20px currentColor',
        },
        '.text-glow-strong': {
          textShadow: '0 0 15px currentColor, 0 0 30px currentColor, 0 0 45px currentColor',
        },
        '.border-pixel': {
          borderStyle: 'solid',
          borderImage: 'repeating-linear-gradient(90deg, currentColor 0, currentColor 2px, transparent 2px, transparent 4px) 1',
        },
      })
    },
  ],
}
