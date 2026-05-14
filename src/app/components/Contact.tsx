import { Github, Linkedin, Mail, Instagram } from "lucide-react";

export default function Contact() {
  const socials = [
    { icon: Github, label: "GitHub", handle: "@RYTH-07", href: "https://github.com/RYTH-07" },
    { icon: Linkedin, label: "LinkedIn", handle: "linkedin.com/in/ryth07", href: "https://www.linkedin.com/in/ryth07" },
    { icon: Instagram, label: "Instagram", handle: "@RYTH_25", href: "https://www.instagram.com/RYTH_25" },
    { icon: Mail, label: "Email", handle: "rythcomputes@gmail.com", href: "mailto:rythcomputes@gmail.com" },
  ];

  return (
    <section id="contact" className="py-20 bg-gray-50 dark:bg-gray-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Get In Touch</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Contact</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            Open to internships, collaborations, and interesting conversations.
          </p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
          <div className="space-y-4">
            {socials.map((s) => (
              <a key={s.label} href={s.href} target="_blank" rel="noopener noreferrer"
                className="flex items-center gap-4 p-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 hover:border-blue-300 dark:hover:border-blue-700 transition-all">
                <div className="p-2.5 rounded-lg bg-gray-100 dark:bg-gray-800">
                  <s.icon className="w-4 h-4 text-gray-600 dark:text-gray-400" />
                </div>
                <div>
                  <p className="text-sm font-medium text-gray-900 dark:text-white">{s.label}</p>
                  <p className="text-xs text-gray-400 dark:text-gray-500">{s.handle}</p>
                </div>
              </a>
            ))}
          </div>
          <div className="flex flex-col justify-center">
            <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-3">Drop me a message</h3>
            <p className="text-gray-500 dark:text-gray-400 text-sm mb-6">
              Best way to reach me is via email or LinkedIn. I usually respond within 24 hours.
            </p>
            <a href="mailto:rythcomputes@gmail.com"
              className="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-lg bg-blue-600 text-white hover:bg-blue-700 transition-colors text-sm font-medium w-fit">
              <Mail className="w-4 h-4" /> Send Email
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}