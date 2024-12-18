from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
from src.config.settings import QDRANT_URL, QDRANT_API_KEY


def add_test_points(collection_name):
    try:
        # Initialize Qdrant client
        client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
        print("Connected to Qdrant.\n")

        # Define test points
        points = [
            PointStruct(id=0, vector=[0.7] * 128, payload={"category": "A", "source": "file0.pdf"}),
            PointStruct(id=1, vector=[0.1] * 128, payload={"category": "A", "source": "file1.pdf"}),
            PointStruct(id=2, vector=[0.2] * 128, payload={"category": "B", "source": "file2.pdf"}),
            PointStruct(id=3, vector=[0.3] * 128, payload={"category": "A", "source": "file3.pdf"})
        ]

        # Add points to the collection
        client.upsert(collection_name=collection_name, points=points)
        print(f"Added {len(points)} points to collection '{collection_name}'.")

    except Exception as e:
        print(f"Error while adding points: {e}")


if __name__ == "__main__":
    collection_name = "test_sharded_collection_3"
    add_test_points(collection_name)