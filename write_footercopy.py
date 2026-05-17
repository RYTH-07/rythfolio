
import chardet
with open('src/app/components/Footer.tsx', 'rb') as f:
    raw = f.read()
encoding = chardet.detect(raw)['encoding']
code = raw.decode(encoding)
code = code.replace(
    '{new Date().getFullYear()} C Rythan. Built with React and Tailwind CSS.',
    '\u00A9 {new Date().getFullYear()} C Rythan. All rights reserved. Built with React and Tailwind CSS.'
)
with open('src/app/components/Footer.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('Footer done!')
