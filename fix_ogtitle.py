
code = open('index.html', 'r', encoding='utf-8').read()
code = code.replace(
    'C Rythan | CS Student &amp; ML Enthusiast',
    'C Rythan | B.Tech CSE Student, ML Enthusiast and NLP Explorer'
)
code = code.replace(
    'C Rythan | CS Student & ML Enthusiast',
    'C Rythan | B.Tech CSE Student, ML Enthusiast and NLP Explorer'
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(code)
print('Title fixed!')
