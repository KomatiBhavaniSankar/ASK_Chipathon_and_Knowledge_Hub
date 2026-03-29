from pathlib import Path
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from rag_chain import answer_question


# ASGI app object (must be named "app")
app = FastAPI(title="ASK Chipathon Knowledge Hub")

BASE_DIR = Path(__file__).resolve().parent
templates_dir = BASE_DIR / "templates"
static_dir = BASE_DIR / "static"


# Serve static files
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    question: str
    k: int = 4
    provider: str = "ollama"   # "ollama" or "groq"
    model: Optional[str] = None
    api_key: Optional[str] = None


@app.get("/", response_class=HTMLResponse)
async def home():
    index_file = templates_dir / "index.html"
    if not index_file.exists():
        return HTMLResponse(
            "<h2>Frontend not found. Create templates/index.html</h2>",
            status_code=500,
        )
    return HTMLResponse(index_file.read_text(encoding="utf-8"))


@app.post("/ask")
async def ask(query: Query):
    try:
        result = answer_question(
            question=query.question,
            k=query.k,
            provider=query.provider,
            model=query.model,
            api_key=query.api_key,
        )
        return JSONResponse({"answer": result})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)