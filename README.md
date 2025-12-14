# 📄 AI PDF Summarizer & Q&A App (Streamlit + LangChain + OpenRouter)

An interactive **PDF Summarizer and Question-Answering application** built with **Streamlit**, **LangChain**, and **OpenRouter GPT models**. This app allows users to upload a PDF, process its content into vector embeddings, and ask natural-language questions to get AI-generated answers based on the document.

---

## 🚀 Features
- 📂 Upload and read PDF files
- ✂️ Smart text chunking using LangChain
- 🧠 Semantic search with FAISS vector database
- 🔍 Ask questions directly from the PDF content
- 🤖 GPT-4o-mini model via OpenRouter API
- 📊 Token usage tracking with OpenAI callbacks
- ⚡ Fast and user-friendly Streamlit UI

---

## 🛠️ Tech Stack
- Python
- Streamlit
- LangChain
- OpenRouter API
- OpenAI Embeddings
- FAISS
- PyPDF2

---

## 📌 How It Works
1. Upload a PDF file
2. Text is extracted and split into chunks
3. Chunks are converted into embeddings
4. FAISS stores embeddings for semantic search
5. User asks a question
6. Relevant content is sent to GPT for an accurate answer

---

## 🎯 Use Cases
- Document summarization
- Research paper analysis
- Notes extraction
- Study material Q&A
- AI-powered document assistants

---

## 🔐 Setup
Add your OpenRouter API key in the `api_key` variable before running the app.

---

## ⭐ Ideal For
Beginners and developers exploring **AI document intelligence**, **RAG pipelines**, and **LLM-powered apps**.
