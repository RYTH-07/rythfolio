code = '''import { useEffect, useRef } from "react";

export default function CursorSpotlight() {
  const spotlightRef = useRef<HTMLDivElement>(null);
  const pos = useRef({ x: 0, y: 0 });
  const current = useRef({ x: 0, y: 0 });
  const animRef = useRef<number>(0);

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      pos.current = { x: e.clientX, y: e.clientY };
    };

    const animate = () => {
      current.current.x += (pos.current.x - current.current.x) * 0.08;
      current.current.y += (pos.current.y - current.current.y) * 0.08;

      if (spotlightRef.current) {
        spotlightRef.current.style.left = current.current.x + "px";
        spotlightRef.current.style.top = current.current.y + "px";
      }
      animRef.current = requestAnimationFrame(animate);
    };

    window.addEventListener("mousemove", handleMouseMove);
    animRef.current = requestAnimationFrame(animate);

    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      cancelAnimationFrame(animRef.current);
    };
  }, []);

  return (
    <div
      ref={spotlightRef}
      className="pointer-events-none fixed z-[200] hidden lg:block"
      style={{
        width: "500px",
        height: "500px",
        borderRadius: "50%",
        transform: "translate(-50%, -50%)",
        background: "radial-gradient(circle, rgba(37,99,235,0.07) 0%, rgba(139,92,246,0.04) 40%, transparent 70%)",
      }}
    />
  );
}
'''

with open('src/app/components/CursorSpotlight.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("CursorSpotlight improved!")
