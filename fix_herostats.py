with open('src/app/components/Hero.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix projects count
code = code.replace(
    '{ value: 2, label: "Projects", suffix: "" }',
    '{ value: 3, label: "Projects", suffix: "" }'
)

# Fix problems solved
code = code.replace(
    '{ value: 12, label: "Problems Solved", suffix: "+" }',
    '{ value: 30, label: "Problems Solved", suffix: "+" }'
)

with open('src/app/components/Hero.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("Hero stats updated!")
