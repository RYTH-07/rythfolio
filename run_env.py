with open('write_env.py', 'w', encoding='utf-8') as s:
    s.write("""
code = '''VITE_EMAILJS_SERVICE_ID=service_2ytlsc3
VITE_EMAILJS_TEMPLATE_ID=template_3gzdxql
VITE_EMAILJS_PUBLIC_KEY=48z8_D9-EGFE10XGv'''
with open('.env', 'w', encoding='utf-8') as f:
    f.write(code)
print('env done!')
""")
