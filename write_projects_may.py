code = '''import { ExternalLink, Github } from "lucide-react";
import { motion } from "motion/react";

export default function Projects() {
  const projects = [
    {
      title: "MAY — Personal AI Assistant",
      description: "Personal AI assistant powered by Claude Sonnet 4.5. Features real-time web search, Google Calendar, Gmail and Tasks integration, persistent memory via Supabase + pgvector semantic search, React Native mobile app with Chat, Dashboard and Memory screens, and voice TTS responses. Deployed on Render.",
      tags: ["Claude Sonnet", "React Native", "Supabase", "pgvector", "Google APIs", "TTS", "Render"],
      github: "https://github.com/RYTH-07/MAY",
      demo: null,
      featured: true,
      badge: "AI Project",
      badgeColor: "bg-purple-50 dark:bg-purple-950 text-purple-600 dark:text-purple-400",
    },
    {
      title: "Rythfolio",
      description: "Personal developer portfolio built with React, Vite, and Tailwind CSS v4. Features live GitHub contribution heatmap, dynamic LeetCode stats, 3D skills globe, Supabase guestbook, EmailJS contact form, particle canvas animation, and dark/light mode. Deployed on Vercel with auto CI/CD.",
      tags: ["React", "TypeScript", "Tailwind CSS", "Vite", "Vercel", "Supabase"],
      github: "https://github.com/RYTH-07/rythfolio",
      demo: "https://rythfolio.vercel.app/",
      featured: true,
      badge: "Featured",
      badgeColor: "bg-blue-50 dark:bg-blue-950 text-blue-600 dark:text-blue-400",
    },
    {
      title: "Neural Lens",
      description: "An interactive, zero-framework SPA field guide for NLP and LLM concepts. Features real-time tokenization demos, self-attention visualizations, and a scored quiz. Built for CSE students with no build step required.",
      tags: ["HTML", "CSS", "JavaScript", "NLP", "LLM"],
      github: "https://github.com/RYTH-07/neural-lens",
      demo: "https://ryth-07.github.io/neural-lens/",
      featured: false,
      badge: null,
      badgeColor: "",
    },
  ];

  return (
    <section id="projects" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Work</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Projects</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            Projects built across academic and personal contexts. More coming soon.
          </p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {projects.map((project, i) => (
            <motion.div
              key={project.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.1, duration: 0.4 }}
              whileHover={{ y: -4, transition: { duration: 0.2 } }}
              className={"rounded-xl border bg-white dark:bg-gray-950 p-6 flex flex-col transition-shadow hover:shadow-lg hover:shadow-blue-500/10 " +
                (project.featured
                  ? "border-blue-200 dark:border-blue-800"
                  : "border-gray-200 dark:border-gray-800"
                )}
            >
              {project.badge && (
                <span className={"self-start text-xs font-semibold px-2.5 py-0.5 rounded-full mb-3 " + project.badgeColor}>
                  {project.badge}
                </span>
              )}
              <h3 className="font-semibold text-gray-900 dark:text-white mb-2">{project.title}</h3>
              <p className="text-sm text-gray-500 dark:text-gray-400 leading-relaxed flex-1 mb-4">{project.description}</p>
              <div className="flex flex-wrap gap-2 mb-4">
                {project.tags.map((tag) => (
                  <span key={tag} className="text-xs px-2.5 py-0.5 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-400">
                    {tag}
                  </span>
                ))}
              </div>
              <div className="flex items-center gap-4 pt-4 border-t border-gray-100 dark:border-gray-800">
                <a href={project.github} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1.5 text-sm text-blue-600 dark:text-blue-400 hover:underline font-medium">
                  <Github className="w-3.5 h-3.5" /> GitHub
                </a>
                {project.demo && (
                  <a href={project.demo} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1.5 text-sm text-blue-600 dark:text-blue-400 hover:underline font-medium">
                    <ExternalLink className="w-3.5 h-3.5" /> Live Demo
                  </a>
                )}
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
'''

with open('src/app/components/Projects.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("Projects updated with MAY!")
