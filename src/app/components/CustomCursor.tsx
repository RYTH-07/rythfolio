import { useEffect, useRef, useState } from "react";

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
        transform: "translate(-50%, -50%)",
        transition: "width 0.15s, height 0.15s, background 0.15s, border-color 0.15s",
        width: clicking ? "10px" : hovering ? "44px" : "20px",
        height: clicking ? "10px" : hovering ? "44px" : "20px",
        borderRadius: "50%",
        background: hovering
          ? "rgba(59,130,246,0.15)"
          : clicking
          ? "#3b82f6"
          : "rgba(255,255,255,0.9)",
        border: hovering ? "2px solid #3b82f6" : "none",
        boxShadow: hovering
          ? "0 0 12px rgba(59,130,246,0.4)"
          : clicking
          ? "0 0 8px rgba(59,130,246,0.6)"
          : "0 0 6px rgba(255,255,255,0.3)",
        mixBlendMode: hovering ? "normal" : "difference",
      }}
    />
  );
}
