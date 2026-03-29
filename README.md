# ASK_Chipathon_and_Knowledge_Hub

ASK_Chipathon_and_Knowledge_Hub is a two-part project that combines a documentation-driven knowledge base with an AI-powered question answering system for Chipathon and OpenROAD learning resources. The repository contains a structured MkDocs knowledge hub and a Retrieval-Augmented Generation (RAG) chatbot backend that answers user questions using that knowledge base. 
## Project structure

The repository is organized into two main folders: `Ask_Chipathon/` for the chatbot backend and `Chitathon_Knowledge_Hub-main/` for the documentation site. The backend contains the API, ingestion pipeline, and RAG chain, while the documentation folder contains the markdown content and MkDocs configuration. 
```
ASK_Chipathon_and_Knowledge_Hub/
├── Ask_Chipathon/
│   ├── app.py
│   ├── config.py
│   ├── ingest.py
│   ├── rag_chain.py
│   ├── debug_check_store.py
│   └── requirements.txt
│
└── Chitathon_Knowledge_Hub-main/
    ├── mkdocs.yml
    ├── README.md
    ├── docs/
    │   ├── index.md
    │   ├── getting-started/
    │   ├── openroad-fundamentals/
    │   ├── debugging-playbooks/
    │   ├── chatbot/
    │   ├── faq/
    │   ├── contributor-guide/
    │   ├── submission/
    │   ├── artifact-map/
    │   └── seen-during-chipathon/
    └── .github/workflows/ci.yml
```
## Features
```

- Documentation-driven knowledge base built with MkDocs. 
- AI-powered RAG chatbot for answering Chipathon/OpenROAD questions from the knowledge base. 
- Modular backend with separate config, ingestion, and retrieval chain logic. 
- Markdown-based content organization for easy contribution and maintenance. 
- CI workflow for documentation deployment and validation.
## Tech stack

### Knowledge hub
- MkDocs for documentation site generation. 
- Markdown for content authoring. 
- GitHub Actions for CI workflow.

### ASK_Chipathon
- FastAPI for the backend API layer.
- LangChain for retrieval and chain orchestration.
- Chroma for vector storage. 
- Sentence Transformers for embeddings.
- Python for ingestion and API logic.

## How it works

The `Chitathon_Knowledge_Hub-main/docs` folder acts as the project knowledge source, containing structured documentation about setup, OpenROAD flow, debugging, FAQ, and submission guidance. The chatbot backend ingests this content, converts it into embeddings, stores it in Chroma, and uses a retrieval pipeline to answer user questions based on the indexed knowledge. [pip.pypa](https://pip.pypa.io/en/stable/cli/pip_freeze/)

The overall workflow is:
1. Author or update markdown docs in the knowledge hub.
2. Run the ingestion pipeline to create/update the vector database. 
3. Start the FastAPI backend.
4. Send a query to the chatbot API and receive an answer grounded in the stored documentation.
## Setup

### 1. Clone the repository

```bash
git clone https://github.com/KomatiBhavaniSankar/ASK_Chipathon_and_Knowledge_Hub.git
cd ASK_Chipathon_and_Knowledge_Hub
```

### 2. Create a virtual environment

```bash
cd Ask_Chipathon
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the chatbot backend

Before starting the API, run the ingestion step so the knowledge base is indexed into the vector store. The backend depends on that stored Chroma database to retrieve context for answers. [stackoverflow](https://stackoverflow.com/questions/61536466/pips-requirements-txt-best-practice)

### 1. Ingest the documents

```bash
python ingest.py
```

### 2. Start the FastAPI app

```bash
uvicorn app:app --reload
```

### 3. Open the API

- Root: `http://127.0.0.1:8000/`
- Swagger docs: `http://127.0.0.1:8000/docs`

## Running the documentation site

To preview the knowledge hub locally, go to the documentation folder and run MkDocs. The site content is defined by `mkdocs.yml` and the markdown files inside `docs/`. [pip.pypa](https://pip.pypa.io/en/stable/cli/pip_freeze/)

```bash
cd ../Chitathon_Knowledge_Hub-main
mkdocs serve
```

Then open:

```txt
http://127.0.0.1:8000/
```

## API example

Once the chatbot backend is running, you can test it using curl:

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d "{\"query\":\"What is OpenROAD?\"}"
```

## Documentation coverage

The knowledge hub includes sections for:
- Getting started and installation. 
- OpenROAD flow and fundamentals such as synthesis, placement, routing, floorplanning, and signoff.
- Debugging playbooks for common Chipathon issues. 
- FAQ and contributor guidance.
- Submission checklist and artifact mapping.

## Use cases

This project is useful for:
- Chipathon participants who need a searchable assistant for event documentation. 
- Students learning OpenROAD concepts through structured docs and question-answer interaction.
- Teams that want to turn markdown documentation into a knowledge-aware assistant. 

## Contributing

To contribute:
- Add or improve content in `Chitathon_Knowledge_Hub-main/docs/`. 
- Update the chatbot ingestion flow if new document types or retrieval features are needed.
- Test changes locally by running both the docs preview and the chatbot backend. 
