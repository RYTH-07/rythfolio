import { inject } from '@vercel/analytics';
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './styles/fonts.css'
import './styles/globals.css'
import './styles/index.css'
import './styles/tailwind.css'
import './styles/theme.css'
import App from './app/App.tsx'

inject();

creatRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>
)