with open('src/app/components/CodeMatrix.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Fix the fetch to use the correct username and better endpoint
old_fetch = '''    async function fetchLeetCode() {
      try {
        const res = await fetch("https://alfa-leetcode-api.onrender.com/Vvhq82c4cV/solved?nocache=" + Date.now());
        const data = await res.json();
        if (data.solvedProblem && data.solvedProblem > 0) {
          setLeetCount(data.solvedProblem);
        } else {
          setLeetCount(12); // fallback
        }
      } catch (err) {
        console.error("Failed to fetch LeetCode stats:", err);
        setLeetCount(12); // fallback
      }
    }'''

new_fetch = '''    async function fetchLeetCode() {
      try {
        const res = await fetch("https://alfa-leetcode-api.onrender.com/RYTH-07/solved?nocache=" + Date.now());
        const data = await res.json();
        if (data.solvedProblem && data.solvedProblem > 0) {
          setLeetCount(data.solvedProblem);
        } else {
          setLeetCount(13); // fallback
        }
      } catch (err) {
        console.error("Failed to fetch LeetCode stats:", err);
        setLeetCount(13); // fallback
      }
    }'''

code = code.replace(old_fetch, new_fetch)

# Also fix the leetcard image to use new username
code = code.replace('Vvhq82c4cV', 'RYTH-07')

with open('src/app/components/CodeMatrix.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("CodeMatrix username and sync fixed!")
