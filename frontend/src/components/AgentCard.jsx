export default function AgentCard({ title, desc }) {
  return (
    <div className="agent-card">
      <h3>{title}</h3>
      <p>{desc}</p>
    </div>
  );
}
