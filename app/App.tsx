import Navigation from "./components/Navigation";
import Hero from "./components/Hero";
import CodeMatrix from "./components/CodeMatrix";
import GitHubHeatmap from "./components/GitHubHeatmap";
import Achievements from "./components/Achievements";
import Projects from "./components/Projects";
import LearningJourney from "./components/LearningJourney";
import Blog from "./components/Blog";
import Testimonials from "./components/Testimonials";
import Contact from "./components/Contact";
import Footer from "./components/Footer";

export default function App() {
  return (
    <div className="min-h-screen bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100 overflow-x-hidden">
      <Navigation />
      <main>
        <Hero />
        <CodeMatrix />
        <GitHubHeatmap />
        <Achievements />
        <Projects />
        <LearningJourney />
        <Blog />
        <Testimonials />
        <Contact />
      </main>
      <Footer />
    </div>
  );
}
