import { useEffect, useRef, useState } from "react";

export default function CustomCursor() {
  const cursorRef = useRef<HTMLDivElement>(null);
  const [clicking, setClicking] = useState(false);
  const [hovering, setHovering] = useState(false);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const onMove = (e: MouseEvent) => {
      if (cursorRef.current) {
        cursorRef.current.style.left = e.clientX + "px";
        cursorRef.current.style.top = e.clientY + "px";
      }
      const target = e.target as HTMLElement;
      setHovering(!!target.closest("a, button, [data-hover]"));
    };

    const onEnter = () => setVisible(true);
    const onLeave = () => setVisible(false);
    const onDown = () => setClicking(true);
    const onUp = () => setClicking(false);

    document.addEventListener("mousemove", onMove);
    document.addEventListener("mouseenter", onEnter);
    document.addEventListener("mouseleave", onLeave);
    document.addEventListener("mousedown", onDown);
    document.addEventListener("mouseup", onUp);

    const style = document.createElement("style");
    style.id = "cursor-none-style";
    style.textContent = `*, *::before, *::after { cursor: none !important; }`;
    document.head.appendChild(style);

    return () => {
      document.removeEventListener("mousemove", onMove);
      document.removeEventListener("mouseenter", onEnter);
      document.removeEventListener("mouseleave", onLeave);
      document.removeEventListener("mousedown", onDown);
      document.removeEventListener("mouseup", onUp);
      document.getElementById("cursor-none-style")?.remove();
    };
  }, []);

  const color = hovering ? "#a78bfa" : "#3b82f6";
  const glow = hovering ? "#7c3aed" : "#1d4ed8";

  return (
    <div
      ref={cursorRef}
      className="pointer-events-none fixed z-[9999] hidden lg:block"
      style={{
        transform: `translate(-1px, -1px) scale(${clicking ? 0.75 : hovering ? 1.15 : 1})`,
        transition: "transform 0.12s ease, opacity 0.15s ease, filter 0.2s ease",
        opacity: visible ? 1 : 0,
        filter: `drop-shadow(0 0 4px ${color}) drop-shadow(0 0 8px ${glow})`,
      }}
    >
      <svg width="20" height="24" viewBox="0 0 20 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        {/* Top-left pointing triangle - like default OS cursor */}
        <path
          d="M2 2 L2 20 L7 14 L11 22 L14 21 L10 13 L17 13 Z"
          fill={color + "30"}
          stroke={color}
          strokeWidth="1.5"
          strokeLinejoin="round"
          strokeLinecap="round"
        />
      </svg>
    </div>
  );
}
