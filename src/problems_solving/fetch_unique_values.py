import json
from qdrant_client import QdrantClient

from src.config.settings import QDRANT_URL, QDRANT_API_KEY


# def fetch_metadata():
#     try:
#         # Initialize Qdrant client
#         client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
#         print("Successfully connected to Qdrant.\n")
#
#         # Specify the collection
#         collection_name = "test_sharded_collection_3"
#
#         # Scroll through the collection to fetch points and their payload
#         response = client.scroll(
#             collection_name=collection_name,
#             limit=10,
#             with_payload=True
#         )
#         points, _ = response
#
#         # Print points with payload
#         print(f"Points in collection '{collection_name}':")
#         for point in points:
#             print(f"ID: {point.id}, Payload: {point.payload}")
#
#     except Exception as e:
#         print(f"Error, something went wrong: {e}")
#
#
# if __name__ == "__main__":
#     fetch_metadata()

#####################################################################################################

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
