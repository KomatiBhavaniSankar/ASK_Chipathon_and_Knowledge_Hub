from typing import List

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

from config import CHROMA_DB_DIR
from ingest import SentenceTransformerEmbeddings

import os
import logging

# Suppress warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("sentence_transformers").setLevel(logging.ERROR)


# Vector Store
def get_vector_store() -> Chroma:
    embedding = SentenceTransformerEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma(
        embedding_function=embedding,
        persist_directory=CHROMA_DB_DIR,
        collection_name="openroad_rag",
    )


# Retriever
def get_retriever(k: int = 3):
    return get_vector_store().as_retriever(search_kwargs={"k": k})


# LLM
def get_llm():
    return OllamaLLM(
        model="llama3:instruct",
        temperature=0.2,
    )


# Prompt with strict citations
RAG_PROMPT = ChatPromptTemplate.from_template(
    """You are an expert in OpenROAD.

You MUST follow these rules:
1. Answer ONLY using the provided context
2. Every important statement MUST include citations like [1], [2]
3. Do NOT make up information
4. If answer is not in context, say "I don't know"
5. Use clear technical explanation with bullet points if needed

Question:
{question}

Context:
{context}

Answer with citations:
"""
)


# Format documents
def format_docs(docs: List[Document]) -> str:
    parts = []
    for i, d in enumerate(docs, start=1):
        source = d.metadata.get("source", "unknown")
        parts.append(f"[{i}] Source: {source}\n{d.page_content}")
    return "\n\n".join(parts)


# Main QA function
def answer_question(question: str, k: int = 3) -> dict:
    retriever = get_retriever(k)
    llm = get_llm()

    docs = retriever.invoke(question)

    # Remove duplicate sources
    seen = set()
    unique_docs = []
    for d in docs:
        src = d.metadata.get("source", "unknown")
        if src not in seen:
            seen.add(src)
            unique_docs.append(d)

    docs = unique_docs

    context = format_docs(docs)

    prompt = RAG_PROMPT.format(
        question=question,
        context=context
    )

    response = llm.invoke(prompt)

    answer_text = response if isinstance(response, str) else str(response)

    return {
        "answer": answer_text,
        "sources": [d.metadata.get("source", "unknown") for d in docs],
    }



# CLI
if __name__ == "__main__":
    print("OpenROAD RAG system ready. Ask your questions.")

    while True:
        q = input("\nAsk a question (or 'exit'): ")

        if q.lower().strip() in {"exit", "quit"}:
            print("Exiting...")
            break

        result = answer_question(q)

        print("\n--- Answer ---\n")
        print(result["answer"])

        print("\n--- Sources ---")
        for s in result["sources"]:
            print("-", s)