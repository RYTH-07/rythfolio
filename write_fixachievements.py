
code = open('src/app/components/Achievements.tsx', 'r', encoding='utf-8').read()
code = code.replace('\u2014', '--')
code = code.replace('\u2013', '-')
code = code.replace('\u2019', "'")
code = code.replace('\u201c', '"')
code = code.replace('\u201d', '"')
# Fix the diamond question marks from encoding issues
import re
code = re.sub(r'[\x80-\xff]', '', code)
with open('src/app/components/Achievements.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('Achievements fixed!')
