import os
from dotenv import load_dotenv

load_dotenv()

CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "./chroma_db")
DOCS_DIR = os.getenv("DOCS_DIR", "./docs")

# Website(s) to ingest
WEB_URLS = [
    "https://openroad-flow-scripts.readthedocs.io/en/latest/index2.html"
]