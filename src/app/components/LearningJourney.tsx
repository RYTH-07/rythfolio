import { motion } from "motion/react";

export default function LearningJourney() {
  const semesters = [
    {
      label: "Semester 2",
      year: "2025-26",
      current: false,
      title: "OOP, Math & Physics",
      description: "OOP in Java (classes, objects, inheritance, interfaces, exception handling), Discrete Mathematics (recurrence relations, graph theory, relations), Linear Algebra (vector spaces, eigenvalues, transformations), Modern Physics (quantum mechanics, wave functions), User Interface Design (HTML, CSS, JavaScript).",
      sgpa: "8.67",
      sgpaColor: "from-purple-400 to-blue-500",
      glowColor: "rgba(139,92,246,0.5)",
    },
    {
      label: "Semester 1",
      year: "2024-25",
      current: false,
      title: "Programming Foundations",
      description: "Python programming fundamentals, problem solving, basic data structures, and introductory computer science concepts.",
      sgpa: "8.22",
      sgpaColor: "from-blue-400 to-cyan-500",
      glowColor: "rgba(59,130,246,0.5)",
    },
  ];

  return (
    <section id="learning-journey" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Education</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Learning Journey</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            B.Tech Computer Science and Engineering at Amrita School of Computing, Chennai.
            <span className="ml-2 font-semibold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
              CGPA: 8.48 ✦
            </span>
          </p>
        </div>
        <div className="relative max-w-2xl">
          <div className="absolute left-[15px] top-2 bottom-2 w-px bg-gray-200 dark:bg-gray-800" />
          <div className="space-y-6">
            {semesters.map((sem, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, x: -20 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.15, duration: 0.5 }}
                className="relative flex gap-6 pl-10"
              >
                <div className={`absolute left-0 top-1.5 w-8 h-8 rounded-full border flex items-center justify-center flex-shrink-0 z-10 bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-700`}>
                  <div className="w-2 h-2 rounded-full bg-gray-300 dark:bg-gray-600" />
                </div>
                <div className="flex-1 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 p-5 hover:border-blue-200 dark:hover:border-blue-800 transition-colors">
                  <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
                    <div className="flex items-center gap-2">
                      <span className="text-sm font-medium text-gray-900 dark:text-white">{sem.label}</span>
                      <span className="text-xs text-gray-400 dark:text-gray-500">{sem.year}</span>
                    </div>
                    <motion.div
                      initial={{ opacity: 0, scale: 0.5 }}
                      whileInView={{ opacity: 1, scale: 1 }}
                      viewport={{ once: true }}
                      transition={{ delay: i * 0.15 + 0.3, duration: 0.4, type: "spring" }}
                      className="relative"
                    >
                      <span
                        className={`text-lg font-bold bg-gradient-to-r ${sem.sgpaColor} bg-clip-text text-transparent`}
                        style={{ filter: `drop-shadow(0 0 6px ${sem.glowColor})` }}
                      >
                        {sem.sgpa}
                      </span>
                      <span className="ml-1 text-xs text-gray-400">SGPA</span>
                      <motion.span
                        animate={{ opacity: [0, 1, 0] }}
                        transition={{ duration: 2, repeat: Infinity, delay: i * 0.5 }}
                        className="absolute -top-1 -right-2 text-yellow-400 text-xs"
                      >
                        ✦
      </motion.span>
                    </motion.div>
                  </div>
                  <h3 className="font-medium text-gray-900 dark:text-white mb-1">{sem.title}</h3>
                  <p className="text-sm text-gray-500 dark:text-gray-400 leading-relaxed">{sem.description}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
