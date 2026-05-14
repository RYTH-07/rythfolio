export default function LearningJourney() {
  const semesters = [
    {
      label: "Semester 2",
      year: "2025-26",
      current: true,
      title: "OOP, Math & Physics",
      description: "OOP in Java (classes, objects, inheritance, interfaces, exception handling), Discrete Mathematics (recurrence relations, graph theory, relations), Linear Algebra (vector spaces, eigenvalues, transformations), Modern Physics (quantum mechanics, wave functions), User Interface Design (HTML, CSS, JavaScript).",
    },
    {
      label: "Semester 1",
      year: "2024-25",
      current: false,
      title: "Programming Foundations",
      description: "Python programming fundamentals, problem solving, basic data structures, and introductory computer science concepts. SGPA: 8.22.",
    },
  ];

  return (
    <section id="learning-journey" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Education</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Learning Journey</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            B.Tech Computer Science and Engineering at Amrita School of Computing, Chennai. Semester-by-semester record of academic progress.
          </p>
        </div>
        <div className="relative max-w-2xl">
          <div className="absolute left-[15px] top-2 bottom-2 w-px bg-gray-200 dark:bg-gray-800" />
          <div className="space-y-6">
            {semesters.map((sem, i) => (
              <div key={i} className="relative flex gap-6 pl-10">
                <div className={bsolute left-0 top-1.5 w-8 h-8 rounded-full border flex items-center justify-center flex-shrink-0 z-10 }>
                  <div className={w-2 h-2 rounded-full } />
                </div>
                <div className="flex-1 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 p-5">
                  <div className="flex flex-wrap items-center gap-2 mb-2">
                    <span className="text-sm font-medium text-gray-900 dark:text-white">{sem.label}</span>
                    <span className="text-xs text-gray-400 dark:text-gray-500">{sem.year}</span>
                    {sem.current && <span className="text-xs font-medium px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 dark:bg-blue-950 dark:text-blue-300">Current</span>}
                  </div>
                  <h3 className="font-medium text-gray-900 dark:text-white mb-1">{sem.title}</h3>
                  <p className="text-sm text-gray-500 dark:text-gray-400 leading-relaxed">{sem.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}