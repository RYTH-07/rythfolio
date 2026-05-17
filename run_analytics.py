with open('write_analytics.py', 'w', encoding='utf-8') as s:
    s.write("""
code = open('src/main.tsx', 'r', encoding='utf-8').read()
code = "import { inject } from '@vercel/analytics';\\n" + code
code = code.replace(
    "createRoot(document.getElementById('root')!).render(",
    "inject();\\n\\ncreatRoot(document.getElementById('root')!).render("
)
with open('src/main.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('Analytics done!')
""")
