# qdrant-collection-inspector

##A simple Python script to connect to a Qdrant instance, fetch all collections, and display their shard IDs in a user-friendly table format.

## Features

- Connects to a Qdrant instance using the Qdrant Python client.
- Fetches all collections available in the instance.
- Displays shard information for each collection:
  - **Combined shard IDs** in one row.
- Clean, readable output using `tabulate`.

## Prerequisites

- Python 3.8+ (3.12 is better)
- Qdrant client library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/qdrant-shard-inspector.git
   cd qdrant-shard-inspector

2. Install dependencies
   ```bash
   pip install -r requirements.txt

3. Configure Qdrant connection in src/config/settings.py:
   ```bash
   QDRANT_URL = "your-qdrant-url"
   QDRANT_API_KEY = "your-api-key"

