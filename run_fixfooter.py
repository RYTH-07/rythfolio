with open('write_fixfooter.py', 'w', encoding='utf-8') as s:
    s.write("""
import chardet
with open('src/app/components/Footer.tsx', 'rb') as f:
    raw = f.read()
encoding = chardet.detect(raw)['encoding']
code = raw.decode(encoding)
import re
code = re.sub(r'[^\\x00-\\x7F]+', '', code)
code = code.replace('{new Date().getFullYear()} C Rythan.', '{new Date().getFullYear()} C Rythan.')
with open('src/app/components/Footer.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('Footer fixed!')
""")
