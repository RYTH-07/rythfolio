with open('write_apptest.py', 'w', encoding='utf-8') as s:
    s.write("""
code = '''import Navigation from "./components/Navigation";
import Hero from "./components/Hero";
import Footer from "./components/Footer";

export default function App() {
  return (
    <div className="min-h-screen bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100 overflow-x-hidden">
      <Navigation />
      <main>
        <Hero />
      </main>
      <Footer />
    </div>
  );
}'''
with open('src/app/App.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('App test done!')
""")
