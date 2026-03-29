import os
import requests
from typing import Optional
from openai import OpenAI


def retrieve_context(question: str, k: int = 4) -> str:
    return f"Retrieved top {k} context items for: {question}"


def build_prompt(question: str, context: str) -> str:
    return f"""
You are a helpful assistant answering questions based on the given retrieved context.

Retrieved Context:
{context}

User Question:
{question}

Answer clearly and only use the context if relevant.
""".strip()


def call_ollama(prompt: str, model: Optional[str] = None) -> str:
    model_name = model or "llama3"
    url = "http://127.0.0.1:11434/api/generate"

    response = requests.post(
        url,
        json={
            "model": model_name,
            "prompt": prompt,
            "stream": False
        },
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()
    return data.get("response", "").strip()


def call_groq(prompt: str, api_key: Optional[str] = None, model: Optional[str] = None) -> str:
    key = api_key or os.getenv("GROQ_API_KEY")
    if not key:
        raise ValueError("Groq API key is missing.")

    client = OpenAI(
        api_key=key,
        base_url="https://api.groq.com/openai/v1"
    )

    model_name = model or "llama-3.3-70b-versatile"

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful RAG assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()


def answer_question(
    question: str,
    k: int = 4,
    provider: str = "ollama",
    model: Optional[str] = None,
    api_key: Optional[str] = None,
) -> str:
    context = retrieve_context(question, k=k)
    prompt = build_prompt(question, context)

    provider = (provider or "ollama").strip().lower()

    if provider == "ollama":
        return call_ollama(prompt, model=model)

    if provider == "groq":
        return call_groq(prompt, api_key=api_key, model=model)

    raise ValueError("Unsupported provider. Use 'ollama' or 'groq'.")