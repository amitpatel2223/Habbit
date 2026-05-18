from ai.vector_store import collection
from ai.data_loader import load_documents

def initialize_vector_db():

    existing_data = collection.get()

    if not existing_data["ids"]:

        print("Loading initial documents...")

        load_documents()

        print("Documents loaded.")

    else:

        print("ChromaDB already contains data.")