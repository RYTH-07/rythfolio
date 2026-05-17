import { useState, useEffect } from "react";
import { Home, Code2, FolderOpen, Trophy, Mail } from "lucide-react";

const sections = [
  { id: "hero", icon: Home, label: "Home" },
  { id: "code-matrix", icon: Code2, label: "Stats" },
  { id: "projects", icon: FolderOpen, label: "Projects" },
  { id: "achievements", icon: Trophy, label: "Wins" },
  { id: "contact", icon: Mail, label: "Contact" },
];

export default function MobileBottomNav() {
  const [active, setActive] = useState("hero");

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

  return (
    <div className="fixed bottom-0 left-0 right-0 z-50 lg:hidden bg-white/95 dark:bg-gray-950/95 backdrop-blur-md border-t border-gray-200 dark:border-gray-800">
      <div className="flex items-center justify-around px-2 py-2">
        {sections.map((section) => {
          const Icon = section.icon;
          const isActive = active === section.id;
          return (
            <button
              key={section.id}
              onClick={() => scrollTo(section.id)}
              className={"flex flex-col items-center gap-1 px-3 py-1.5 rounded-xl transition-all " +
                (isActive
                  ? "text-blue-600 dark:text-blue-400"
                  : "text-gray-400 dark:text-gray-500 hover:text-gray-700 dark:hover:text-gray-300"
                )}
            >
              <Icon className="w-5 h-5" />
              <span className="text-xs font-medium">{section.label}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
