from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN
import numpy as np
import uuid

model = SentenceTransformer("all-MiniLM-L6-v2")
conversation_embeddings = []

def process_message(message):
    text = message["text"]
    embedding = model.encode([text])[0]
    
    node_id = str(uuid.uuid4())
    node = {
        "id": node_id,
        "text": text,
        "speaker": message["speaker"],
        "conversation_id": message["conversation_id"],
        "embedding": embedding.tolist()
    }
    conversation_embeddings.append(embedding)

    edges = []
    if len(conversation_embeddings) > 1:
        sim = np.dot(conversation_embeddings[-2], embedding) / (
            np.linalg.norm(conversation_embeddings[-2]) * np.linalg.norm(embedding)
        )
        edges.append({"source": node_id, "target": node_id, "weight": sim})

    return node, edges
