const items = [
  {
    year: "2026",
    category: "Hackathon",
    title: "Flash 2.0 — 4th Place",
    description: "Built a fitness app prototype in under 4 hours at Amrita School of Computing, Chennai. Competed against teams across the college.",
  },
];

const badgeStyles: Record<string, string> = {
  Hackathon: "bg-blue-50 text-blue-700 dark:bg-blue-950 dark:text-blue-300",
  Certification: "bg-green-50 text-green-700 dark:bg-green-950 dark:text-green-300",
  Award: "bg-amber-50 text-amber-700 dark:bg-amber-950 dark:text-amber-300",
};

export default function Achievements() {
  return (
    <section id="achievements" className="py-20 bg-gray-50 dark:bg-gray-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">
            Milestones
          </p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Achievements</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            Hackathons, certifications, and awards — a timeline of key accomplishments.
          </p>
        </div>
        <div className="relative max-w-2xl">
          <div className="absolute left-[15px] top-2 bottom-2 w-px bg-gray-200 dark:bg-gray-800" />
          <div className="space-y-6">
            {items.map((item, i) => (
              <div key={i} className="relative flex gap-6 pl-10">
                <div className="absolute left-0 top-1.5 w-8 h-8 rounded-full bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-700 flex items-center justify-center flex-shrink-0 z-10">
                  <div className="w-2 h-2 rounded-full bg-gray-300 dark:bg-gray-600" />
                </div>
                <div className="flex-1 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 p-5">
                  <div className="flex flex-wrap items-center gap-2 mb-2">
                    <span className={`text-xs font-medium px-2.5 py-0.5 rounded-full ${badgeStyles[item.category] ?? "bg-gray-100 text-gray-600"}`}>
                      {item.category}
                    </span>
                    <span className="text-xs text-gray-400 dark:text-gray-500">{item.year}</span>
                  </div>
                  <h3 className="font-medium text-gray-900 dark:text-white mb-1">{item.title}</h3>
                  <p className="text-sm text-gray-500 dark:text-gray-400 leading-relaxed">{item.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
