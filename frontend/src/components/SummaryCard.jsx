export default function SummaryCard({ summary }) {
  return (
    <div className="card">
      <h2>📌 Health Summary</h2>
      <p>{summary || "Loading AI summary..."}</p>
    </div>
  );
}
