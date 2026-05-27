import { useEffect, useState } from "react";

export default function CodeMatrix() {
  const [leetCount, setLeetCount] = useState(0);

  useEffect(() => {
    async function fetchLeetCode() {
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
    }
    fetchLeetCode();
  }, []);

  const platforms = [
    { name: "GeeksforGeeks", handle: "@C RYTHAN", href: "https://www.geeksforgeeks.org/profile/rythcomra12?tab=activity", dot: "bg-green-500" },
    { name: "HackerRank", handle: "@rythcomputes", href: "https://www.hackerrank.com/profile/rythcomputes", dot: "bg-emerald-500" },
    { name: "Codolio", handle: "@C RYTHAN", href: "https://codolio.com/profile/C%20RYTHAN", dot: "bg-blue-500" },
  ];

  const totalStats = [
    { platform: "LeetCode", solved: leetCount, color: "text-orange-400" },
    { platform: "GeeksforGeeks", solved: 2, color: "text-green-500" },
    { platform: "HackerRank", solved: 4, color: "text-emerald-500" },
  ];

  const total = totalStats.reduce((sum, p) => sum + p.solved, 0);

  return (
    <section id="code-matrix" className="py-20 bg-gray-50 dark:bg-gray-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Coding Activity</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Code Matrix</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">Competitive programming statistics across major platforms.</p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
          <a
            href="https://leetcode.com/u/RYTH-07"
            target="_blank"
            rel="noopener noreferrer"
            className="rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 p-6 hover:shadow-md hover:border-blue-300 dark:hover:border-blue-700 transition-all cursor-pointer block no-underline"
          >
            <div className="flex items-start justify-between mb-4">
              <div>
                <h3 className="font-semibold text-gray-900 dark:text-white">LeetCode</h3>
                <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">RYTH-07</p>
              </div>
              <span className="w-2.5 h-2.5 rounded-full mt-1.5 bg-orange-400" />
            </div>
            <img
              src="https://leetcard.jacoblin.cool/RYTH-07?theme=dark&font=Poppins&ext=contest"
              alt="LeetCode Stats"
              className="w-full rounded-lg"
            />
          </a>
          <div className="rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 p-6">
            <div className="flex items-start justify-between mb-6">
              <div>
                <h3 className="font-semibold text-gray-900 dark:text-white">Total Solved</h3>
                <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Across all platforms</p>
              </div>
              <span className="text-2xl font-bold text-blue-600 dark:text-blue-400">{total}</span>
            </div>
            <div className="space-y-3">
              {totalStats.map((p) => (
                <div key={p.platform} className="flex items-center justify-between">
                  <span className={"text-sm font-medium " + p.color}>{p.platform}</span>
                  <span className="text-sm font-semibold text-gray-900 dark:text-white">{p.solved} solved</span>
                </div>
              ))}
            </div>
          </div>
          {platforms.map((platform) => (
            <a
              key={platform.name}
              href={platform.href}
              target="_blank"
              rel="noopener noreferrer"
              className="rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 p-6 hover:shadow-md hover:border-blue-300 dark:hover:border-blue-700 transition-all cursor-pointer block no-underline"
            >
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="font-semibold text-gray-900 dark:text-white">{platform.name}</h3>
                  <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">{platform.handle}</p>
                </div>
                <div className="flex items-center gap-3">
                  <span className="text-xs text-gray-400 dark:text-gray-500">View Profile →</span>
                  <span className={"w-2.5 h-2.5 rounded-full " + platform.dot} />
                </div>
              </div>
            </a>
          ))}
        </div>
        <p className="mt-6 text-xs text-gray-400 dark:text-gray-500 text-center">Click any card to view full profile</p>
      </div>
    </section>
  );
}
