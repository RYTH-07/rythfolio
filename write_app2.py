
code = '''import Navigation from "./components/Navigation";
import Hero from "./components/Hero";
import CodeMatrix from "./components/CodeMatrix";
import GitHubHeatmap from "./components/GitHubHeatmap";
import Achievements from "./components/Achievements";
import Certifications from "./components/Certifications";
import Projects from "./components/Projects";
import TechStack from "./components/TechStack";
import CurrentlyLearning from "./components/CurrentlyLearning";
import LearningJourney from "./components/LearningJourney";
import Contact from "./components/Contact";
import Footer from "./components/Footer";

export default function App() {
  return (
    <div className="min-h-screen bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100 overflow-x-hidden">
      <Navigation />
      <main>
        <Hero />
        <TechStack />
        <CodeMatrix />
        <GitHubHeatmap />
        <Projects />
        <Achievements />
        <Certifications />
        <LearningJourney />
        <CurrentlyLearning />
        <Contact />
      </main>
      <Footer />
    </div>
  );
}'''
with open('src/app/App.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print('App.tsx restored!')
