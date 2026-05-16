with open('write_fixstats.py', 'w', encoding='utf-8') as s:
    s.write("""
code = open('src/app/components/Hero.tsx', 'r', encoding='utf-8').read()
code = code.replace('<p className="text-2xl font-semibold text-gray-900 dark:text-white">1</p><p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Projects</p>', '<p className="text-2xl font-semibold text-gray-900 dark:text-white">2</p><p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Projects</p>')
with open('src/app/components/Hero.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('Stats updated!')
""")
