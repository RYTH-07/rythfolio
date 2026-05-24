code = open('src/app/App.tsx', 'r', encoding='utf-8').read()
code = code.replace('import SkillsGlobe from "./components/SkillsGlobe";', 'import TechStack from "./components/TechStack";')
code = code.replace('<SkillsGlobe />', '<TechStack />')
with open('src/app/App.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('App fixed - SkillsGlobe removed!')
