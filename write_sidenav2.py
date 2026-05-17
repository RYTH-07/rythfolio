
code = '''import { useState, useEffect } from "react";
import { Home, Code2, Github, FolderOpen, Trophy, Award, BookOpen, Lightbulb, Mail, BarChart2 } from "lucide-react";

const sections = [
  { id: "hero", icon: Home, label: "Home" },
  { id: "techstack", icon: BarChart2, label: "Skills" },
  { id: "code-matrix", icon: Code2, label: "Code Stats" },
  { id: "github-heatmap", icon: Github, label: "GitHub" },
  { id: "projects", icon: FolderOpen, label: "Projects" },
  { id: "achievements", icon: Trophy, label: "Achievements" },
  { id: "certifications", icon: Award, label: "Certifications" },
  { id: "learning-journey", icon: BookOpen, label: "Learning" },
  { id: "currently-learning", icon: Lightbulb, label: "Now Learning" },
  { id: "contact", icon: Mail, label: "Contact" },
];

export default function SideNav() {
  const [active, setActive] = useState("hero");
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setVisible(true), 1000);
    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    const observers: IntersectionObserver[] = [];
    sections.forEach(({ id }) => {
      const el = document.getElementById(id);
      if (!el) return;
      const obs = new IntersectionObserver(
        ([entry]) => { if (entry.isIntersecting) setActive(id); },
        { threshold: 0.3 }
      );
      obs.observe(el);
      observers.push(obs);
    });
    return () => observers.forEach(o => o.disconnect());
  }, []);

  const scrollTo = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
  };

  if (!visible) return null;

  return (
    <div className="fixed right-4 top-1/2 -translate-y-1/2 z-50 hidden lg:flex flex-col gap-2">
      {sections.map((section) => {
        const Icon = section.icon;
        const isActive = active === section.id;
        return (
          <div key={section.id} className="group relative flex items-center justify-end">
            <span className="absolute right-11 bg-gray-900 dark:bg-white text-white dark:text-gray-900 text-xs font-medium px-2.5 py-1 rounded-md opacity-0 group-hover:opacity-100 transition-all duration-200 whitespace-nowrap pointer-events-none translate-x-1 group-hover:translate-x-0 shadow-lg">
              {section.label}
            </span>
            <button
              onClick={() => scrollTo(section.id)}
              title={section.label}
              className={"w-8 h-8 rounded-full border-2 flex items-center justify-center transition-all duration-200 " +
                (isActive
                  ? "bg-blue-600 border-blue-600 text-white scale-110 shadow-lg shadow-blue-500/30"
                  : "bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-700 text-gray-400 dark:text-gray-500 hover:border-blue-400 hover:text-blue-500 dark:hover:text-blue-400"
                )}
            >
              <Icon className="w-3.5 h-3.5" />
            </button>
          </div>
        );
      })}
    </div>
  );
}'''
with open('src/app/components/SideNav.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('SideNav done!')
