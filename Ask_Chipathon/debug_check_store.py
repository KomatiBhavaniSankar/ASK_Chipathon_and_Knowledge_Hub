# debug_check_store.py
from rag_chain import get_vector_store

if __name__ == "__main__":
    vectordb = get_vector_store()

    # collection info
    print("Persist directory:", vectordb._persist_directory)
    print("Collection name:", vectordb._collection.name)

    # number of embeddings (if available)
    try:
        count = vectordb._collection.count()
    except Exception as e:
        print("Could not get count:", e)
        count = None

    print("Total embeddings (approx):", count)

    # simple similarity search
    print("\n=== Test similarity search ===")
    docs = vectordb.similarity_search("What is this project about?", k=3)
    for i, d in enumerate(docs, start=1):
        print(f"\n[{i}] Source:", d.metadata.get("source"))
        print(d.page_content[:400], "...")