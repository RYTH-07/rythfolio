import json

with open('package.json', 'r', encoding='utf-8') as f:
    pkg = json.load(f)

# Add react and react-dom to dependencies
pkg['dependencies']['react'] = '^18.3.1'
pkg['dependencies']['react-dom'] = '^18.3.1'

# Remove from peerDependencies
if 'peerDependencies' in pkg:
    del pkg['peerDependencies']
if 'peerDependenciesMeta' in pkg:
    del pkg['peerDependenciesMeta']

with open('package.json', 'w', encoding='utf-8') as f:
    json.dump(pkg, f, indent=2)

print("package.json fixed!")
