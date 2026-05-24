with open('fix_env2.py', 'w', encoding='utf-8') as s:
    s.write("""
code = open('.env', 'r', encoding='utf-8').read()
if 'SUPABASE' not in code:
    code += '\\nVITE_SUPABASE_URL=https://yzyzoultqmuxhbnujqkt.supabase.co'
    code += '\\nVITE_SUPABASE_KEY=sb_publishable_-Ts93NuJv4iUTGqP_xkkLg_pXV7CaHt'
    with open('.env', 'w', encoding='utf-8') as f:
        f.write(code)
    print('env updated!')
else:
    print('Already in env')
""")
