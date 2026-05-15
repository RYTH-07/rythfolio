import chardet

# Read file as bytes
with open('src/app/components/Footer.tsx', 'rb') as f:
    raw = f.read()

# Detect encoding
encoding = chardet.detect(raw)['encoding']
print(f'Detected encoding: {encoding}')

# Decode and modify
code = raw.decode(encoding)
code = code.replace('{ label: "Blog", href: "#blog" },', '')

# Write back using same encoding
with open('src/app/components/Footer.tsx', 'w', encoding=encoding) as f:
    f.write(code)

print('Footer done!')
