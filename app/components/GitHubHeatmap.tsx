const WEEKS = 52;
const DAYS = 7;
const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

export default function GitHubHeatmap() {
  return (
    <section id="github-heatmap" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">
            Contributions
          </p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">GitHub Reflector</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            Commit activity for the past year — connect your GitHub account to populate real data.
          </p>
        </div>

        <div className="rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 p-6">
          <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 mb-5">
            <p className="text-sm text-gray-500 dark:text-gray-400">0 contributions in the last year</p>
            <div className="flex items-center gap-1.5 text-xs text-gray-400 dark:text-gray-500">
              <span>Less</span>
              {["bg-gray-100 dark:bg-gray-800", "bg-blue-100 dark:bg-blue-900/40", "bg-blue-200 dark:bg-blue-800/60", "bg-blue-400 dark:bg-blue-600", "bg-blue-600 dark:bg-blue-400"].map((cls, i) => (
                <span key={i} className={`w-3 h-3 rounded-sm ${cls}`} />
              ))}
              <span>More</span>
            </div>
          </div>

          <div className="overflow-x-auto">
            <div className="flex gap-1 min-w-max pb-1">
              {Array.from({ length: WEEKS }, (_, w) => (
                <div key={w} className="flex flex-col gap-1">
                  {Array.from({ length: DAYS }, (_, d) => (
                    <div
                      key={d}
                      className="w-3 h-3 rounded-sm bg-gray-100 dark:bg-gray-800"
                    />
                  ))}
                </div>
              ))}
            </div>
          </div>

          <div className="mt-3 flex justify-between text-xs text-gray-400 dark:text-gray-500">
            {MONTHS.map((m) => (
              <span key={m}>{m}</span>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
