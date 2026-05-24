import { useEffect, useRef, useState } from "react";

const skills = [
  { name: "Python", color: "#3b82f6", current: true },
  { name: "Java", color: "#f97316", current: true },
  { name: "TypeScript", color: "#60a5fa", current: true },
  { name: "React", color: "#22d3ee", current: true },
  { name: "HTML/CSS", color: "#ec4899", current: true },
  { name: "JavaScript", color: "#facc15", current: true },
  { name: "Git", color: "#f87171", current: true },
  { name: "DSA", color: "#a78bfa", current: true },
  { name: "Flask", color: "#6ee7b7", current: false },
  { name: "NLP", color: "#c084fc", current: false },
  { name: "ML", color: "#fb923c", current: false },
  { name: "SQL", color: "#38bdf8", current: false },
  { name: "Node.js", color: "#4ade80", current: false },
];

type SkillPoint = {
  name: string;
  color: string;
  current: boolean;
  x: number;
  y: number;
  z: number;
};

export default function SkillsGlobe() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const angleRef = useRef(0);
  const mouseRef = useRef({ x: 0, y: 0, dragging: false, lastX: 0 });
  const rotYRef = useRef(0);
  const rotXRef = useRef(0.3);
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

    const R = 130;
    const total = skills.length;

    function getPositions(): SkillPoint[] {
      return skills.map((skill, i) => {
        const phi = Math.acos(-1 + (2 * i) / total);
        const theta = Math.sqrt(total * Math.PI) * phi + rotYRef.current;
        const sinPhi = Math.sin(phi + rotXRef.current);
        const cosPhi = Math.cos(phi + rotXRef.current);
        return {
          ...skill,
          x: R * sinPhi * Math.cos(theta),
          y: R * sinPhi * Math.sin(theta),
          z: R * cosPhi,
        };
      });
    }

    function draw() {
      if (!ctx || !canvas) return;
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      const cx = canvas.width / 2;
      const cy = canvas.height / 2;

      // Draw wireframe sphere
      ctx.strokeStyle = "rgba(96,165,250,0.12)";
      ctx.lineWidth = 0.5;
      for (let i = 0; i < 8; i++) {
        const a = (i / 8) * Math.PI;
        ctx.beginPath();
        for (let j = 0; j <= 60; j++) {
          const b = (j / 60) * Math.PI * 2 + rotYRef.current;
          const x = R * Math.sin(a) * Math.cos(b);
          const z = R * Math.sin(a) * Math.sin(b);
          const y = R * Math.cos(a);
          const scale = (z + R * 2) / (R * 3);
          if (j === 0) ctx.moveTo(cx + x * scale, cy + y * scale);
          else ctx.lineTo(cx + x * scale, cy + y * scale);
        }
        ctx.stroke();
      }
      for (let i = 0; i < 8; i++) {
        const b = (i / 8) * Math.PI * 2 + rotYRef.current;
        ctx.beginPath();
        for (let j = 0; j <= 60; j++) {
          const a = (j / 60) * Math.PI;
          const x = R * Math.sin(a) * Math.cos(b);
          const z = R * Math.sin(a) * Math.sin(b);
          const y = R * Math.cos(a);
          const scale = (z + R * 2) / (R * 3);
          if (j === 0) ctx.moveTo(cx + x * scale, cy + y * scale);
          else ctx.lineTo(cx + x * scale, cy + y * scale);
        }
        ctx.stroke();
      }

      const points = getPositions();
      const sorted = [...points].sort((a, b) => a.z - b.z);

      sorted.forEach((point) => {
        const scale = (point.z + R * 2) / (R * 3);
        const sx = cx + point.x * scale;
        const sy = cy + point.y * scale;
        const alpha = 0.4 + 0.6 * scale;
        const fontSize = Math.round(10 + 4 * scale);
        const isHovered = hoveredSkill === point.name;

        ctx.save();
        ctx.globalAlpha = alpha;
        ctx.font = `${isHovered ? "bold" : "600"} ${isHovered ? fontSize + 2 : fontSize}px Poppins, sans-serif`;
        ctx.fillStyle = point.color;
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";

        if (isHovered) {
          ctx.shadowColor = point.color;
          ctx.shadowBlur = 12;
        }

        ctx.fillText(point.name, sx, sy);

        if (!point.current) {
          ctx.strokeStyle = point.color;
          ctx.lineWidth = 0.5;
          ctx.globalAlpha = alpha * 0.4;
          const w = ctx.measureText(point.name).width;
          ctx.beginPath();
          ctx.moveTo(sx - w / 2, sy + fontSize / 2 + 1);
          ctx.lineTo(sx + w / 2, sy + fontSize / 2 + 1);
          ctx.stroke();
        }

        ctx.restore();
      });

      rotYRef.current += 0.004;
      animRef.current = requestAnimationFrame(draw);
    }

    draw();

    const onMouseMove = (e: MouseEvent) => {
      const rect = canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;

      if (mouseRef.current.dragging) {
        const dx = mx - mouseRef.current.lastX;
        rotYRef.current += dx * 0.01;
        mouseRef.current.lastX = mx;
      }

      // Check hover
      const cx = canvas.width / 2;
      const cy = canvas.height / 2;
      const points = getPositions();
      let found: string | null = null;
      points.forEach((point) => {
        const scale = (point.z + R * 2) / (R * 3);
        const sx = cx + point.x * scale;
        const sy = cy + point.y * scale;
        const dist = Math.sqrt((mx - sx) ** 2 + (my - sy) ** 2);
        if (dist < 30) found = point.name;
      });
      setHoveredSkill(found);
      canvas.style.cursor = found ? "pointer" : "grab";
    };

    const onMouseDown = (e: MouseEvent) => {
      mouseRef.current.dragging = true;
      mouseRef.current.lastX = e.clientX - canvas.getBoundingClientRect().left;
      canvas.style.cursor = "grabbing";
    };

    const onMouseUp = () => {
      mouseRef.current.dragging = false;
      canvas.style.cursor = "grab";
    };

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
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            Technologies I work with and aspiring to master. Drag the globe to explore.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
          <div className="h-[380px] w-full rounded-2xl border border-gray-100 dark:border-gray-800 bg-gray-50 dark:bg-gray-900 overflow-hidden">
            <canvas ref={canvasRef} className="w-full h-full" style={{ cursor: "grab" }} />
          </div>

          <div className="space-y-6">
            <div>
              <p className="text-xs font-semibold uppercase tracking-widest text-blue-600 dark:text-blue-400 mb-3">Currently Working With</p>
              <div className="flex flex-wrap gap-2">
                {skills.filter(s => s.current).map(skill => (
                  <span key={skill.name} className="px-3 py-1.5 rounded-full text-xs font-medium bg-blue-50 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800">
                    {skill.name}
                  </span>
                ))}
              </div>
            </div>
            <div>
              <p className="text-xs font-semibold uppercase tracking-widest text-purple-600 dark:text-purple-400 mb-3">Aspiring To Master</p>
              <div className="flex flex-wrap gap-2">
                {skills.filter(s => !s.current).map(skill => (
                  <span key={skill.name} className="px-3 py-1.5 rounded-full text-xs font-medium bg-purple-50 dark:bg-purple-950/40 text-purple-700 dark:text-purple-300 border border-purple-200 dark:border-purple-800 opacity-80">
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
                    {skills.find(s => s.name === hoveredSkill)?.current ? "Currently learning" : "Aspiring to master"}
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
