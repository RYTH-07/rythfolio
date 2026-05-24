import re

with open('src/app/components/Hero.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the static stats section with animated count-up version
old_stats = '''        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.8 }} className="mt-16 pt-8 border-t border-gray-100 dark:border-gray-800 flex flex-wrap gap-8">
          <div><p className="text-2xl font-semibold text-gray-900 dark:text-white">2</p><p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Projects</p></div>
          <div><p className="text-2xl font-semibold text-gray-900 dark:text-white">12</p><p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Problems Solved</p></div>
          <div><p className="text-2xl font-semibold text-gray-900 dark:text-white">8.22</p><p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Sem 1 SGPA</p></div>
          <div><p className="text-2xl font-semibold text-gray-900 dark:text-white">1</p><p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Certification</p></div>
        </motion.div>'''

new_stats = '''        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.8 }} className="mt-16 pt-8 border-t border-gray-100 dark:border-gray-800 flex flex-wrap gap-8">
          {[
            { value: 2, label: "Projects", suffix: "" },
            { value: 12, label: "Problems Solved", suffix: "+" },
            { value: 8.22, label: "Sem 1 SGPA", suffix: "", decimal: true },
            { value: 1, label: "Certification", suffix: "" },
          ].map((stat, i) => (
            <CountUp key={stat.label} {...stat} delay={0.9 + i * 0.1} />
          ))}
        </motion.div>'''

code = code.replace(old_stats, new_stats)

# Add CountUp component and useRef import
old_import = 'import { useEffect, useState, useRef } from "react";'
new_import = '''import { useEffect, useState, useRef } from "react";

function CountUp({ value, label, suffix, decimal, delay }: { value: number; label: string; suffix: string; decimal?: boolean; delay: number }) {
  const [count, setCount] = useState(0);
  const ref = useRef<HTMLDivElement>(null);
  const started = useRef(false);

  useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting && !started.current) {
        started.current = true;
        const duration = 1500;
        const steps = 60;
        const increment = value / steps;
        let current = 0;
        const timer = setInterval(() => {
          current += increment;
          if (current >= value) {
            setCount(value);
            clearInterval(timer);
          } else {
            setCount(decimal ? Math.round(current * 100) / 100 : Math.floor(current));
          }
        }, duration / steps);
      }
    }, { threshold: 0.5 });
    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, [value, decimal]);

  return (
    <div ref={ref}>
      <p className="text-2xl font-semibold text-gray-900 dark:text-white">
        {decimal ? count.toFixed(2) : count}{suffix}
      </p>
      <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">{label}</p>
    </div>
  );
}'''

if 'function CountUp' not in code:
    code = code.replace(old_import, new_import)

with open('src/app/components/Hero.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("Hero count-up animation done!")
