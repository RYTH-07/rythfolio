
code = '''import { useState, useEffect } from "react";

const sections = [
  { id: "hero", icon: "H", label: "Home" },
  { id: "techstack", icon: "S", label: "Skills" },
  { id: "code-matrix", icon: "C", label: "Code Stats" },
  { id: "github-heatmap", icon: "G", label: "GitHub" },
  { id: "projects", icon: "P", label: "Projects" },
  { id: "achievements", icon: "A", label: "Achievements" },
  { id: "certifications", icon: "Cr", label: "Certifications" },
  { id: "learning-journey", icon: "L", label: "Learning" },
  { id: "currently-learning", icon: "N", label: "Now" },
  { id: "contact", icon: "Co", label: "Contact" },
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
        { threshold: 0.4 }
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
      {sections.map((section) => (
        <div key={section.id} className="group relative flex items-center justify-end">
          <span className="absolute right-12 bg-gray-900 dark:bg-gray-100 text-white dark:text-gray-900 text-xs font-medium px-2.5 py-1 rounded-md opacity-0 group-hover:opacity-100 transition-all duration-200 whitespace-nowrap pointer-events-none translate-x-2 group-hover:translate-x-0">
            {section.label}
          </span>
          <button
            onClick={() => scrollTo(section.id)}
            className={"w-8 h-8 rounded-full border-2 flex items-center justify-center text-xs font-bold transition-all duration-200 " +
              (active === section.id
                ? "bg-blue-600 border-blue-600 text-white scale-110"
                : "bg-white dark:bg-gray-900 border-gray-300 dark:border-gray-600 text-gray-500 dark:text-gray-400 hover:border-blue-400 hover:text-blue-500"
              )}
          >
            {section.icon}
          </button>
        </div>
      ))}
    </div>
  );
}'''
with open('src/app/components/SideNav.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('SideNav done!')
