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

  return (
    <div
      ref={cursorRef}
      className="pointer-events-none fixed z-[999] hidden lg:block"
      style={{
        transform: clicking ? "scale(0.85)" : hovering ? "scale(1.2)" : "scale(1)",
        transition: "transform 0.15s ease",
        filter: hovering
          ? "drop-shadow(0 0 6px #3b82f6)"
          : clicking
          ? "drop-shadow(0 0 4px #60a5fa)"
          : "drop-shadow(0 0 2px rgba(255,255,255,0.4))",
      }}
    >
      <svg
        width="22"
        height="26"
        viewBox="0 0 22 26"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M2 2L2 20L7.5 15L11 22L13.5 21L10 14L17 14L2 2Z"
          fill={hovering ? "#3b82f6" : "white"}
          stroke={hovering ? "#1d4ed8" : "#374151"}
          strokeWidth="1.5"
          strokeLinejoin="round"
          style={{ transition: "fill 0.2s ease" }}
        />
      </svg>
    </div>
  );
}
'''

with open('src/app/components/CustomCursor.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("Arrow cursor done!")
