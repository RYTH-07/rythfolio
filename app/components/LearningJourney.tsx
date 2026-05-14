const milestones = [
  {
    period: "Semester 5 – 6",
    year: "2024",
    title: "Advanced Algorithms & Systems",
    description: "Placeholder — add key courses, projects completed, and skills acquired during this period.",
    current: true,
  },
  {
    period: "Semester 3 – 4",
    year: "2023",
    title: "Data Structures & OS Fundamentals",
    description: "Placeholder — add key courses, projects completed, and skills acquired during this period.",
    current: false,
  },
  {
    period: "Semester 1 – 2",
    year: "2022",
    title: "Programming Foundations",
    description: "Placeholder — add introductory courses, first projects, and foundational skills acquired.",
    current: false,
  },
];

export default function LearningJourney() {
  return (
    <section id="learning" className="py-20 bg-gray-50 dark:bg-gray-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">
            Education
          </p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Learning Journey</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            A semester-by-semester record of academic progress and self-directed learning.
          </p>
        </div>

        <div className="max-w-2xl">
          {milestones.map((item, i) => (
            <div key={i} className="relative flex gap-6 pb-10 last:pb-0">
              <div className="flex flex-col items-center">
                <div
                  className={`w-4 h-4 rounded-full flex-shrink-0 border-2 transition-colors ${
                    item.current
                      ? "bg-blue-600 border-blue-600 dark:bg-blue-500 dark:border-blue-500"
                      : "bg-white dark:bg-gray-900 border-gray-300 dark:border-gray-600"
                  }`}
                />
                {i < milestones.length - 1 && (
                  <div className="flex-1 w-px bg-gray-200 dark:bg-gray-800 mt-1" />
                )}
              </div>

              <div className="flex-1 pt-0.5 pb-2">
                <div className="flex flex-wrap items-center gap-2 mb-2">
                  <span className="text-sm font-medium text-gray-900 dark:text-white">{item.period}</span>
                  <span className="text-xs text-gray-400 dark:text-gray-500">{item.year}</span>
                  {item.current && (
                    <span className="text-xs px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 dark:bg-blue-950 dark:text-blue-300">
                      Current
                    </span>
                  )}
                </div>
                <h3 className="font-semibold text-gray-900 dark:text-white mb-1.5">{item.title}</h3>
                <p className="text-sm text-gray-500 dark:text-gray-400 leading-relaxed">{item.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
