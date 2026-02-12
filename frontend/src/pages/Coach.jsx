import { useState } from "react";
import {
  fetchNutrition,
  fetchExercise,
  fetchSleep,
  fetchGoals,
  fetchDoctor
} from "../api/healthApi";

export default function Coach() {
  const [response, setResponse] = useState("");

  const handle = async (fn) => {
    setResponse("Thinking...");
    const res = await fn();
    setResponse(res.response);
  };

  return (
    <div style={styles.container}>
      <h1>🤖 AI Health Coach</h1>

      <div style={styles.buttonGrid}>
        <button onClick={() => handle(fetchNutrition)}>🥗 Nutrition Agent</button>
        <button onClick={() => handle(fetchExercise)}>🏃 Exercise Agent</button>
        <button onClick={() => handle(fetchSleep)}>😴 Sleep Agent</button>
        <button onClick={() => handle(fetchGoals)}>🎯 Goals Agent</button>
        <button onClick={() => handle(fetchDoctor)}>🩺 Doctor Prep</button>
      </div>

      <div style={styles.responseCard}>
        <h3>🧠 AI Recommendation</h3>
        <pre style={styles.pre}>{response}</pre>
      </div>
    </div>
  );
}

const styles = {
  container: {
    padding: "24px",
    minHeight: "100vh",
    background: "#0f172a",
    color: "#e5e7eb"
  },
  buttonGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))",
    gap: "12px",
    marginBottom: "20px"
  },
  responseCard: {
    background: "#111827",
    padding: "20px",
    borderRadius: "12px",
    marginTop: "10px"
  },
  pre: {
    whiteSpace: "pre-wrap",
    fontSize: "14px"
  }
};
