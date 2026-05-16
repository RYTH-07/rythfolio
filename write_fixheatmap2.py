
import chardet
with open('src/app/components/GitHubHeatmap.tsx', 'rb') as f:
    raw = f.read()
encoding = chardet.detect(raw)['encoding']
code = raw.decode(encoding)
code = code.replace(
    'fetch(https://github-contributions-api.jogruber.de/v4/?y=last)',
    'fetch(https://github-contributions-api.jogruber.de/v4/?y=2026)'
)
with open('src/app/components/GitHubHeatmap.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('Heatmap year fixed!')
