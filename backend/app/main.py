from fastapi import FastAPI, WebSocket
from pymongo import MongoClient
from app.websocket_manager import ws_manager
from app.ml_pipeline import process_message

app = FastAPI()

client = MongoClient("mongodb://mongo:27017")
db = client["conversation_graph"]

@app.post("/ingest/")
async def ingest_message(conversation_id: str, speaker: str, text: str, timestamp: str):
    message = {
        "conversation_id": conversation_id,
        "speaker": speaker,
        "text": text,
        "timestamp": timestamp
    }
    db.messages.insert_one(message)

    node, edges = process_message(message)
    db.graph_nodes.insert_one(node)
    if edges:
        db.graph_edges.insert_many(edges)

    await ws_manager.broadcast({"event": "new_message", "node": node, "edges": edges})
    return {"status": "ok"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        ws_manager.disconnect(websocket)
