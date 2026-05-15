
code = '''import { ExternalLink } from "lucide-react";

export default function Certifications() {
  const certs = [
    {
      title: "Complete 2026 Python Bootcamp: Learn Python from Scratch",
      issuer: "Udemy — Code With Harry",
      year: "2026",
      skills: ["Python", "Flask", "API Integration", "Web Development"],
      image: "/python-cert.jpg",
      linkedin: "https://www.linkedin.com/in/ryth07",
    },
  ];

  return (
    <section id="certifications" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Credentials</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Certifications</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">Verified credentials and completed courses.</p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
          {certs.map((cert) => (
            <div key={cert.title} className="rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 overflow-hidden hover:shadow-md transition-shadow">
              <div className="h-48 overflow-hidden bg-gray-100 dark:bg-gray-800 cursor-pointer" onClick={() => window.open(cert.image, "_blank")}>
                <img src={cert.image} alt={cert.title} className="w-full h-full object-cover hover:scale-105 transition-transform duration-300" />
              </div>
              <div className="p-5">
                <h3 className="font-semibold text-gray-900 dark:text-white mb-1 leading-snug">{cert.title}</h3>
                <p className="text-xs text-gray-400 dark:text-gray-500 mb-3">{cert.issuer} · {cert.year}</p>
                <div className="flex flex-wrap gap-2 mb-4">
                  {cert.skills.map((s) => (
                    <span key={s} className="text-xs px-2.5 py-0.5 rounded-full bg-blue-50 dark:bg-blue-950 text-blue-700 dark:text-blue-300">{s}</span>
                  ))}
                </div>
                <a href={cert.linkedin} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1.5 text-xs text-blue-600 dark:text-blue-400 hover:underline font-medium">
                  <ExternalLink className="w-3 h-3" /> View on LinkedIn
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}'''
with open('src/app/components/Certifications.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('Certifications done!')
