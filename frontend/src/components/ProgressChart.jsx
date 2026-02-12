import {
  BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer
} from "recharts";

const data = [
  { goal: "Sleep", progress: 80 },
  { goal: "Exercise", progress: 65 },
  { goal: "Nutrition", progress: 70 },
];

export default function ProgressChart() {
  return (
    <div className="card">
      <h3>🎯 Goal Progress</h3>
      <ResponsiveContainer width="100%" height={250}>
        <BarChart data={data}>
          <XAxis dataKey="goal" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="progress" fill="#22c55e" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
