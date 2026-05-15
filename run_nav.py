with open('write_nav.py', 'w', encoding='utf-8') as s:
    s.write("""
code = open('src/app/components/Navigation.tsx', 'r', encoding='utf-8').read()
code = code.replace('{ label: "Blog", href: "#blog" },', '')
with open('src/app/components/Navigation.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('Navigation done!')
""")
