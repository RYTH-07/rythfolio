code = '''import { useEffect, useRef, useState } from "react";

const skills = [
  { name: "Python", color: "#3b82f6", current: true, size: 15 },
  { name: "Java", color: "#f97316", current: true, size: 14 },
  { name: "TypeScript", color: "#60a5fa", current: true, size: 13 },
  { name: "React", color: "#22d3ee", current: true, size: 14 },
  { name: "HTML/CSS", color: "#ec4899", current: true, size: 13 },
  { name: "JavaScript", color: "#facc15", current: true, size: 13 },
  { name: "Git", color: "#f87171", current: true, size: 13 },
  { name: "DSA", color: "#a78bfa", current: true, size: 14 },
  { name: "Supabase", color: "#34d399", current: true, size: 12 },
  { name: "Flask", color: "#6ee7b7", current: false, size: 12 },
  { name: "NLP", color: "#c084fc", current: false, size: 13 },
  { name: "ML", color: "#fb923c", current: false, size: 13 },
  { name: "SQL", color: "#38bdf8", current: false, size: 12 },
  { name: "Node.js", color: "#4ade80", current: false, size: 12 },
  { name: "Claude API", color: "#818cf8", current: true, size: 12 },
];

type SkillPoint = {
  name: string;
  color: string;
  current: boolean;
  size: number;
  x: number;
  y: number;
  z: number;
};

export default function SkillsGlobe() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const rotYRef = useRef(0);
  const rotXRef = useRef(0.2);
  const mouseRef = useRef({ dragging: false, lastX: 0 });
  const animRef = useRef<number>(0);
  const [hoveredSkill, setHoveredSkill] = useState<string | null>(null);

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

    const R = 140;
    const total = skills.length;

    function getPositions(): SkillPoint[] {
      return skills.map((skill, i) => {
        const phi = Math.acos(-1 + (2 * i) / total);
        const theta = Math.sqrt(total * Math.PI) * phi + rotYRef.current;
        const sinX = Math.sin(rotXRef.current);
        const cosX = Math.cos(rotXRef.current);
        const x0 = R * Math.sin(phi) * Math.cos(theta);
        const y0 = R * Math.sin(phi) * Math.sin(theta);
        const z0 = R * Math.cos(phi);
        return {
          ...skill,
          x: x0,
          y: y0 * cosX - z0 * sinX,
          z: y0 * sinX + z0 * cosX,
        };
      });
    }

    function hexToRgb(hex: string) {
      const r = parseInt(hex.slice(1, 3), 16);
      const g = parseInt(hex.slice(3, 5), 16);
      const b = parseInt(hex.slice(5, 7), 16);
      return { r, g, b };
    }

    function draw() {
      if (!ctx || !canvas) return;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const cx = canvas.width / 2;
      const cy = canvas.height / 2;

      // Wireframe
      for (let i = 0; i < 10; i++) {
        const a = (i / 10) * Math.PI;
        ctx.beginPath();
        ctx.strokeStyle = "rgba(96,165,250,0.08)";
        ctx.lineWidth = 0.5;
        for (let j = 0; j <= 64; j++) {
          const b = (j / 64) * Math.PI * 2 + rotYRef.current;
          const x = R * Math.sin(a) * Math.cos(b);
          const z = R * Math.sin(a) * Math.sin(b);
          const y = R * Math.cos(a);
          const scale = (z + R * 2) / (R * 3);
          j === 0 ? ctx.moveTo(cx + x * scale, cy + y * scale) : ctx.lineTo(cx + x * scale, cy + y * scale);
        }
        ctx.stroke();
      }
      for (let i = 0; i < 10; i++) {
        const b = (i / 10) * Math.PI * 2 + rotYRef.current;
        ctx.beginPath();
        ctx.strokeStyle = "rgba(96,165,250,0.08)";
        ctx.lineWidth = 0.5;
        for (let j = 0; j <= 64; j++) {
          const a = (j / 64) * Math.PI;
          const x = R * Math.sin(a) * Math.cos(b);
          const z = R * Math.sin(a) * Math.sin(b);
          const y = R * Math.cos(a);
          const scale = (z + R * 2) / (R * 3);
          j === 0 ? ctx.moveTo(cx + x * scale, cy + y * scale) : ctx.lineTo(cx + x * scale, cy + y * scale);
        }
        ctx.stroke();
      }

      const points = getPositions();
      const sorted = [...points].sort((a, b) => a.z - b.z);

      sorted.forEach((point) => {
        const scale = (point.z + R * 2) / (R * 3);
        const sx = cx + point.x * scale;
        const sy = cy + point.y * scale;
        const alpha = 0.35 + 0.65 * scale;
        const fontSize = Math.round((point.size - 2) + 4 * scale);
        const isHovered = hoveredSkill === point.name;
        const rgb = hexToRgb(point.color);

        ctx.save();
        ctx.globalAlpha = alpha;

        if (isHovered || scale > 0.75) {
          ctx.shadowColor = point.color;
          ctx.shadowBlur = isHovered ? 20 : 8 * scale;
        }

        ctx.font = `${isHovered ? "700" : "600"} ${isHovered ? fontSize + 3 : fontSize}px Poppins, sans-serif`;
        ctx.fillStyle = point.color;
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(point.name, sx, sy);

        if (!point.current) {
          ctx.strokeStyle = `rgba(${rgb.r},${rgb.g},${rgb.b},0.5)`;
          ctx.lineWidth = 0.8;
          ctx.globalAlpha = alpha * 0.5;
          const w = ctx.measureText(point.name).width;
          ctx.beginPath();
          ctx.moveTo(sx - w / 2, sy + fontSize / 2 + 1);
          ctx.lineTo(sx + w / 2, sy + fontSize / 2 + 1);
          ctx.stroke();
        }

        ctx.restore();
      });

      rotYRef.current += 0.003;
      animRef.current = requestAnimationFrame(draw);
    }

    draw();

    const onMouseMove = (e: MouseEvent) => {
      const rect = canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;

      if (mouseRef.current.dragging) {
        rotYRef.current += (mx - mouseRef.current.lastX) * 0.008;
        mouseRef.current.lastX = mx;
      }

      const cx = canvas.width / 2;
      const cy = canvas.height / 2;
      const points = getPositions();
      let found: string | null = null;
      points.forEach((point) => {
        const scale = (point.z + R * 2) / (R * 3);
        const sx = cx + point.x * scale;
        const sy = cy + point.y * scale;
        if (Math.sqrt((mx - sx) ** 2 + (my - sy) ** 2) < 35) found = point.name;
      });
      setHoveredSkill(found);
    };

    const onMouseDown = (e: MouseEvent) => {
      mouseRef.current.dragging = true;
      mouseRef.current.lastX = e.clientX - canvas.getBoundingClientRect().left;
    };
    const onMouseUp = () => { mouseRef.current.dragging = false; };

    canvas.addEventListener("mousemove", onMouseMove);
    canvas.addEventListener("mousedown", onMouseDown);
    window.addEventListener("mouseup", onMouseUp);

    return () => {
      cancelAnimationFrame(animRef.current);
      window.removeEventListener("resize", resize);
      canvas.removeEventListener("mousemove", onMouseMove);
      canvas.removeEventListener("mousedown", onMouseDown);
      window.removeEventListener("mouseup", onMouseUp);
    };
  }, [hoveredSkill]);

  return (
    <section id="techstack" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Skills</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Tech Stack</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">Technologies I work with and aspiring to master. Drag the globe to explore.</p>
        </div>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
          <div className="h-[420px] w-full rounded-2xl border border-gray-100 dark:border-gray-800 bg-gray-950 overflow-hidden relative">
            <div className="absolute inset-0 bg-gradient-to-br from-blue-950/30 via-transparent to-purple-950/20 pointer-events-none" />
            <canvas ref={canvasRef} className="w-full h-full" style={{ cursor: "grab" }} />
          </div>
          <div className="space-y-6">
            <div>
              <p className="text-xs font-semibold uppercase tracking-widest text-blue-600 dark:text-blue-400 mb-3">Currently Working With</p>
              <div className="flex flex-wrap gap-2">
                {skills.filter(s => s.current).map(skill => (
                  <span key={skill.name} style={{ borderColor: skill.color + "40", color: skill.color }}
                    className="px-3 py-1.5 rounded-full text-xs font-medium bg-gray-50 dark:bg-gray-900 border">
                    {skill.name}
                  </span>
                ))}
              </div>
            </div>
            <div>
              <p className="text-xs font-semibold uppercase tracking-widest text-purple-600 dark:text-purple-400 mb-3">Aspiring To Master</p>
              <div className="flex flex-wrap gap-2">
                {skills.filter(s => !s.current).map(skill => (
                  <span key={skill.name} style={{ borderColor: skill.color + "30", color: skill.color }}
                    className="px-3 py-1.5 rounded-full text-xs font-medium bg-gray-50 dark:bg-gray-900 border opacity-70">
                    {skill.name}
                  </span>
                ))}
              </div>
            </div>
            {hoveredSkill && (
              <div className="p-3 rounded-xl bg-gray-100 dark:bg-gray-800 border border-gray-200 dark:border-gray-700">
                <p className="text-sm font-medium text-gray-900 dark:text-white">
                  {hoveredSkill}
                  <span className="ml-2 text-xs text-gray-400">
                    {skills.find(s => s.name === hoveredSkill)?.current ? "Currently using" : "Aspiring to master"}
                  </span>
                </p>
              </div>
            )}
            <p className="text-xs text-gray-400 dark:text-gray-500 italic">Drag the globe to spin it</p>
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
