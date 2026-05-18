from ai.embeddings import create_embedding
from ai.vector_store import collection

def load_documents():

    files = [
        "data/products.txt",
        "data/policies.txt"
    ]

    document_id = 1

    for file_path in files:

        with open(file_path, "r") as file:

            content = file.read()

            chunks = content.split("\n\n")

            for chunk in chunks:

                embedding = create_embedding(
                    chunk
                )

                collection.add(
                    ids=[str(document_id)],
                    documents=[chunk],
                    embeddings=[embedding]
                )

                document_id += 1

    print("Documents loaded successfully")