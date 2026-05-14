import { motion } from "motion/react";
import { Code, GitCommit, Trophy, Flame } from "lucide-react";
import { useEffect, useState } from "react";

export default function StatsDashboard() {
  const [stats, setStats] = useState([
    { label: "Total Commits", value: 0, target: 2487, icon: GitCommit, color: "from-blue-400 to-cyan-500" },
    { label: "Problems Solved", value: 0, target: 1049, icon: Code, color: "from-purple-400 to-pink-500" },
    { label: "Contests Won", value: 0, target: 23, icon: Trophy, color: "from-yellow-400 to-orange-500" },
    { label: "Day Streak", value: 0, target: 147, icon: Flame, color: "from-red-400 to-rose-500" },
  ]);

  useEffect(() => {
    const duration = 2000;
    const steps = 60;
    const interval = duration / steps;

    let currentStep = 0;
    const timer = setInterval(() => {
      currentStep++;
      setStats(prev =>
        prev.map(stat => ({
          ...stat,
          value: Math.min(Math.floor((stat.target / steps) * currentStep), stat.target),
        }))
      );

      if (currentStep >= steps) {
        clearInterval(timer);
      }
    }, interval);

    return () => clearInterval(timer);
  }, []);

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
          <h2 className="text-4xl md:text-5xl font-bold mb-4 bg-gradient-to-r from-orange-400 to-red-400 bg-clip-text text-transparent" style={{ fontFamily: 'Poppins, sans-serif' }}>
            Stats Dashboard
          </h2>
          <p className="text-foreground/60">Real-time performance metrics</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="max-w-5xl mx-auto"
        >
          <div className="relative">
            <div className="absolute inset-0 bg-gradient-to-br from-orange-500/20 via-red-500/20 to-pink-500/20 rounded-3xl blur-2xl" />
            <div className="relative p-8 rounded-3xl bg-white/50 dark:bg-white/5 backdrop-blur-lg border border-white/20 dark:border-white/10">
              <div className="grid grid-cols-2 lg:grid-cols-4 gap-6">
                {stats.map((stat, index) => (
                  <motion.div
                    key={stat.label}
                    initial={{ opacity: 0, scale: 0.8 }}
                    whileInView={{ opacity: 1, scale: 1 }}
                    viewport={{ once: true }}
                    transition={{ delay: index * 0.1, duration: 0.4 }}
                    whileHover={{ scale: 1.05 }}
                    className="relative group"
                  >
                    <div className={`absolute inset-0 bg-gradient-to-br ${stat.color} opacity-0 group-hover:opacity-20 rounded-2xl blur-lg transition-all duration-300`} />
                    <div className="relative text-center p-6 rounded-2xl bg-white/30 dark:bg-white/5 border border-white/20 dark:border-white/10 hover:border-white/30 transition-all">
                      <div className={`inline-flex p-3 rounded-xl bg-gradient-to-br ${stat.color} mb-3`}>
                        <stat.icon className="w-6 h-6 text-white" />
                      </div>
                      <div className={`text-3xl font-bold mb-1 bg-gradient-to-r ${stat.color} bg-clip-text text-transparent`}>
                        {stat.value.toLocaleString()}
                      </div>
                      <div className="text-xs text-foreground/60 uppercase tracking-wide">
                        {stat.label}
                      </div>
                    </div>
                  </motion.div>
                ))}
              </div>

              <div className="mt-8 pt-8 border-t border-white/10">
                <div className="flex flex-wrap items-center justify-center gap-6 text-sm">
                  <div className="flex items-center gap-2">
                    <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
                    <span className="text-foreground/70">All systems active</span>
                  </div>
                  <div className="text-foreground/50">|</div>
                  <div className="text-foreground/70">
                    Last updated: <span className="font-semibold">Just now</span>
                  </div>
                  <div className="text-foreground/50">|</div>
                  <div className="text-foreground/70">
                    Rank: <span className="font-semibold bg-gradient-to-r from-yellow-400 to-orange-500 bg-clip-text text-transparent">Top 5%</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
