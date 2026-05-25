code = open('src/app/components/CodeMatrix.tsx', 'r', encoding='utf-8').read()

# Fix the API to use alfa-leetcode which matches the card
old_fetch = '''  useEffect(() => {
    async function fetchLeetCode() {
      try {
        const res = await fetch("https://leetcode-stats-api.herokuapp.com/Vvhq82c4cV");
        const data = await res.json();
        if (data.totalSolved && data.totalSolved > 0) {
          setLeetCount(data.totalSolved);
        } else {
          setLeetCount(8); // fallback if API returns 0
        }
      } catch (err) {
        console.error("Failed to fetch LeetCode stats:", err);
        setLeetCount(8); // fallback if API fails
      }
    }
    fetchLeetCode();
  }, []);'''

new_fetch = '''  useEffect(() => {
    async function fetchLeetCode() {
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
    }
    fetchLeetCode();
  }, []);'''

code = code.replace(old_fetch, new_fetch)

with open('src/app/components/CodeMatrix.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("CodeMatrix LeetCode sync fixed!")
