with open('src/app/components/Hero.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_svg = '''                <svg className="w-8 h-8 sm:w-10 sm:h-10 text-blue-500 flex-shrink-0" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>'''

new_svg = '''                <svg className="w-8 h-8 sm:w-10 sm:h-10 flex-shrink-0" viewBox="0 0 24 24" fill="none">
                  <path d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-.497 3.842 3.745 3.745 0 01-3.843.497A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.745 3.745 0 01-3.842-.497 3.745 3.745 0 01-.497-3.842A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 01.497-3.842 3.745 3.745 0 013.842-.497A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.842.497 3.745 3.745 0 01.497 3.842A3.745 3.745 0 0121 12z" stroke="#3b82f6" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
                  <path d="M9 12.75L11.25 15 15 9.75" stroke="#3b82f6" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>'''

code = code.replace(old_svg, new_svg)

with open('src/app/components/Hero.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("Verified tick fixed!")
