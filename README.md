# ConversationGraph Prototype

## Prototype DEMO
![WhatsApp Image 2025-09-04 at 16 45 39_5fa13058](https://github.com/user-attachments/assets/a38165aa-3246-4e0e-82fa-48f323dc7e6a)


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

