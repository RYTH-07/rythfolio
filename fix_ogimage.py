
code = open('index.html', 'r', encoding='utf-8').read()
code = code.replace('og-image.jpg', 'og-image.png')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(code)
print('OG image updated!')
