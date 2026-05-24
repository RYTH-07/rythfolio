code = '''import { useRef, useMemo } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { Text, OrbitControls } from "@react-three/drei";
import * as THREE from "three";

const skills = [
  // Current skills
  { name: "Python", color: "#3b82f6", size: 0.13 },
  { name: "Java", color: "#f97316", size: 0.12 },
  { name: "TypeScript", color: "#60a5fa", size: 0.11 },
  { name: "React", color: "#22d3ee", size: 0.12 },
  { name: "HTML/CSS", color: "#ec4899", size: 0.11 },
  { name: "JavaScript", color: "#facc15", size: 0.11 },
  { name: "Git", color: "#f87171", size: 0.11 },
  { name: "DSA", color: "#a78bfa", size: 0.12 },
  // Aspiring
  { name: "Flask", color: "#6ee7b7", size: 0.10 },
  { name: "NLP", color: "#c084fc", size: 0.10 },
  { name: "ML", color: "#fb923c", size: 0.10 },
  { name: "SQL", color: "#38bdf8", size: 0.10 },
  { name: "Node.js", color: "#4ade80", size: 0.10 },
];

function getPositionOnSphere(index: number, total: number, radius: number) {
  const phi = Math.acos(-1 + (2 * index) / total);
  const theta = Math.sqrt(total * Math.PI) * phi;
  return new THREE.Vector3(
    radius * Math.sin(phi) * Math.cos(theta),
    radius * Math.sin(phi) * Math.sin(theta),
    radius * Math.cos(phi)
  );
}

function SkillLabel({ position, name, color, size }: {
  position: THREE.Vector3;
  name: string;
  color: string;
  size: number;
}) {
  const ref = useRef<THREE.Mesh>(null);

  useFrame(({ camera }) => {
    if (ref.current) {
      ref.current.quaternion.copy(camera.quaternion);
    }
  });

  return (
    <group position={position}>
      <Text
        ref={ref}
        fontSize={size}
        color={color}
        anchorX="center"
        anchorY="middle"
        font="https://fonts.gstatic.com/s/poppins/v20/pxiEyp8kv8JHgFVrJJfecg.woff2"
      >
        {name}
      </Text>
    </group>
  );
}

function WireframeSphere() {
  const geometry = useMemo(() => new THREE.SphereGeometry(1.4, 24, 24), []);
  return (
    <mesh geometry={geometry}>
      <meshBasicMaterial color="#3b82f6" wireframe opacity={0.08} transparent />
    </mesh>
  );
}

function Globe() {
  const groupRef = useRef<THREE.Group>(null);

  useFrame((_, delta) => {
    if (groupRef.current) {
      groupRef.current.rotation.y += delta * 0.2;
    }
  });

  const positions = useMemo(() =>
    skills.map((_, i) => getPositionOnSphere(i, skills.length, 1.5)),
    []
  );

  return (
    <group ref={groupRef}>
      <WireframeSphere />
      {skills.map((skill, i) => (
        <SkillLabel
          key={skill.name}
          position={positions[i]}
          name={skill.name}
          color={skill.color}
          size={skill.size}
        />
      ))}
    </group>
  );
}

export default function SkillsGlobe() {
  return (
    <section id="techstack" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Skills</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Tech Stack</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            Technologies I work with and aspiring to master. Drag to explore.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
          <div className="h-[420px] w-full rounded-2xl overflow-hidden border border-gray-100 dark:border-gray-800 bg-gray-50 dark:bg-gray-900">
            <Canvas camera={{ position: [0, 0, 4], fov: 45 }}>
              <ambientLight intensity={0.5} />
              <pointLight position={[10, 10, 10]} />
              <Globe />
              <OrbitControls
                enableZoom={false}
                enablePan={false}
                autoRotate={false}
              />
            </Canvas>
          </div>

          <div className="space-y-6">
            <div>
              <p className="text-xs font-semibold uppercase tracking-widest text-blue-600 dark:text-blue-400 mb-3">Currently Working With</p>
              <div className="flex flex-wrap gap-2">
                {["Python", "Java", "TypeScript", "React", "HTML/CSS", "JavaScript", "Git", "DSA"].map(skill => (
                  <span key={skill} className="px-3 py-1.5 rounded-full text-xs font-medium bg-blue-50 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800">
                    {skill}
                  </span>
                ))}
              </div>
            </div>
            <div>
              <p className="text-xs font-semibold uppercase tracking-widest text-purple-600 dark:text-purple-400 mb-3">Aspiring To Master</p>
              <div className="flex flex-wrap gap-2">
                {["Flask", "NLP", "Machine Learning", "SQL", "Node.js"].map(skill => (
                  <span key={skill} className="px-3 py-1.5 rounded-full text-xs font-medium bg-purple-50 dark:bg-purple-950/40 text-purple-700 dark:text-purple-300 border border-purple-200 dark:border-purple-800">
                    {skill}
                  </span>
                ))}
              </div>
            </div>
            <p className="text-xs text-gray-400 dark:text-gray-500 italic">Drag the globe to explore all skills</p>
          </div>
        </div>
      </div>
    </section>
  );
}
'''

with open('src/app/components/SkillsGlobe.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("SkillsGlobe done!")
