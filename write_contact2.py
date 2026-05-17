code = '''import { useState, useRef } from "react";
import emailjs from "@emailjs/browser";
import { Github, Linkedin, Mail, Instagram, Send, CheckCircle, XCircle } from "lucide-react";
import { motion } from "motion/react";

const socials = [
  { icon: Github, label: "GitHub", handle: "@RYTH-07", href: "https://github.com/RYTH-07" },
  { icon: Linkedin, label: "LinkedIn", handle: "linkedin.com/in/ryth07", href: "https://www.linkedin.com/in/ryth07" },
  { icon: Instagram, label: "Instagram", handle: "@RYTH_25", href: "https://www.instagram.com/RYTH_25" },
  { icon: Mail, label: "Email", handle: "rythcomputes@gmail.com", href: "mailto:rythcomputes@gmail.com" },
];

const roles = ["Student", "Recruiter", "Developer", "Collaborator", "Just saying hi!"];

export default function Contact() {
  const formRef = useRef<HTMLFormElement>(null);
  const [form, setForm] = useState({ from_name: "", from_email: "", role: "", subject: "", message: "" });
  const [status, setStatus] = useState<"idle" | "loading" | "success" | "error">("idle");
  const [charCount, setCharCount] = useState(0);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setForm(prev => ({ ...prev, [name]: value }));
    if (name === "message") setCharCount(value.length);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!form.from_name || !form.from_email || !form.message) return;
    setStatus("loading");
    try {
      await emailjs.send(
        import.meta.env.VITE_EMAILJS_SERVICE_ID,
        import.meta.env.VITE_EMAILJS_TEMPLATE_ID,
        { ...form },
        import.meta.env.VITE_EMAILJS_PUBLIC_KEY
      );
      setStatus("success");
      setForm({ from_name: "", from_email: "", role: "", subject: "", message: "" });
      setCharCount(0);
      setTimeout(() => setStatus("idle"), 4000);
    } catch {
      setStatus("error");
      setTimeout(() => setStatus("idle"), 4000);
    }
  };

  const inputClass = "w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white placeholder-gray-400 dark:placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-sm";

  return (
    <section id="contact" className="py-20 bg-gray-50 dark:bg-gray-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Get In Touch</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Contact</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">Open to internships, collaborations, and interesting conversations.</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-10">
          <motion.div initial={{ opacity: 0, x: -20 }} whileInView={{ opacity: 1, x: 0 }} viewport={{ once: true }} transition={{ duration: 0.5 }}>
            <div className="bg-white dark:bg-gray-950 rounded-2xl border border-gray-200 dark:border-gray-800 p-6">
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-1">Send a Message</h3>
              <p className="text-sm text-gray-400 dark:text-gray-500 mb-6">Usually replies within 24 hours.</p>

              <form ref={formRef} onSubmit={handleSubmit} className="space-y-4">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-xs font-medium text-gray-700 dark:text-gray-300 mb-1.5">Name *</label>
                    <input name="from_name" value={form.from_name} onChange={handleChange} placeholder="John Doe" required className={inputClass} />
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-gray-700 dark:text-gray-300 mb-1.5">Email *</label>
                    <input name="from_email" type="email" value={form.from_email} onChange={handleChange} placeholder="john@example.com" required className={inputClass} />
                  </div>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-xs font-medium text-gray-700 dark:text-gray-300 mb-1.5">Role</label>
                    <select name="role" value={form.role} onChange={handleChange} className={inputClass}>
                      <option value="">Who are you?</option>
                      {roles.map(r => <option key={r} value={r}>{r}</option>)}
                    </select>
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-gray-700 dark:text-gray-300 mb-1.5">Subject</label>
                    <input name="subject" value={form.subject} onChange={handleChange} placeholder="Project Inquiry" className={inputClass} />
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-medium text-gray-700 dark:text-gray-300 mb-1.5">Message *</label>
                  <textarea name="message" value={form.message} onChange={handleChange} placeholder="Hey! Let us build something cool together..." required rows={5} maxLength={1000} className={inputClass + " resize-none"} />
                  <p className="text-xs text-gray-400 dark:text-gray-500 text-right mt-1">{charCount}/1000</p>
                </div>

                <button type="submit" disabled={status === "loading"} className="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-60 disabled:cursor-not-allowed transition-all text-sm font-medium shadow-lg shadow-blue-500/20">
                  {status === "loading" ? (
                    <><div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" /> Sending...</>
                  ) : (
                    <><Send className="w-4 h-4" /> Send Message</>
                  )}
                </button>

                {status === "success" && (
                  <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="flex items-center gap-2 text-green-600 dark:text-green-400 text-sm font-medium">
                    <CheckCircle className="w-4 h-4" /> Message sent! I will get back to you soon.
                  </motion.div>
                )}
                {status === "error" && (
                  <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="flex items-center gap-2 text-red-500 text-sm font-medium">
                    <XCircle className="w-4 h-4" /> Something went wrong. Try emailing me directly.
                  </motion.div>
                )}
              </form>
            </div>
          </motion.div>

          <motion.div initial={{ opacity: 0, x: 20 }} whileInView={{ opacity: 1, x: 0 }} viewport={{ once: true }} transition={{ duration: 0.5 }} className="flex flex-col gap-4">
            <div className="bg-white dark:bg-gray-950 rounded-2xl border border-gray-200 dark:border-gray-800 p-6">
              <h3 className="text-base font-semibold text-gray-900 dark:text-white mb-1">Connect with me</h3>
              <p className="text-sm text-gray-400 dark:text-gray-500 mb-5">Find me on these platforms.</p>
              <div className="space-y-3">
                {socials.map((s) => (
                  <a key={s.label} href={s.href} target="_blank" rel="noopener noreferrer"
                    className="flex items-center gap-4 p-3.5 rounded-xl border border-gray-100 dark:border-gray-800 hover:border-blue-300 dark:hover:border-blue-700 hover:bg-blue-50/50 dark:hover:bg-blue-950/20 transition-all group">
                    <div className="p-2 rounded-lg bg-gray-100 dark:bg-gray-800 group-hover:bg-blue-100 dark:group-hover:bg-blue-900/30 transition-colors">
                      <s.icon className="w-4 h-4 text-gray-600 dark:text-gray-400 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors" />
                    </div>
                    <div>
                      <p className="text-sm font-medium text-gray-900 dark:text-white">{s.label}</p>
                      <p className="text-xs text-gray-400 dark:text-gray-500">{s.handle}</p>
                    </div>
                  </a>
                ))}
              </div>
            </div>

            <div className="bg-blue-600 rounded-2xl p-6 text-white">
              <h3 className="font-semibold mb-1">Open to Opportunities</h3>
              <p className="text-blue-100 text-sm leading-relaxed">Looking for internships and collaborations in ML, NLP, and web development. First year CSE student with real project experience.</p>
              <div className="flex items-center gap-2 mt-4">
                <div className="w-2 h-2 rounded-full bg-green-400 animate-pulse" />
                <span className="text-sm text-blue-100">Available from 2026</span>
              </div>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
'''

with open('src/app/components/Contact.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("Contact done!")
