from qdrant_client import QdrantClient
from tabulate import tabulate

from src.config.settings import QDRANT_URL, QDRANT_API_KEY


def fetch_and_print_shards():
    # Initialize Qdrant client
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
    print("Successfully connected to Qdrant.\n")

    # Fetch all collections
    collections_response = client.get_collections()
    collections = collections_response.collections

    if not collections:
        print("No collections found in Qdrant.")
        return

    # Prepare table data
    table_data = []
    for collection in collections:
        collection_name = collection.name
        # Get collection info to find shard_number
        collection_info = client.get_collection(collection_name)

        # Extract shard_number
        shard_number = collection_info.config.params.shard_number

        # Generate shard IDs and combine them in a single row
        shard_ids = [str(shard_id) for shard_id in range(shard_number)]
        table_data.append([collection_name, ", ".join(shard_ids)])


    # Display table
    if table_data:
        print(tabulate(table_data, headers=["Collection Name", "Shard IDs"], tablefmt="grid"))
    else:
        print("No shard information available.")
      

if __name__ == "__main__":
    fetch_and_print_shards()
