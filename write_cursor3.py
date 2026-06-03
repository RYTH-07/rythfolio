code = '''import { useEffect, useRef, useState } from "react";

export default function CustomCursor() {
  const cursorRef = useRef<HTMLDivElement>(null);
  const dotRef = useRef<HTMLDivElement>(null);
  const pos = useRef({ x: 0, y: 0 });
  const current = useRef({ x: 0, y: 0 });
  const animRef = useRef<number>(0);
  const [clicking, setClicking] = useState(false);
  const [hovering, setHovering] = useState(false);

  useEffect(() => {
    const onMove = (e: MouseEvent) => {
      pos.current = { x: e.clientX, y: e.clientY };
      if (dotRef.current) {
        dotRef.current.style.left = e.clientX + "px";
        dotRef.current.style.top = e.clientY + "px";
      }

      const target = e.target as HTMLElement;
      const isHoverable = target.closest("a, button, [data-hover]");
      setHovering(!!isHoverable);
    };

    const onDown = () => setClicking(true);
    const onUp = () => setClicking(false);

    const animate = () => {
      current.current.x += (pos.current.x - current.current.x) * 0.12;
      current.current.y += (pos.current.y - current.current.y) * 0.12;
      if (cursorRef.current) {
        cursorRef.current.style.left = current.current.x + "px";
        cursorRef.current.style.top = current.current.y + "px";
      }
      animRef.current = requestAnimationFrame(animate);
    };

    window.addEventListener("mousemove", onMove);
    window.addEventListener("mousedown", onDown);
    window.addEventListener("mouseup", onUp);
    animRef.current = requestAnimationFrame(animate);

    document.body.style.cursor = "none";

    return () => {
      window.removeEventListener("mousemove", onMove);
      window.removeEventListener("mousedown", onDown);
      window.removeEventListener("mouseup", onUp);
      cancelAnimationFrame(animRef.current);
      document.body.style.cursor = "auto";
    };
  }, []);

  return (
    <>
      <div
        ref={cursorRef}
        className="pointer-events-none fixed z-[999] hidden lg:block"
        style={{
          width: hovering ? "48px" : clicking ? "20px" : "36px",
          height: hovering ? "48px" : clicking ? "20px" : "36px",
          borderRadius: "50%",
          border: hovering ? "2px solid #3b82f6" : "1.5px solid rgba(148,163,184,0.6)",
          background: hovering ? "rgba(59,130,246,0.08)" : "transparent",
          transform: "translate(-50%, -50%)",
          transition: "width 0.2s ease, height 0.2s ease, border-color 0.2s ease, background 0.2s ease",
        }}
      />
      <div
        ref={dotRef}
        className="pointer-events-none fixed z-[1000] hidden lg:block"
        style={{
          width: clicking ? "6px" : "5px",
          height: clicking ? "6px" : "5px",
          borderRadius: "50%",
          background: hovering ? "#3b82f6" : "#94a3b8",
          transform: "translate(-50%, -50%)",
          transition: "width 0.1s ease, height 0.1s ease, background 0.2s ease",
        }}
      />
    </>
  );
}
'''

with open('src/app/components/CustomCursor.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("CustomCursor done!")
