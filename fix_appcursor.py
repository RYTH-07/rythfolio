
code = open('src/app/App.tsx', 'r', encoding='utf-8').read()
if 'CursorSpotlight' not in code:
    code = code.replace(
        'import ScrollToTop from "./components/ScrollToTop";',
        'import ScrollToTop from "./components/ScrollToTop";\nimport CursorSpotlight from "./components/CursorSpotlight";'
    )
    code = code.replace(
        '<ProgressBar />',
        '<ProgressBar />\n      <CursorSpotlight />'
    )
    with open('src/app/App.tsx', 'w', encoding='utf-8') as f:
        f.write(code)
    print('CursorSpotlight added!')
else:
    print('Already added')
