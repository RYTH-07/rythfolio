import { useState } from "react";
import { Github, Linkedin, Twitter, Mail, Send } from "lucide-react";

const socials = [
  { icon: Github, label: "GitHub", href: "#", handle: "@c_rythan" },
  { icon: Linkedin, label: "LinkedIn", href: "#", handle: "linkedin.com/in/c-rythan" },
  { icon: Twitter, label: "Twitter / X", href: "#", handle: "@c_rythan" },
  { icon: Mail, label: "Email", href: "mailto:placeholder@email.com", handle: "placeholder@email.com" },
];

export default function Contact() {
  const [form, setForm] = useState({ name: "", email: "", message: "" });

  return (
    <section id="contact" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">
            Get In Touch
          </p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Contact</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            Open to internships, collaborations, and interesting conversations. Drop me a message or connect on social.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-5 gap-12">
          <div className="lg:col-span-3">
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">
                  Name
                </label>
                <input
                  type="text"
                  placeholder="Your full name"
                  value={form.name}
                  onChange={(e) => setForm({ ...form, name: e.target.value })}
                  className="w-full px-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-900 text-gray-900 dark:text-white placeholder-gray-400 dark:placeholder-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition text-sm"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">
                  Email
                </label>
                <input
                  type="email"
                  placeholder="your@email.com"
                  value={form.email}
                  onChange={(e) => setForm({ ...form, email: e.target.value })}
                  className="w-full px-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-900 text-gray-900 dark:text-white placeholder-gray-400 dark:placeholder-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition text-sm"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">
                  Message
                </label>
                <textarea
                  rows={5}
                  placeholder="What's on your mind?"
                  value={form.message}
                  onChange={(e) => setForm({ ...form, message: e.target.value })}
                  className="w-full px-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-900 text-gray-900 dark:text-white placeholder-gray-400 dark:placeholder-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition resize-none text-sm"
                />
              </div>

              <button
                type="button"
                className="inline-flex items-center gap-2 px-6 py-2.5 rounded-lg bg-blue-600 text-white hover:bg-blue-700 active:bg-blue-800 transition-colors text-sm font-medium"
              >
                Send Message
                <Send className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

          <div className="lg:col-span-2">
            <h3 className="text-sm font-semibold text-gray-900 dark:text-white mb-1">
              Connect with me
            </h3>
            <p className="text-sm text-gray-500 dark:text-gray-400 mb-5">
              Update these placeholders with your actual social handles.
            </p>

            <div className="space-y-3">
              {socials.map((social) => (
                <a
                  key={social.label}
                  href={social.href}
                  className="flex items-center gap-3 p-3.5 rounded-xl border border-gray-200 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-900 transition-colors group"
                >
                  <div className="w-8 h-8 rounded-lg bg-gray-100 dark:bg-gray-800 flex items-center justify-center flex-shrink-0">
                    <social.icon className="w-4 h-4 text-gray-500 dark:text-gray-400 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors" />
                  </div>
                  <div className="min-w-0">
                    <p className="text-xs font-medium text-gray-700 dark:text-gray-300">{social.label}</p>
                    <p className="text-xs text-gray-400 dark:text-gray-500 truncate">{social.handle}</p>
                  </div>
                </a>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
