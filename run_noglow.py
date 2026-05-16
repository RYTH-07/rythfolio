with open('write_noglow.py', 'w', encoding='utf-8') as s:
    s.write("""
code = open('src/app/components/Hero.tsx', 'r', encoding='utf-8').read()
code = code.replace('            <div className="absolute -inset-4 bg-gradient-to-br from-blue-400 to-purple-500 rounded-2xl opacity-20 blur-xl animate-pulse" />', '')
with open('src/app/components/Hero.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('Glow removed!')
""")
