code = open('src/app/App.tsx', 'r', encoding='utf-8').read()

if 'CustomCursor' not in code:
    code = code.replace(
        'import CursorSpotlight from "./components/CursorSpotlight";',
        'import CursorSpotlight from "./components/CursorSpotlight";\nimport CustomCursor from "./components/CustomCursor";'
    )
    code = code.replace(
        '<CursorSpotlight />',
        '<CursorSpotlight />\n      <CustomCursor />'
    )

with open('src/app/App.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("CustomCursor added to App!")
