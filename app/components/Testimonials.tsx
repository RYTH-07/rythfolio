const testimonials = [
  {
    quote:
      "Placeholder — an endorsement or testimonial quote from a professor or academic mentor. Replace with actual feedback about your work, skills, or character.",
    name: "Prof. Placeholder",
    role: "Department of Computer Science",
    initials: "PP",
  },
  {
    quote:
      "Placeholder — an endorsement from a hackathon teammate or project collaborator. Replace with actual feedback about your collaboration and technical contributions.",
    name: "Team Member",
    role: "Hackathon Collaborator",
    initials: "TM",
  },
  {
    quote:
      "Placeholder — an endorsement from an industry mentor or internship supervisor. Replace with actual feedback about your professional growth and impact.",
    name: "Industry Mentor",
    role: "Senior Software Engineer",
    initials: "IM",
  },
];

export default function Testimonials() {
  return (
    <section id="testimonials" className="py-20 bg-gray-50 dark:bg-gray-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">
            Social Proof
          </p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Testimonials</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            What professors, peers, and mentors have to say.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
          {testimonials.map((item, i) => (
            <div
              key={i}
              className="flex flex-col rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950 p-6"
            >
              <p className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed italic flex-1 mb-6">
                "{item.quote}"
              </p>
              <div className="flex items-center gap-3 pt-4 border-t border-gray-100 dark:border-gray-800">
                <div className="w-8 h-8 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center text-xs font-medium text-gray-500 dark:text-gray-400 flex-shrink-0">
                  {item.initials}
                </div>
                <div>
                  <p className="text-sm font-medium text-gray-900 dark:text-white">{item.name}</p>
                  <p className="text-xs text-gray-400 dark:text-gray-500">{item.role}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
