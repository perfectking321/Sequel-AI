import React from "react";
import CytoscapeComponent from "react-cytoscapejs";

interface GraphProps {
  graph: { nodes: any[]; edges: any[] };
}

function GraphView({ graph }: GraphProps) {
  const elements = [
    ...graph.nodes.map((n) => ({ data: { id: n.id, label: n.text } })),
    ...graph.edges.map((e) => ({
      data: { source: e.source, target: e.target, weight: e.weight }
    }))
  ];

  return (
    <CytoscapeComponent
      elements={elements}
      style={{ width: "100%", height: "100%" }}
      layout={{ name: "cose" }}
    />
  );
}

export default GraphView;
