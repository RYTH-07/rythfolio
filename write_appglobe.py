
code = open('src/app/App.tsx', 'r', encoding='utf-8').read()
code = code.replace('import TechStack from "./components/TechStack";', 'import SkillsGlobe from "./components/SkillsGlobe";')
code = code.replace('<TechStack />', '<SkillsGlobe />')
with open('src/app/App.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('App updated!')
