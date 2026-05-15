content = '''import { motion } from "motion/react";
import { BookOpen, Code, Brain, Flame } from "lucide-react";

const items = [
  { icon: Brain, title: "LLMs & NLP", description: "Exploring transformer architecture, attention mechanisms, and how large language models work under the hood.", color: "text-purple-500", bg: "bg-purple-50 dark:bg-purple-950/30" },
  { icon: Code, title: "DSA in Java", description: "Practicing data structures and algorithms daily using Kunal Kushwaha Java series — currently on OOP and exception handling.", color: "text-blue-500", bg: "bg-blue-50 dark:bg-blue-950/30" },
  { icon: BookOpen, title: "Discrete Mathematics", description: "Graph theory, recurrence relations, and combinatorics as part of B.Tech Semester 2 curriculum.", color: "text-green-500", bg: "bg-green-50 dark:bg-green-950/30" },
  { icon: Flame, title: "React & Vite", description: "Building this portfolio and other projects to get hands-on with modern frontend tooling.", color: "text-orange-500", bg: "bg-orange-50 dark:bg-orange-950/30" },
];

export default function CurrentlyLearning() {
  return (
    <section id="currently-learning" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">In Progress</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Currently Learning</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">What I am actively studying and building right now.</p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
          {items.map((item, i) => (
            <motion.div
              key={item.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1, duration: 0.4 }}
              className={"rounded-xl p-6 border border-gray-200 dark:border-gray-800 " + item.bg}
            >
              <div className={"inline-flex p-2.5 rounded-lg mb-4 bg-white dark:bg-gray-900"}>
                <item.icon className={"w-5 h-5 " + item.color} />
              </div>
              <h3 className="font-semibold text-gray-900 dark:text-white mb-2">{item.title}</h3>
              <p className="text-sm text-gray-500 dark:text-gray-400 leading-relaxed">{item.description}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}'''
with open('src/app/components/CurrentlyLearning.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('CurrentlyLearning done!')
