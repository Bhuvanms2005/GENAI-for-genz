import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer
} from "recharts";

const data = [
  { day: "Mon", sleep: 6 },
  { day: "Tue", sleep: 7 },
  { day: "Wed", sleep: 5.5 },
  { day: "Thu", sleep: 7.5 },
  { day: "Fri", sleep: 6.8 },
  { day: "Sat", sleep: 8 },
  { day: "Sun", sleep: 7.2 },
];

export default function SleepChart() {
  return (
    <div className="card">
      <h3>😴 Sleep Trend (Last 7 Days)</h3>
      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="day" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="sleep" stroke="#4f46e5" strokeWidth={3} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
