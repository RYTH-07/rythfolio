with open('fix_appguestbook.py', 'w', encoding='utf-8') as s:
    s.write("""
code = open('src/app/App.tsx', 'r', encoding='utf-8').read()
code = code.replace(
    'import Contact from "./components/Contact";',
    'import Contact from "./components/Contact";\\nimport Guestbook from "./components/Guestbook";'
)
code = code.replace(
    '<Contact />',
    '<Contact />\\n        <Guestbook />'
)
with open('src/app/App.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('App updated with Guestbook!')
""")
