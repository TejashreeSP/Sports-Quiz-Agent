import os
import json
import chromadb
from chromadb.utils import embedding_functions


def get_chroma_client():
    """
    Creates or connects to the local ChromaDB database.
    """
    return chromadb.PersistentClient(path="./chroma_db")


def setup_and_populate_db(json_file_path="./data/sports_facts.json"):
    """
    Reads sports facts from JSON and stores them in ChromaDB.
    """

    client = get_chroma_client()

    embedding_fn = embedding_functions.DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name="sports_history",
        embedding_function=embedding_fn
    )

    
    if collection.count() > 0:
        print(f"Database already contains {collection.count()} facts.")
        return collection

    if not os.path.exists(json_file_path):
        print("sports_facts.json not found.")
        return collection

    with open(json_file_path, "r", encoding="utf-8") as file:
        facts = json.load(file)

    documents = []
    metadatas = []
    ids = []

    for index, item in enumerate(facts):
        documents.append(item["fact"])
        metadatas.append({"sport": item["sport"]})
        ids.append(f"fact_{index}")

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print(f"{len(documents)} facts inserted successfully.")

    return collection


def query_historic_facts(sport, query_text, n_results=3):
    """
    Searches ChromaDB for historical facts.
    """

    client = get_chroma_client()

    embedding_fn = embedding_functions.DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name="sports_history",
        embedding_function=embedding_fn
    )

    results = collection.query(
        query_texts=[query_text],
        n_results=n_results,
        where={"sport": sport}
    )

    return results["documents"][0]