content = '''import { Award } from "lucide-react";

export default function Certifications() {
  return (
    <section id="certifications" className="py-20 bg-gray-50 dark:bg-gray-900">
      <div className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="mb-12">
          <p className="text-xs font-semibold tracking-widest uppercase text-blue-600 dark:text-blue-400 mb-2">Credentials</p>
          <h2 className="text-3xl font-semibold text-gray-900 dark:text-white">Certifications</h2>
          <p className="mt-3 text-gray-500 dark:text-gray-400 max-w-lg">
            Professional certifications and verified credentials.
          </p>
        </div>
        <div className="flex flex-col items-center justify-center py-20 rounded-xl border border-dashed border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-950">
          <div className="p-4 rounded-full bg-gray-100 dark:bg-gray-800 mb-4">
            <Award className="w-8 h-8 text-gray-400 dark:text-gray-500" />
          </div>
          <p className="text-gray-500 dark:text-gray-400 font-medium mb-1">Certifications coming soon</p>
          <p className="text-sm text-gray-400 dark:text-gray-500">Currently working toward my first certification.</p>
        </div>
      </div>
    </section>
  );
}'''
with open('src/app/components/Certifications.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print('Certifications done!')
