# ConversationGraph MVP

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
