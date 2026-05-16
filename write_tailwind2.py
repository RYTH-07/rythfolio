
code = '''@import "tailwindcss" source(none);
@source "../**/*.{js,ts,jsx,tsx}";

@variant dark (&:where(.dark, .dark *));

@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
'''
with open('src/styles/tailwind.css', 'w', encoding='utf-8') as f:
    f.write(code)
print('Tailwind fixed!')
