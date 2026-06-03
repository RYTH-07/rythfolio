code = '''import { useEffect, useRef, useState } from "react";

const skills = [
  { name: "Python", color: "#3b82f6", current: true, size: 14 },
  { name: "Java", color: "#f97316", current: true, size: 13 },
  { name: "TypeScript", color: "#60a5fa", current: true, size: 13 },
  { name: "React", color: "#22d3ee", current: true, size: 14 },
  { name: "HTML/CSS", color: "#ec4899", current: true, size: 12 },
  { name: "JavaScript", color: "#facc15", current: true, size: 12 },
  { name: "Git", color: "#f87171", current: true, size: 12 },
  { name: "DSA", color: "#a78bfa", current: true, size: 13 },
  { name: "Supabase", color: "#34d399", current: true, size: 11 },
  { name: "Claude API", color: "#818cf8", current: true, size: 11 },
  { name: "Flask", color: "#6ee7b7", current: false, size: 11 },
  { name: "NLP", color: "#c084fc", current: false, size: 12 },
  { name: "ML", color: "#fb923c", current: false, size: 12 },
  { name: "SQL", color: "#38bdf8", current: false, size: 11 },
  { name: "Node.js", color: "#4ade80", current: false, size: 11 },
];

type Point = { name: string; color: string; current: boolean; size: number; x: number; y: number; z: number };

export default function SkillsGlobe() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const rotY = useRef(0);
  const animRef = useRef<number>(0);
  const dragging = useRef(false);
  const lastX = useRef(0);
  const [hovered, setHovered] = useState<string | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const resize = () => {
      canvas.width = canvas.offsetWidth;
      canvas.height = canvas.offsetHeight;
    };
    resize();
    window.addEventListener("resize", resize);

    const R = Math.min(canvas.width, canvas.height) * 0.38;
    const N = skills.length;

    const getPoints = (): Point[] =>
      skills.map((s, i) => {
        const phi = Math.acos(-1 + (2 * i) / N);
        const theta = Math.sqrt(N * Math.PI) * phi + rotY.current;
        return {
          ...s,
          x: R * Math.sin(phi) * Math.cos(theta),
          y: R * Math.cos(phi),
          z: R * Math.sin(phi) * Math.sin(theta),
        };
      });

    const draw = () => {
      if (!ctx || !canvas) return;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const cx = canvas.width / 2;
      const cy = canvas.height / 2;

      // Draw visible wireframe sphere rings
      const rings = 8;
      for (let i = 1; i < rings; i++) {
        const phi = (i / rings) * Math.PI;
        const ringR = R * Math.sin(phi);
        const ringY = R * Math.cos(phi);
        ctx.beginPath();
        ctx.ellipse(cx, cy + ringY, ringR, ringR * 0.35, 0, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(96,165,250,0.18)";
        ctx.lineWidth = 0.8;
        ctx.stroke();
      }

      // Vertical arcs
      for (let i = 0; i < 8; i++) {
        const angle = (i / 8) * Math.PI + rotY.current;
        ctx.beginPath();
        for (let j = 0; j <= 60; j++) {
          const phi = (j / 60) * Math.PI;
          const x = R * Math.sin(phi) * Math.cos(angle);
          const y = R * Math.cos(phi);
          const z = R * Math.sin(phi) * Math.sin(angle);
          const scale = (z + R * 2) / (R * 3);
          const sx = cx + x * scale;
          const sy = cy + y * 0.6 * scale + y * 0.4;
          j === 0 ? ctx.moveTo(sx, sy) : ctx.lineTo(sx, sy);
        }
        ctx.strokeStyle = "rgba(139,92,246,0.12)";
        ctx.lineWidth = 0.6;
        ctx.stroke();
      }

      // Outer glow circle
      const grad = ctx.createRadialGradient(cx, cy, R * 0.7, cx, cy, R * 1.1);
      grad.addColorStop(0, "rgba(59,130,246,0.03)");
      grad.addColorStop(1, "rgba(59,130,246,0)");
      ctx.beginPath();
      ctx.arc(cx, cy, R * 1.1, 0, Math.PI * 2);
      ctx.fillStyle = grad;
      ctx.fill();

      // Draw skill labels
      const points = getPoints().sort((a, b) => a.z - b.z);
      points.forEach((p) => {
        const depth = (p.z + R) / (2 * R);
        const scale = 0.5 + depth * 0.5;
        const alpha = 0.3 + depth * 0.7;
        const sx = cx + p.x;
        const sy = cy + p.y * 0.6 + p.z * 0.15;
        const fs = Math.round(p.size * scale);
        const isHov = hovered === p.name;

        ctx.save();
        ctx.globalAlpha = alpha;
        ctx.font = `${isHov ? 700 : 600} ${isHov ? fs + 2 : fs}px Poppins, sans-serif`;
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";

        if (depth > 0.6 || isHov) {
          ctx.shadowColor = p.color;
          ctx.shadowBlur = isHov ? 16 : 6 * depth;
        }

        ctx.fillStyle = p.color;
        ctx.fillText(p.name, sx, sy);

        if (!p.current) {
          ctx.lineWidth = 0.7;
          ctx.strokeStyle = p.color;
          ctx.globalAlpha = alpha * 0.4;
          const w = ctx.measureText(p.name).width;
          ctx.beginPath();
          ctx.moveTo(sx - w / 2, sy + fs / 2 + 1);
          ctx.lineTo(sx + w / 2, sy + fs / 2 + 1);
          ctx.stroke();
        }
        ctx.restore();
      });

      rotY.current += 0.004;
      animRef.current = requestAnimationFrame(draw);
    };

    draw();

    const onMove = (e: MouseEvent) => {
      const rect = canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;
      if (dragging.current) {
        rotY.current += (mx - lastX.current) * 0.007;
        lastX.current = mx;
      }
      const cx = canvas.width / 2;
      const cy = canvas.height / 2;
      const pts = getPoints();
      let found: string | null = null;
      pts.forEach((p) => {
        const sx = cx + p.x;
        const sy = cy + p.y * 0.6 + p.z * 0.15;
        if (Math.hypot(mx - sx, my - sy) < 32) found = p.name;
      });
      setHovered(found);
    };

    const onDown = (e: MouseEvent) => { dragging.current = true; lastX.current = e.clientX - canvas.getBoundingClientRect().left; };
    const onUp = () => { dragging.current = false; };

    canvas.addEventListener("mousemove", onMove);
    canvas.addEventListener("mousedown", onDown);
    window.addEventListener("mouseup", onUp);

    return () => {
      cancelAnimationFrame(animRef.current);
      window.removeEventListener("resize", resize);
      canvas.removeEventListener("mousemove", onMove);
      canvas.removeEventListener("mousedown", onDown);
      window.removeEventListener("mouseup", onUp);
    };
  }, [hovered]);

  return (
    <section id="techstack" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Skills</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Tech Stack</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">Technologies I work with and aspiring to master. Drag the globe to explore.</p>
        </div>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
          <div className="relative h-[420px] w-full rounded-2xl overflow-hidden border border-gray-200 dark:border-gray-700 bg-[#0a0f1e]">
            <div className="absolute inset-0 bg-gradient-radial from-blue-900/20 via-transparent to-purple-900/10 pointer-events-none" />
            <canvas ref={canvasRef} className="w-full h-full" style={{ cursor: "grab" }} />
          </div>
          <div className="space-y-6">
            <div>
              <p className="text-xs font-semibold uppercase tracking-widest text-blue-500 mb-3">Currently Working With</p>
              <div className="flex flex-wrap gap-2">
                {skills.filter(s => s.current).map(s => (
                  <span key={s.name} style={{ color: s.color, borderColor: s.color + "50" }}
                    className="px-3 py-1 rounded-full text-xs font-semibold border bg-white dark:bg-gray-900">
                    {s.name}
                  </span>
                ))}
              </div>
            </div>
            <div>
              <p className="text-xs font-semibold uppercase tracking-widest text-purple-500 mb-3">Aspiring To Master</p>
              <div className="flex flex-wrap gap-2">
                {skills.filter(s => !s.current).map(s => (
                  <span key={s.name} style={{ color: s.color + "bb", borderColor: s.color + "30" }}
                    className="px-3 py-1 rounded-full text-xs font-semibold border bg-white dark:bg-gray-900 opacity-75">
                    {s.name}
                  </span>
                ))}
              </div>
            </div>
            {hovered && (
              <div className="p-3 rounded-xl bg-gray-100 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 transition-all">
                <p className="text-sm font-semibold text-gray-900 dark:text-white">
                  {hovered}
                  <span className="ml-2 text-xs font-normal text-gray-400">
                    {skills.find(s => s.name === hovered)?.current ? "Currently using" : "Aspiring"}
                  </span>
                </p>
              </div>
            )}
            <p className="text-xs text-gray-400 italic">Drag to spin · Hover to highlight</p>
          </div>
        </div>
      </div>
    </section>
  );
}
'''

with open('src/app/components/SkillsGlobe.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("Enhanced SkillsGlobe done!")
