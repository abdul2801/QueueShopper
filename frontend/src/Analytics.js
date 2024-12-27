import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

const Analytics = ({ events }) => {
  const processedData = events
    .filter((e) => e.topic === "order_placed")
    .map((e, index) => ({
      name: `Order ${index + 1}`,
      amount: e.data.amount,
    }));

  return (
    <div className="mt-8">
      <h2 className="text-2xl font-bold mb-4 text-blue-600">📊 Order Analytics</h2>

      {processedData.length === 0 ? (
        <p className="text-gray-500">No order data available...</p>
      ) : (
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={processedData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="amount" stroke="#8884d8" />
          </LineChart>
        </ResponsiveContainer>
      )}
    </div>
  );
};

export default Analytics;
