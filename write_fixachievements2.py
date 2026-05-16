
import chardet
with open('src/app/components/Achievements.tsx', 'rb') as f:
    raw = f.read()
encoding = chardet.detect(raw)['encoding']
print(f'Detected: {encoding}')
code = raw.decode(encoding)
# Fix weird characters
code = code.replace('\u2014', '--')
code = code.replace('\u2013', '-')
code = code.replace('\u2019', "'")
code = code.replace('\u201c', '"')
code = code.replace('\u201d', '"')
code = code.replace('\x97', '--')
code = code.replace('\x96', '-')
code = code.replace('\x93', '"')
code = code.replace('\x94', '"')
code = code.replace('\x92', "'")
with open('src/app/components/Achievements.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('Achievements fixed!')
