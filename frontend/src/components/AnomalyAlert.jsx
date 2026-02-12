export default function AnomalyAlert({ anomalies }) {
  return (
    <div className="card">
      <h2>🚨 Anomalies</h2>
      {anomalies.length > 0 ? (
        <ul>
          {anomalies.map((a, i) => (
            <li key={i}>{a}</li>
          ))}
        </ul>
      ) : (
        <p>No major anomalies detected</p>
      )}
    </div>
  );
}
