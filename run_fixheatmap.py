with open('write_fixheatmap.py', 'w', encoding='utf-8') as s:
    s.write("""
import chardet
with open('src/app/components/GitHubHeatmap.tsx', 'rb') as f:
    raw = f.read()
encoding = chardet.detect(raw)['encoding']
code = raw.decode(encoding)
code = code.replace('Commit activity for the past year \\u2014 live from GitHub.', 'Commit activity for the past year - live from GitHub.')
code = code.replace('Commit activity for the past year \\x97 live from GitHub.', 'Commit activity for the past year - live from GitHub.')
# Remove any non-ascii diamond characters
import re
code = re.sub(r'[^\\x00-\\x7F]+', '-', code)
with open('src/app/components/GitHubHeatmap.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('GitHubHeatmap fixed!')
""")
