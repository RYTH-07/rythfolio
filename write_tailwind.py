content = '''@import "tailwindcss" source(none);
@source "../**/*.{js,ts,jsx,tsx}";
@import "tw-animate-css";

@variant dark (&:where(.dark, .dark *));'''
with open('src/styles/tailwind.css', 'w', encoding='utf-8') as f:
    f.write(content)
print('Tailwind fixed!')
