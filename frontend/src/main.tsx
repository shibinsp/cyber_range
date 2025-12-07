import React from 'react'
import ReactDOM from 'react-dom/client'
import { Provider } from 'react-redux'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import { Toaster } from 'react-hot-toast'
import App from './App'
import { store } from './features/store'
import './styles/index.css'

// Configure React Query
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: 1,
      staleTime: 5 * 60 * 1000, // 5 minutes
    },
  },
})

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Provider store={store}>
      <QueryClientProvider client={queryClient}>
        <App />
        <Toaster
          position="top-right"
          toastOptions={{
            duration: 4000,
            style: {
              background: '#051014',
              color: '#00FF7F',
              border: '1px solid #00FF7F',
              fontFamily: 'IBM Plex Mono, monospace',
            },
            success: {
              iconTheme: {
                primary: '#00FF7F',
                secondary: '#000',
              },
            },
            error: {
              iconTheme: {
                primary: '#FF0033',
                secondary: '#000',
              },
              style: {
                border: '1px solid #FF0033',
                color: '#FF0033',
              },
            },
          }}
        />
        {import.meta.env.DEV && <ReactQueryDevtools initialIsOpen={false} />}
      </QueryClientProvider>
    </Provider>
  </React.StrictMode>
)
