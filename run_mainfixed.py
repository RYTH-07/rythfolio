with open('write_mainfixed.py', 'w', encoding='utf-8') as s:
    s.write("""
code = '''import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { inject } from '@vercel/analytics'
import './styles/fonts.css'
import './styles/globals.css'
import './styles/index.css'
import './styles/tailwind.css'
import './styles/theme.css'
import App from './app/App.tsx'

inject()

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>
)'''
with open('src/main.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('main.tsx fixed!')
""")
