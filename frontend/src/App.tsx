import React, { useEffect, useState } from "react";
import GraphView from "./GraphView";
import { connectWebSocket } from "./websocket";

function App() {
  const [graph, setGraph] = useState({ nodes: [], edges: [] });

  useEffect(() => {
    const ws = connectWebSocket((msg: any) => {
      if (msg.event === "new_message") {
        setGraph((prev) => ({
          nodes: [...prev.nodes, msg.node],
          edges: [...prev.edges, ...msg.edges]
        }));
      }
    });
    return () => ws.close();
  }, []);

  return (
    <div className="h-screen w-screen">
      <GraphView graph={graph} />
    </div>
  );
}

export default App;
