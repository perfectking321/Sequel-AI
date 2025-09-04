# ConversationGraph Prototype

## Prototype DEMO
<img src="https://github.com/user-attachments/assets/83e703f4-d51a-46f0-a88b-0b4a0bc0f9e6" alt="djsli" width="300">
<img src="https://github.com/user-attachments/assets/1afe7433-6e3d-4958-93e7-1fee5b8bb8d1" alt="WhatsApp Image 1" width="300">
<img src="https://github.com/user-attachments/assets/4fc00764-9a05-493c-bb6a-fe3491e92494" alt="WhatsApp Image 2" width="300">


## Quick Start

1. Clone this repo and go into folder:
   ```bash
   git clone <repo-url>
   cd conversationgraph
   ```

2. Start services:
   ```bash
   docker-compose up --build
   ```

3. Access frontend at [http://localhost:3000](http://localhost:3000)  
   Backend API at [http://localhost:8000](http://localhost:8000)

## Features
- Chat ingestion via FastAPI
- SBERT embeddings for semantic similarity
- MongoDB for storage
- Real-time WebSocket graph updates
- React + Cytoscape.js visualization

