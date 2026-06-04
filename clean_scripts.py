import subprocess
import os
import glob

# Find all write_*.py and fix_*.py and run_*.py files
patterns = ['write_*.py', 'fix_*.py', 'run_*.py']
files = []
for pattern in patterns:
    files.extend(glob.glob(pattern))

if not files:
    print("No script files found to clean!")
else:
    print(f"Found {len(files)} files to remove from git tracking:")
    for f in files:
        print(f"  - {f}")
    
    # Add to gitignore
    with open('.gitignore', 'r', encoding='utf-8') as f:
        gitignore = f.read()
    
    additions = []
    if 'fix_*.py' not in gitignore:
        additions.append('fix_*.py')
    if 'run_*.py' not in gitignore:
        additions.append('run_*.py')
    
    if additions:
        with open('.gitignore', 'a', encoding='utf-8') as f:
            f.write('\n' + '\n'.join(additions) + '\n')
        print(f"Added to .gitignore: {additions}")
    
    # Remove from git cache
    for file in files:
        try:
            result = subprocess.run(['git', 'rm', '--cached', file], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Removed from git: {file}")
        except Exception as e:
            print(f"Could not remove {file}: {e}")

print("\nDone! Now run: git add . && git commit -m 'chore: clean up scripts'")
