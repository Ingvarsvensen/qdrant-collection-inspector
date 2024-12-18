from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance
from src.config.settings import QDRANT_URL, QDRANT_API_KEY

# def create_collection_with_shards(collection_name, shard_count):
#     try:
#         # Initialize Qdrant client
#         client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
#         print(f"Connected to Qdrant.")
#
#         # Check if the collection already exists
#         if collection_name in [c.name for c in client.get_collections().collections]:
#             print(f"Collection '{collection_name}' already exists. Skipping creation.")
#             return
#
#         # Create collection with specified shard count
#         client.create_collection(
#             collection_name=collection_name,
#             vectors_config=VectorParams(size=4, distance=Distance.COSINE),
#             shard_number=shard_count
#         )
#         print(f"Collection '{collection_name}' created with {shard_count} shards.")
#
#     except Exception as e:
#         print(f"Error: {e}")
#
#
# if __name__ == "__main__":
#     create_collection_with_shards("test_sharded_collection_2", 5)

#############################################################################################################

# --- Creating collection with parameters---
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

from src.config.settings import QDRANT_URL, QDRANT_API_KEY


# Create a Qdrant collection with custom settings
def create_custom_collection(collection_name, shard_count, vector_size=128):
    try:
        # Initialize Qdrant client
        client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
        print(f"Connected to Qdrant.")

        # Check if collection already exists
        existing_collections = [col.name for col in client.get_collections().collections]
        if collection_name in existing_collections:
            print(f"Collection '{collection_name}' already exists. Skipping creation.")
            return

        # Create the collection
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
            shard_number=shard_count
        )
        print(f"Collection '{collection_name}' created with {shard_count} shards.")

    except Exception as e:
        print(f"Error while creating collection: {e}")


if __name__ == "__main__":
    create_custom_collection("test_sharded_collection_3", shard_count=5)




