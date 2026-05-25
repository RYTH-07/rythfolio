code = open('src/app/App.tsx', 'r', encoding='utf-8').read()

if 'PageLoader' not in code:
    code = code.replace(
        'import ProgressBar from "./components/ProgressBar";',
        'import ProgressBar from "./components/ProgressBar";\nimport PageLoader from "./components/PageLoader";'
    )
    code = code.replace(
        '<ProgressBar />',
        '<PageLoader />\n      <ProgressBar />'
    )

with open('src/app/App.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("App.tsx updated with PageLoader!")
