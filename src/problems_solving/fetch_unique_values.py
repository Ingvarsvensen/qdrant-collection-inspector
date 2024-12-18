import json
from qdrant_client import QdrantClient

from src.config.settings import QDRANT_URL, QDRANT_API_KEY


# Fetch metadata values for a specific field from the first 100 points in the collection.
def fetch_metadata_values(collection_name, field_name):
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
    print(f"Connected to Qdrant.")

    # Scroll through the first 100 points
    response = client.scroll(
        collection_name=collection_name,
        limit=100,
        with_payload=True
    )
    points, _ = response

    # Extract values for the specified metadata field
    values = {point.payload.get(field_name) for point in points if field_name in point.payload}
    return values


if __name__ == "__main__":
    collection_name = "test_sharded_collection_3"
    field_name = "category"

    # Fetch and display unique metadata values
    values = fetch_metadata_values(collection_name, field_name)
    print(f"Unique values for '{field_name}': {values}")
