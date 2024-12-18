from qdrant_client import QdrantClient
from src.config.settings import QDRANT_URL, QDRANT_API_KEY


def delete_collection(collection_name):
    try:
        # Initialize Qdrant client
        client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
        print(f"Connected to Qdrant.\n")

        # Delete the collection
        client.delete_collection(collection_name=collection_name)
        print(f"Collection '{collection_name}' deleted successfully.")

    except Exception as e:
        print(f"Error while deleting collection: {e}")


if __name__ == "__main__":
    collection_name = "test_sharded_collection_3"
    delete_collection(collection_name)
