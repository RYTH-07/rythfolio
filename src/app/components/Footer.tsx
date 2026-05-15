import { Github, Linkedin, ExternalLink, Mail } from "lucide-react";

const links = [
  { icon: Github, label: "GitHub", href: "https://github.com/RYTH-07" },
  { icon: Linkedin, label: "LinkedIn", href: "https://www.linkedin.com/in/ryth07" },
  { icon: ExternalLink, label: "Codolio", href: "https://codolio.com/profile/C%20RYTHAN" },
  { icon: Mail, label: "Email", href: "mailto:rythcomputes@gmail.com" },
];

const navLinks = [
  { label: "About", href: "#hero" },
  { label: "Projects", href: "#projects" },
  
  { label: "Contact", href: "#contact" },
];

export default function Footer() {
  const scrollTo = (href: string) => {
    document.querySelector(href)?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <footer className="border-t border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 py-10">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-8">
          <div>
            <p className="text-base font-semibold text-gray-900 dark:text-white mb-1" style={{ fontFamily: "Poppins, sans-serif" }}>
              C Rythan
            </p>
            <p className="text-xs text-gray-400 dark:text-gray-500">Computer Science Student</p>
          </div>
          <div className="flex flex-wrap gap-x-6 gap-y-2">
            {navLinks.map((link) => (
              <button key={link.label} onClick={() => scrollTo(link.href)} className="text-sm text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">
                {link.label}
              </button>
            ))}
          </div>
          <div className="flex items-center gap-2">
            {links.map((link) => (
              <a key={link.label} href={link.href} target="_blank" rel="noopener noreferrer" aria-label={link.label} className="p-2 rounded-lg text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition-all">
                <link.icon className="w-4 h-4" />
              </a>
            ))}
          </div>
        </div>
        <div className="mt-8 pt-6 border-t border-gray-100 dark:border-gray-800">
          <p className="text-xs text-gray-400 dark:text-gray-500 text-center">
            © {new Date().getFullYear()} C Rythan. Built with React and Tailwind CSS.
          </p>
        </div>
      </div>
    </footer>
  );
}
