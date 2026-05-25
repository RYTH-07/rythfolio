import re

with open('src/app/components/Hero.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

old_h1 = '''            <motion.h1 initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.2, duration: 0.6 }} className="text-5xl sm:text-7xl font-bold text-gray-900 dark:text-white mb-6 leading-tight" style={{ fontFamily: "Poppins, sans-serif" }}>
              C Rythan
            </motion.h1>'''

new_h1 = '''            <motion.h1 initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.2, duration: 0.6 }} className="text-4xl sm:text-6xl font-bold text-gray-900 dark:text-white mb-6 leading-tight" style={{ fontFamily: "Poppins, sans-serif" }}>
              <span className="block text-2xl sm:text-3xl font-medium text-gray-500 dark:text-gray-400 mb-2">Hi, I am</span>
              <span className="inline-flex items-center gap-3">
                C Rythan
                <svg className="w-8 h-8 sm:w-10 sm:h-10 text-blue-500 flex-shrink-0" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </span>
            </motion.h1>'''

code = code.replace(old_h1, new_h1)

with open('src/app/components/Hero.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("Hero name updated!")
