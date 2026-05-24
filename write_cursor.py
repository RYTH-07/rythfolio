code = '''import { useEffect, useRef } from "react";

export default function CursorSpotlight() {
  const spotlightRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!spotlightRef.current) return;
      spotlightRef.current.style.left = e.clientX + "px";
      spotlightRef.current.style.top = e.clientY + "px";
    };

    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, []);

  return (
    <div
      ref={spotlightRef}
      className="pointer-events-none fixed z-[200] hidden lg:block"
      style={{
        width: "400px",
        height: "400px",
        borderRadius: "50%",
        transform: "translate(-50%, -50%)",
        background: "radial-gradient(circle, rgba(37,99,235,0.06) 0%, transparent 70%)",
        transition: "left 0.1s ease, top 0.1s ease",
      }}
    />
  );
}
'''

with open('src/app/components/CursorSpotlight.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("CursorSpotlight done!")
