code = '''import { useState, useEffect } from "react";

export default function PageLoader() {
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setLoaded(true), 800);
    return () => clearTimeout(timer);
  }, []);

  if (loaded) return null;

  return (
    <div className="fixed inset-0 z-[999] bg-white dark:bg-gray-950 flex flex-col items-center justify-center gap-4">
      <div className="relative">
        <div className="w-16 h-16 rounded-2xl bg-gray-900 dark:bg-white flex items-center justify-center">
          <span className="text-white dark:text-gray-900 font-bold text-2xl" style={{ fontFamily: "Poppins, sans-serif" }}>CR</span>
        </div>
        <div className="absolute -inset-1 rounded-2xl border-2 border-blue-500 animate-ping opacity-30" />
      </div>
      <div className="flex gap-1.5 mt-2">
        {[0, 1, 2].map(i => (
          <div
            key={i}
            className="w-1.5 h-1.5 rounded-full bg-blue-500"
            style={{ animation: "bounce 0.8s ease-in-out infinite", animationDelay: i * 0.15 + "s" }}
          />
        ))}
      </div>
      <style>{`
        @keyframes bounce {
          0%, 100% { transform: translateY(0); opacity: 0.4; }
          50% { transform: translateY(-6px); opacity: 1; }
        }
      `}</style>
    </div>
  );
}
'''

with open('src/app/components/PageLoader.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("PageLoader done!")
