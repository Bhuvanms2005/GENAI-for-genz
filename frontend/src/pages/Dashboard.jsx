import { useEffect, useState } from "react";
import { fetchSummary, fetchAnomalies, fetchProgress } from "../api/healthApi";

import SummaryCard from "../components/SummaryCard";
import AnomalyAlert from "../components/AnomalyAlert";
import AgentCard from "../components/AgentCard";
import SleepChart from "../components/SleepChart";
import ProgressChart from "../components/ProgressChart";

import "../styles/dashboard.css";

export default function Dashboard() {
  const [summary, setSummary] = useState("");
  const [anomalies, setAnomalies] = useState([]);
  const [progress, setProgress] = useState(null);

  useEffect(() => {
    fetchSummary().then(data =>
      setSummary(data.compressed_health_summary)
    );

    fetchAnomalies().then(data =>
      setAnomalies(data.detected_anomalies || [])
    );

    fetchProgress().then(setProgress);
  }, []);

  return (
    <div className="dashboard">
        <div className="dashboard-container">
      <h1>🏥 Personal Health Coach</h1>

      {/* AI Summary */}
      <SummaryCard summary={summary} />

      {/* Anomaly Alerts */}
      <AnomalyAlert anomalies={anomalies} />

      {/* Agent Cards */}
      <div className="agent-grid">
        <AgentCard title="🥗 Nutrition Agent" desc="Personalized meal planning" />
        <AgentCard title="🏃 Exercise Agent" desc="Workout recommendations" />
        <AgentCard title="😴 Sleep Agent" desc="Sleep quality analysis" />
      </div>

      {/* Charts */}
      <div className="charts-grid">
        <SleepChart />
        <ProgressChart />
      </div>

      {/* Raw Progress (optional – can remove later) */}
      {progress && (
        <pre className="raw-json">
          {JSON.stringify(progress.progress_summary, null, 2)}
        </pre>
      )}
    </div>
    </div>
  );
}
