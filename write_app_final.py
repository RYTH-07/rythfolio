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
import SideNav from "./components/SideNav";
import ScrollToTop from "./components/ScrollToTop";
import ProgressBar from "./components/ProgressBar";
import MobileBottomNav from "./components/MobileBottomNav";

export default function App() {
  return (
    <div className="min-h-screen bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100 overflow-x-hidden">
      <ProgressBar />
      <Navigation />
      <SideNav />
      <main className="pb-16 lg:pb-0">
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
      <ScrollToTop />
      <MobileBottomNav />
    </div>
  );
}
'''

with open('src/app/App.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("App.tsx done!")
