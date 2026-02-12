import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Coach from "./pages/Coach";

export default function App() {
  return (
    <BrowserRouter>
      <nav style={styles.nav}>
        <NavLink to="/" style={styles.link}>
          Dashboard
        </NavLink>
        <NavLink to="/coach" style={styles.link}>
          AI Coach
        </NavLink>
      </nav>

      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/coach" element={<Coach />} />
      </Routes>
    </BrowserRouter>
  );
}

const styles = {
  nav: {
    padding: "12px 20px",
    background: "#020617",
    display: "flex",
    gap: "20px",
    borderBottom: "1px solid #1e293b"
  },
  link: {
    color: "#e5e7eb",
    textDecoration: "none",
    fontWeight: "500"
  }
};
