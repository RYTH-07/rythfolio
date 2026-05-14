import { ArrowUpRight } from "lucide-react";

const posts = [
  {
    tag: "Algorithms",
    title: "Understanding Time Complexity in Practice",
    excerpt: "Placeholder — a short insight into algorithm analysis and how Big-O notation applies to real-world code. Replace with your actual article.",
    date: "Jan 2024",
    readTime: "5 min",
  },
  {
    tag: "Craft",
    title: "Why Clean Code Matters More Than You Think",
    excerpt: "Placeholder — thoughts on readability, maintainability, and writing code for humans, not machines. Replace with your actual article.",
    date: "Dec 2023",
    readTime: "4 min",
  },
  {
    tag: "Systems",
    title: "Getting Started with Systems Programming",
    excerpt: "Placeholder — a beginner's guide to writing closer-to-hardware code and the mental models it requires. Replace with your actual article.",
    date: "Nov 2023",
    readTime: "7 min",
  },
];

export default function Blog() {
  return (
    <section id="blog" className="py-20 bg-white dark:bg-gray-950">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">
            Writing
          </p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Blog & Insights</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            Short articles and notes on software engineering, algorithms, and the craft of coding.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
          {posts.map((post, i) => (
            <article
              key={i}
              className="group flex flex-col rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 p-6 hover:shadow-md dark:hover:shadow-black/20 transition-all cursor-pointer"
            >
              <span className="inline-block text-xs font-medium px-2.5 py-0.5 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-500 dark:text-gray-400 mb-4 self-start">
                {post.tag}
              </span>
              <h3 className="font-semibold text-gray-900 dark:text-white mb-2 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors leading-snug flex-1">
                {post.title}
              </h3>
              <p className="text-sm text-gray-500 dark:text-gray-400 mb-5 leading-relaxed line-clamp-3">
                {post.excerpt}
              </p>
              <div className="flex items-center justify-between pt-4 border-t border-gray-100 dark:border-gray-800">
                <div className="flex items-center gap-2 text-xs text-gray-400 dark:text-gray-500">
                  <span>{post.date}</span>
                  <span>·</span>
                  <span>{post.readTime} read</span>
                </div>
                <ArrowUpRight className="w-3.5 h-3.5 text-gray-300 dark:text-gray-600 group-hover:text-blue-500 transition-colors" />
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}
