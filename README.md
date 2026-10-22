◈ **RAG Assistant — Local HR Intelligence**

Ask HR policy questions. Retrieve relevant evidence. Generate grounded answers. All locally.
A lightweight Retrieval-Augmented Generation (RAG) system that turns HR policy PDFs into a searchable knowledge base using local embeddings, vector similarity search, and LLM inference.

⚡ Core Stack

🐍 Python
🦙 Ollama
🚐 Qwen 2.5 7B
🎭 nomic-embed-text
📦 ChromaDB 
📃 PyPDF

◈ _**Architecture**


       HR Policy PDF
             │
             ▼
      Text Extraction
             │
             ▼
   Chunking + Embeddings
             │
             ▼
    ChromaDB Vector Store
             │
     User Query ─────────┐
             │           │
             ▼           │
     Query Embedding     │
             │           │
             ▼           │
    Similarity Search ◄──┘
             │
             ▼
     Retrieved Context
             │
             ▼
    Qwen 2.5 via Ollama
             │
             ▼
    Grounded HR Response


🚀 Get Started

**1 — Clone**

git clone https://github.com/Tamizhselvan26/RAG-Assistant-Local.git
cd RAG-Assistant-Local

**2 — Set up Python**

python -m venv .venv

Windows PowerShell:

.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

**3 — Download local models**

ollama pull qwen2.5:7b
ollama pull nomic-embed-text

**4 — Index and run**

Place your PDF at `resources/HRPolicy.pdf`.

python dataprocessor.py
python QueryProcessor.py


🧠 Engineering Highlights

| Capability            |                 Implementation                         |
|    ---                |                     ---                                |
| Document ingestion    | PDF extraction + overlapping text chunks               |
| Semantic retrieval    | Local embeddings + ChromaDB similarity search          |
| Answer generation     | Qwen 2.5 7B through Ollama                             |
| Knowledge grounding   | Retrieved policy context supplied to the LLM           |
| Hallucination mitigation | Explicit fallback instructions for missing evidence |
| Local persistence     | Reusable vector database stored on disk                |

🔒 Local-First by Design

→ No paid LLM API required for the core pipeline.  
→ Documents, embeddings, and inference can stay on the local machine.  
→ Prompt-based grounding helps reduce unsupported answers.

🗂️ Codebase
RAG-Assistant-Local/
├── resources/       → HR policy documents
├── pdfreader.py     → PDF extraction
├── chunker.py       → Text segmentation
├── embedder.py      → Embedding generation
├── vectorstore.py   → ChromaDB retrieval
├── dataprocessor.py → Indexing pipeline
├── llm.py           → Local model inference
├── QueryProcessor.py→ Query orchestration
└── requirements.txt


**Built to explore practical RAG engineering with local models, semantic search, and document-grounded question answering.**
