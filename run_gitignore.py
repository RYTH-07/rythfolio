with open('write_gitignore.py', 'w', encoding='utf-8') as s:
    s.write("""
try:
    existing = open('.gitignore', 'r', encoding='utf-8').read()
except:
    existing = ''
if '.env' not in existing:
    with open('.gitignore', 'a', encoding='utf-8') as f:
        f.write('\\n.env\\n')
    print('.env added to .gitignore!')
else:
    print('Already in .gitignore')
""")
