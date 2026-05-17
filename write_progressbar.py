code = '''import { useState, useEffect } from "react";

export default function ProgressBar() {
  const [progress, setProgress] = useState(0);
  const [visible, setVisible] = useState(true);

  useEffect(() => {
    const steps = [20, 50, 80, 100];
    const timings = [100, 300, 600, 1000];
    const timers: ReturnType<typeof setTimeout>[] = [];

    steps.forEach((step, i) => {
      timers.push(setTimeout(() => {
        setProgress(step);
        if (step === 100) {
          setTimeout(() => setVisible(false), 400);
        }
      }, timings[i]));
    });

    return () => timers.forEach(clearTimeout);
  }, []);

  if (!visible) return null;

  return (
    <div className="fixed top-0 left-0 right-0 z-[100] h-0.5 bg-transparent">
      <div
        className="h-full bg-blue-600 transition-all duration-300 ease-out"
        style={{ width: progress + "%" }}
      />
    </div>
  );
}
'''

with open('src/app/components/ProgressBar.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("ProgressBar done!")
