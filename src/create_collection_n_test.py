from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance
from src.config.settings import QDRANT_URL, QDRANT_API_KEY


def create_collection_with_shards(collection_name, shard_count):
    try:
        # Initialize Qdrant client
        client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
        print(f"Connected to Qdrant.")

        # Check if the collection already exists
        if collection_name in [c.name for c in client.get_collections().collections]:
            print(f"Collection '{collection_name}' already exists. Skipping creation.")
            return

        # Create collection with specified shard count
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=4, distance=Distance.COSINE),
            shard_number=shard_count
        )
        print(f"Collection '{collection_name}' created with {shard_count} shards.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Create a new collection with 3 shards
    create_collection_with_shards("test_sharded_collection_2", 5)
  
################### All of the code below for the test purposes and understanding the structure
  
# import json
# from qdrant_client import QdrantClient
# from tabulate import tabulate
#
# from src.config.settings import QDRANT_URL, QDRANT_API_KEY
#
#
# def fetch_collections():
#     try:
#         # Initialize Qdrant client
#         client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
#         print("Successfully connected to Qdrant.\n")
#
#         # Fetch all collections
#         response = client.get_collections()
#         print("Full response from get_collections():")
#         print(json.dumps(response.model_dump(), indent=4))
#         print("######################################################################################")
#
#         # Print names of all collections
#         print("List of collection names:")
#         collections = response.collections
#         for collection in collections:
#             print(f"- {collection.name}")
#
#         print("######################################################################################")
#
#         # Fetch details of a specific collection
#         collection_name = "terraforming_plans"
#         print(f"Fetching details for collection: '{collection_name}'")
#         collection_response = client.get_collection(collection_name)
#         print(json.dumps(collection_response.model_dump(), indent=4))
#
#         print("#######################################################################################")
#
#         if not client or not collections:
#             print("No collections found or client initialization failed.")
#             return
#
#         # Prepare table data
#         table_data = []
#         for collection in collections:
#             collection_name = collection.name
#
#             # Fetch collection configuration to get shard_number and status
#             collection_info = client.get_collection(collection_name)
#             shard_number = collection_info.config.params.shard_number
#             collection_status = collection_info.status
#             optimizer_status = collection_info.optimizer_status
#             datatype = collection_info.config.params.vectors.datatype
#             table_data.append([collection_name, shard_number, collection_status, optimizer_status, datatype])
#
#         # Display table
#         print("\nCollection Shard and Status Table:")
#         print(
#             tabulate(table_data, headers=["Collection Name", "Shard Number", "Status", "Optimizer Status", "Data type"],
#                      tablefmt="grid"))
#
#
#     except Exception as e:
#         print(f"Error, something went wrong: {e}")
#
#
# if __name__ == "__main__":
#     fetch_collections()
