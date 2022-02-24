import Sidebar from "./components/Sidebar";
import Dashboard from "./components/Dashboard";
import "./scss/style.scss";

function App() {
  return <div className="app">
    <Sidebar />
    <Dashboard />
  </div>;
}

export default App;
