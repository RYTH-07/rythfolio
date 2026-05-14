import { ArrowUpRight } from "lucide-react";

const projects = [
  {
    title: "Project Alpha",
    description: "Placeholder — a full-stack web application. Add your tech stack, problem solved, and impact here.",
    tags: ["React", "Node.js", "MongoDB"],
  },
  {
    title: "Project Beta",
    description: "Placeholder — a machine learning project. Add your dataset, model architecture, and results here.",
    tags: ["Python", "TensorFlow", "FastAPI"],
  },
  {
    title: "Project Gamma",
    description: "Placeholder — a mobile application. Add your platform, key features, and user base here.",
    tags: ["Flutter", "Firebase", "Dart"],
  },
  {
    title: "Project Delta",
    description: "Placeholder — a systems programming project. Add your language, OS, and performance outcomes here.",
    tags: ["C++", "Linux", "OpenGL"],
  },
  {
    title: "Project Epsilon",
    description: "Placeholder — a data engineering pipeline. Add your data sources, transformations, and scale here.",
    tags: ["Python", "Apache Spark", "SQL"],
  },
  {
    title: "Project Zeta",
    description: "Placeholder — a DevOps or tooling project. Add your workflow, automation gains, and stack here.",
    tags: ["Docker", "Kubernetes", "CI/CD"],
  },
];

export default function Projects() {
  return (
    <section id="projects" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">
            Work
          </p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Projects</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            A selection of projects built across academic, personal, and open-source contexts.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {projects.map((project, i) => (
            <div
              key={i}
              className="group flex flex-col rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 p-6 hover:shadow-md dark:hover:shadow-black/20 transition-all hover:-translate-y-0.5"
            >
              <h3 className="font-semibold text-gray-900 dark:text-white mb-2">{project.title}</h3>
              <p className="text-sm text-gray-500 dark:text-gray-400 mb-4 leading-relaxed flex-1">
                {project.description}
              </p>
              <div className="flex flex-wrap gap-1.5 mb-4">
                {project.tags.map((tag) => (
                  <span
                    key={tag}
                    className="text-xs px-2 py-0.5 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-400"
                  >
                    {tag}
                  </span>
                ))}
              </div>
              <div className="flex gap-4 pt-4 border-t border-gray-100 dark:border-gray-800">
                <button className="flex items-center gap-1 text-xs text-blue-600 dark:text-blue-400 hover:underline">
                  GitHub <ArrowUpRight className="w-3 h-3" />
                </button>
                <button className="flex items-center gap-1 text-xs text-gray-400 dark:text-gray-500 hover:underline">
                  Live Demo <ArrowUpRight className="w-3 h-3" />
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
