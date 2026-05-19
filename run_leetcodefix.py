with open('write_leetcodefix.py', 'w', encoding='utf-8') as s:
    s.write("""
import chardet
with open('src/app/components/CodeMatrix.tsx', 'rb') as f:
    raw = f.read()
encoding = chardet.detect(raw)['encoding']
code = raw.decode(encoding)
code = code.replace(
    'fetch("https://alfa-leetcode-api.onrender.com/Vvhq82c4cV/solved")',
    'fetch("https://alfa-leetcode-api.onrender.com/Vvhq82c4cV/solved?nocache=" + Date.now())'
)
code = code.replace(
    'fetch("https://alfa-leetcode-api.onrender.com/Vvhq82c4cV")',
    'fetch("https://alfa-leetcode-api.onrender.com/Vvhq82c4cV?nocache=" + Date.now())'
)
with open('src/app/components/CodeMatrix.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('LeetCode cache fix done!')
""")
