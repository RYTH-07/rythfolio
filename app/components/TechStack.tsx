import { motion } from "motion/react";
import { RadialBarChart, RadialBar, ResponsiveContainer, PolarAngleAxis } from "recharts";

export default function TechStack() {
  const techData = [
    { name: "Python", value: 95, fill: "#3b82f6" },
    { name: "JavaScript", value: 88, fill: "#f59e0b" },
    { name: "React", value: 85, fill: "#06b6d4" },
    { name: "Node.js", value: 80, fill: "#22c55e" },
    { name: "TypeScript", value: 82, fill: "#8b5cf6" },
    { name: "C++", value: 78, fill: "#ec4899" },
    { name: "SQL", value: 75, fill: "#14b8a6" },
    { name: "Git", value: 92, fill: "#f97316" },
  ];

  return (
    <section className="py-20 px-4">
      <div className="container mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-12"
        >
          <h2 className="text-4xl md:text-5xl font-bold mb-4 bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent" style={{ fontFamily: 'Poppins, sans-serif' }}>
            Tech Stack Heatmap
          </h2>
          <p className="text-foreground/60">Proficiency across languages and frameworks</p>
        </motion.div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="relative"
          >
            <div className="absolute inset-0 bg-gradient-to-br from-blue-500/10 to-purple-500/10 rounded-3xl blur-2xl" />
            <div className="relative h-96 p-8 rounded-3xl bg-white/50 dark:bg-white/5 backdrop-blur-lg border border-white/20 dark:border-white/10">
              <ResponsiveContainer width="100%" height="100%">
                <RadialBarChart
                  innerRadius="10%"
                  outerRadius="90%"
                  data={techData}
                  startAngle={90}
                  endAngle={-270}
                >
                  <PolarAngleAxis type="number" domain={[0, 100]} tick={false} />
                  <RadialBar
                    background
                    dataKey="value"
                    cornerRadius={10}
                    label={{ position: 'insideStart', fill: '#fff', fontSize: 12 }}
                  />
                </RadialBarChart>
              </ResponsiveContainer>
            </div>
          </motion.div>

          <div className="space-y-4">
            {techData.map((tech, index) => (
              <motion.div
                key={tech.name}
                initial={{ opacity: 0, x: 30 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.05, duration: 0.4 }}
                whileHover={{ x: 5 }}
                className="relative group"
              >
                <div className="absolute inset-0 bg-gradient-to-r from-white/5 to-white/0 rounded-2xl blur-lg group-hover:blur-xl transition-all" />
                <div className="relative p-4 rounded-2xl bg-white/50 dark:bg-white/5 backdrop-blur-lg border border-white/20 dark:border-white/10 hover:border-white/30 transition-all">
                  <div className="flex items-center justify-between mb-2">
                    <div className="flex items-center gap-3">
                      <div className="w-3 h-3 rounded-full" style={{ backgroundColor: tech.fill }} />
                      <span className="font-semibold">{tech.name}</span>
                    </div>
                    <span className="text-sm font-bold" style={{ color: tech.fill }}>{tech.value}%</span>
                  </div>
                  <div className="h-2 bg-white/10 dark:bg-white/5 rounded-full overflow-hidden">
                    <motion.div
                      initial={{ width: 0 }}
                      whileInView={{ width: `${tech.value}%` }}
                      viewport={{ once: true }}
                      transition={{ delay: index * 0.05 + 0.3, duration: 1, ease: "easeOut" }}
                      className="h-full rounded-full"
                      style={{ backgroundColor: tech.fill }}
                    />
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
