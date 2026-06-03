code = '''import { useEffect, useRef, useState } from "react";

export default function CustomCursor() {
  const cursorRef = useRef<HTMLDivElement>(null);
  const [clicking, setClicking] = useState(false);
  const [hovering, setHovering] = useState(false);

  useEffect(() => {
    const onMove = (e: MouseEvent) => {
      if (cursorRef.current) {
        cursorRef.current.style.left = e.clientX + "px";
        cursorRef.current.style.top = e.clientY + "px";
      }
      const target = e.target as HTMLElement;
      setHovering(!!target.closest("a, button, [data-hover]"));
    };

    const onDown = () => setClicking(true);
    const onUp = () => setClicking(false);

    window.addEventListener("mousemove", onMove);
    window.addEventListener("mousedown", onDown);
    window.addEventListener("mouseup", onUp);
    document.body.style.cursor = "none";

    return () => {
      window.removeEventListener("mousemove", onMove);
      window.removeEventListener("mousedown", onDown);
      window.removeEventListener("mouseup", onUp);
      document.body.style.cursor = "auto";
    };
  }, []);

  const color = hovering ? "#a78bfa" : clicking ? "#60a5fa" : "#3b82f6";
  const glowColor = hovering ? "#7c3aed" : clicking ? "#2563eb" : "#1d4ed8";

  return (
    <div
      ref={cursorRef}
      className="pointer-events-none fixed z-[999] hidden lg:block"
      style={{
        transform: `translate(-4px, -4px) rotate(-35deg) scale(${clicking ? 0.8 : hovering ? 1.25 : 1})`,
        transition: "transform 0.15s ease, filter 0.2s ease",
        filter: `drop-shadow(0 0 6px ${color}) drop-shadow(0 0 12px ${glowColor}) drop-shadow(0 0 20px ${glowColor}88)`,
      }}
    >
      <svg width="28" height="32" viewBox="0 0 28 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        {/* Rocket body */}
        <path
          d="M14 2 C14 2 20 8 20 18 L14 30 L8 18 C8 8 14 2 14 2Z"
          fill={color + "22"}
          stroke={color}
          strokeWidth="1.5"
          strokeLinejoin="round"
        />
        {/* Rocket window */}
        <circle cx="14" cy="13" r="2.5" fill={color + "44"} stroke={color} strokeWidth="1.2" />
        {/* Left fin */}
        <path d="M8 18 L4 24 L8 22Z" fill={color + "33"} stroke={color} strokeWidth="1.2" strokeLinejoin="round" />
        {/* Right fin */}
        <path d="M20 18 L24 24 L20 22Z" fill={color + "33"} stroke={color} strokeWidth="1.2" strokeLinejoin="round" />
        {/* Flame */}
        <path
          d="M11 28 C11 28 12 32 14 30 C16 32 17 28 17 28 C16 29 14 31 14 30 C14 31 12 29 11 28Z"
          fill={clicking ? "#facc15" : hovering ? "#fb923c" : "#f97316"}
          style={{ transition: "fill 0.2s ease" }}
        />
      </svg>
    </div>
  );
}
'''

with open('src/app/components/CustomCursor.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("Neon rocket cursor done!")
