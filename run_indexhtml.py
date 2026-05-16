with open('write_indexhtml.py', 'w', encoding='utf-8') as s:
    s.write("""
code = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>C Rythan | CS Student & ML Enthusiast</title>
    <meta name="description" content="Portfolio of C Rythan, B.Tech CSE student at Amrita School of Computing. Passionate about LLMs, NLP, and building impactful software." />
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>'''
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(code)
print('index.html updated!')
""")
