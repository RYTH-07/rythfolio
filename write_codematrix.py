import sys
content = open('src/app/components/CodeMatrix.tsx', 'w', encoding='utf-8')
content.write("""import { useEffect, useState } from "react";

type Metric = { label: string; value: string };
type Platform = { name: string; handle: string; href: string; dot: string; metrics: Metric[] };

export default function CodeMatrix() {
  const [platforms, setPlatforms] = useState<Platform[]>([
    { name: "LeetCode", handle: "@Vvhq82c4cV", href: "https://leetcode.com/u/Vvhq82c4cV/", dot: "bg-orange-400", metrics: [{ label: "Problems Solved", value: "..." }, { label: "Easy Solved", value: "..." }, { label: "Global Rank", value: "..." }, { label: "Max Streak", value: "2" }] },
    { name: "GeeksforGeeks", handle: "@C RYTHAN", href: "https://www.geeksforgeeks.org/user/crythan/", dot: "bg-green-500", metrics: [{ label: "Problems Solved", value: "2" }, { label: "Coding Score", value: "4" }, { label: "Easy Solved", value: "2" }, { label: "POTD Streak", value: "0" }] },
    { name: "HackerRank", handle: "@rythcomputes", href: "https://www.hackerrank.com/profile/rythcomputes", dot: "bg-emerald-500", metrics: [{ label: "Problems Solved", value: "4" }, { label: "Badges", value: "1" }, { label: "Python Badge", value: "Star" }, { label: "Certifications", value: "0" }] },
    { name: "Codolio", handle: "@C RYTHAN", href: "https://codolio.com/profile/C%20RYTHAN", dot: "bg-blue-500", metrics: [{ label: "Total Solved", value: "12" }, { label: "Submissions", value: "7" }, { label: "Active Days", value: "5" }, { label: "Awards", value: "1" }] },
  ]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("https://alfa-leetcode-api.onrender.com/Vvhq82c4cV/solved")
      .then(res => res.json())
      .then(data => {
        fetch("https://alfa-leetcode-api.onrender.com/Vvhq82c4cV")
          .then(res2 => res2.json())
          .then(profile => {
            setPlatforms(prev => prev.map(p => {
              if (p.name !== "LeetCode") return p;
              return {
                ...p,
                metrics: [
                  { label: "Problems Solved", value: String(data.solvedProblem ?? "N/A") },
                  { label: "Easy Solved", value: String(data.easySolved ?? "N/A") },
                  { label: "Global Rank", value: profile.ranking ? "#" + Number(profile.ranking).toLocaleString() : "N/A" },
                  { label: "Max Streak", value: "2" },
                ]
              };
            }));
            setLoading(false);
          });
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <section id="code-matrix" className="py-20 bg-gray-50 dark:bg-gray-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Coding Activity</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Code Matrix</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">Competitive programming stats across major platforms.</p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
          {platforms.map((platform) => (
            <a key={platform.name} href={platform.href} target="_blank" rel="noopener noreferrer" className="rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 p-6 hover:shadow-md hover:border-blue-300 dark:hover:border-blue-700 transition-all block">
              <div className="flex items-start justify-between mb-6">
                <div>
                  <h3 className="font-semibold text-gray-900 dark:text-white">{platform.name}</h3>
                  <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">{platform.handle}</p>
                </div>
                <div className="flex items-center gap-2">
                  {platform.name === "LeetCode" && (
                    <span className={	ext-xs px-2 py-0.5 rounded-full }>
                      {loading ? "loading..." : "live"}
                    </span>
                  )}
                  <span className={w-2.5 h-2.5 rounded-full } />
                </div>
              </div>
              <div className="grid grid-cols-2 gap-5">
                {platform.metrics.map((m) => (
                  <div key={m.label}>
                    <p className="text-xs text-gray-400 dark:text-gray-500 mb-1">{m.label}</p>
                    <p className={	ext-sm font-semibold text-gray-900 dark:text-white }>
                      {loading && platform.name === "LeetCode" ? "" : m.value}
                    </p>
                  </div>
                ))}
              </div>
            </a>
          ))}
        </div>
        <p className="mt-6 text-xs text-gray-400 dark:text-gray-500 text-center">Click any card to view full profile</p>
      </div>
    </section>
  );
}""")
content.close()
print("Done!")
