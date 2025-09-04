export function connectWebSocket(onMessage: (msg: any) => void) {
  const ws = new WebSocket("ws://localhost:8000/ws");

  ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    onMessage(msg);
  };

  return ws;
}
