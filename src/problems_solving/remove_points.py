from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue
from src.config.settings import QDRANT_URL, QDRANT_API_KEY


# Delete points from a collection based on metadata filter
def delete_points_by_metadata(collection_name, key, value):
    try:
        # Initialize Qdrant client
        client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
        print(f"Connected to Qdrant.\n")

        # Define filter for deletion
        filter_condition = Filter(
            must=[
                FieldCondition(
                    key=key,
                    match=MatchValue(value=value)
                )
            ]
        )

        # Delete points using filter
        response = client.delete(
            collection_name=collection_name,
            points_selector=filter_condition
        )
        print(f"Points with '{key} = {value}' deleted from collection '{collection_name}'.")
        print(f"Delete response: {response}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    collection_name = "test_sharded_collection_3"
    delete_points_by_metadata(collection_name, "source", "file1.pdf")
