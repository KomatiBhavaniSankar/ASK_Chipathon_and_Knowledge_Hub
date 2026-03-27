import os

os.environ.setdefault("USER_AGENT", "AskChipathonRAG/0.1")

from pathlib import Path
from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, WebBaseLoader
from langchain_community.document_loaders.markdown import UnstructuredMarkdownLoader
from langchain_chroma import Chroma
from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings

from config import DOCS_DIR, CHROMA_DB_DIR, WEB_URLS


#  Embedding Wrapper
class SentenceTransformerEmbeddings(Embeddings):
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.model.encode(texts, show_progress_bar=False).tolist()

    def embed_query(self, text: str) -> List[float]:
        return self.model.encode([text])[0].tolist()


#  Load Local Docs
def load_from_directory(path: str):
    path_obj = Path(path)
    if not path_obj.exists():
        raise FileNotFoundError(f"Docs directory not found: {path}")

    loader = DirectoryLoader(
        path,
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader,
        show_progress=True,
    )

    docs = loader.load()

    #  Ensure metadata has source
    for d in docs:
        if "source" not in d.metadata:
            d.metadata["source"] = str(path_obj)

    return docs


#  Load Web Docs (safe)
def load_from_web(urls: List[str]):
    try:
        loader = WebBaseLoader(urls)
        docs = loader.load()

        #  Add source metadata
        for d, url in zip(docs, urls):
            d.metadata["source"] = url

        return docs

    except Exception as e:
        print(f"Error loading web docs: {e}")
        return []


#  Split Docs
def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""],
    )
    return splitter.split_documents(documents)


#  Build Vector DB
def build_vector_store():
    print(" Loading documents from directory...")
    dir_docs = load_from_directory(DOCS_DIR)

    print(" Loading documents from web URLs...")
    web_docs = load_from_web(WEB_URLS)

    all_docs = dir_docs + web_docs
    print(f" Total raw documents: {len(all_docs)}")

    if len(all_docs) == 0:
        raise ValueError(" No documents loaded. Check DOCS_DIR or WEB_URLS.")

    print(" Splitting into chunks...")
    chunks = split_documents(all_docs)
    print(f" Total chunks: {len(chunks)}")

    print(" Setting up embeddings...")
    embedding = SentenceTransformerEmbeddings()

    print(f" Building Chroma vector store at: {CHROMA_DB_DIR}")

    Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=CHROMA_DB_DIR,
        collection_name="openroad_rag",
    )

    print(" Vector store built successfully!")


if __name__ == "__main__":
    build_vector_store()