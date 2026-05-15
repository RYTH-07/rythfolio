
code = open('src/app/components/Footer.tsx', 'r', encoding='utf-8').read()
code = code.replace('{ label: "Blog", href: "#blog" },', '')
with open('src/app/components/Footer.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('Footer done!')
