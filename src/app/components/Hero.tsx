import { motion } from "motion/react";
import { ArrowRight, Github, Linkedin, ExternalLink } from "lucide-react";

export default function Hero() {
  return (
    <section id="hero" className="min-h-screen flex items-center bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 py-32">
        <div className="flex flex-col md:flex-row items-center gap-12">
          <motion.div
            initial={{ opacity: 0, y: 24 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.55, ease: "easeOut" }}
            className="flex-1 max-w-2xl"
          >
            <span className="inline-block text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-6">
              Computer Science Student
            </span>
            <h1 className="text-5xl sm:text-7xl font-bold text-gray-900 dark:text-white mb-6 leading-tight" style={{ fontFamily: "Poppins, sans-serif" }}>
              C Rythan
            </h1>
            <p className="text-lg text-gray-500 dark:text-gray-400 mb-8 leading-relaxed max-w-lg">
              B.Tech CSE student at Amrita School of Computing, Chennai. Passionate about LLMs, NLP, and building things that matter.
            </p>
            <div className="flex flex-col sm:flex-row gap-3 mb-8">
              <button
                onClick={() => document.getElementById("projects")?.scrollIntoView({ behavior: "smooth" })}
                className="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-lg bg-blue-600 text-white hover:bg-blue-700 transition-colors text-sm font-medium"
              >
                View Projects <ArrowRight className="w-4 h-4" />
              </button>
              <button
                onClick={() => document.getElementById("contact")?.scrollIntoView({ behavior: "smooth" })}
                className="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-lg border border-gray-300 dark:border-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-900 transition-colors text-sm font-medium"
              >
                Get In Touch
              </button>
            </div>
            <div className="flex items-center gap-4">
              <a href="https://github.com/RYTH-07" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">
                <Github className="w-4 h-4" /> GitHub
              </a>
              <a href="https://codolio.com/profile/C%20RYTHAN" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">
                <ExternalLink className="w-4 h-4" /> Codolio
              </a>
              <a href="https://www.linkedin.com/in/ryth07" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">
                <Linkedin className="w-4 h-4" /> LinkedIn
              </a>
            </div>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.55, ease: "easeOut", delay: 0.2 }}
            className="flex-shrink-0"
          >
            <div className="w-56 h-56 sm:w-72 sm:h-72 rounded-2xl overflow-hidden border-4 border-blue-100 dark:border-blue-900 shadow-xl">
              <img src="/Profile.jpeg" alt="C Rythan" className="w-full h-full object-cover" />
            </div>
          </motion.div>
        </div>
        <div className="mt-16 pt-8 border-t border-gray-100 dark:border-gray-800 flex flex-wrap gap-8">
          <div>
            <p className="text-2xl font-semibold text-gray-900 dark:text-white">1</p>
            <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Projects</p>
          </div>
          <div>
            <p className="text-2xl font-semibold text-gray-900 dark:text-white">12</p>
            <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Problems Solved</p>
          </div>
          <div>
            <p className="text-2xl font-semibold text-gray-900 dark:text-white">8.22</p>
            <p className="text-xs text-gray-400 dark:text-gray-500 mt-0.5">Sem 1 SGPA</p>
          </div>
        </div>
      </div>
    </section>
  );
}