
code = open('src/app/components/Navigation.tsx', 'r', encoding='utf-8').read()
code = code.replace(
    '{ label: "Contact", href: "#contact" },',
    '{ label: "Contact", href: "#contact" },\n    { label: "Guestbook", href: "#guestbook" },'
)
with open('src/app/components/Navigation.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('Navigation updated!')
