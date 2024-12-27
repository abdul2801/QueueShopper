import React, { useState, useEffect } from "react";
import Analytics from "./Analytics";

const socket = new WebSocket("ws://localhost:8000/ws");

function App() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    socket.onmessage = (event) => {
      const newEvent = JSON.parse(event.data);
      setEvents((prev) => [newEvent, ...prev]);
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-4xl mx-auto bg-white shadow-lg rounded-lg p-8">
        <h1 className="text-3xl font-bold text-center mb-6">📡 Real-Time Analytics Dashboard</h1>

        <div className="space-y-4">
          {events.length === 0 ? (
            <p className="text-center text-gray-500">No events received yet...</p>
          ) : (
            events.map((e, index) => (
              <div
                key={index}
                className="p-4 bg-gray-50 border border-gray-200 rounded-lg shadow-sm"
              >
                <h3 className="text-lg font-semibold text-blue-600">
                  {e.topic.toUpperCase()}
                </h3>
                <pre className="text-sm text-gray-700 mt-2">
                  {JSON.stringify(e.data, null, 2)}
                </pre>
              </div>
            ))
          )}
        </div>

        <Analytics events={events} />
      </div>
    </div>
  );
}

export default App;
