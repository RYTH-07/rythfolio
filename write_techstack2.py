
code = '''import { motion } from "motion/react";

const skills = [
  { name: "Python", level: 70, color: "bg-blue-500" },
  { name: "Java", level: 60, color: "bg-orange-500" },
  { name: "TypeScript", level: 50, color: "bg-blue-400" },
  { name: "HTML/CSS", level: 80, color: "bg-pink-500" },
  { name: "JavaScript", level: 55, color: "bg-yellow-500" },
  { name: "React", level: 45, color: "bg-cyan-500" },
  { name: "Git", level: 60, color: "bg-red-500" },
  { name: "DSA", level: 40, color: "bg-purple-500" },
];

export default function TechStack() {
  return (
    <section id="techstack" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Skills</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Tech Stack</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">Tools and technologies I work with - proficiency levels are self-assessed and actively growing.</p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          {skills.map((skill, i) => (
            <motion.div key={skill.name} initial={{ opacity: 0, x: -20 }} whileInView={{ opacity: 1, x: 0 }} viewport={{ once: true }} transition={{ delay: i * 0.08, duration: 0.4 }}>
              <div className="flex justify-between mb-1.5">
                <span className="text-sm font-medium text-gray-900 dark:text-white">{skill.name}</span>
                <span className="text-xs text-gray-400 dark:text-gray-500">{skill.level}%</span>
              </div>
              <div className="h-2 w-full rounded-full bg-gray-100 dark:bg-gray-800 overflow-hidden">
                <motion.div className={"h-full rounded-full " + skill.color} initial={{ width: 0 }} whileInView={{ width: skill.level + "%" }} viewport={{ once: true }} transition={{ delay: i * 0.08 + 0.2, duration: 0.7, ease: "easeOut" }} />
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}'''
with open('src/app/components/TechStack.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('TechStack done!')
