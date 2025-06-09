# 📝 LLM-Powered Document Summarization Service

This is a simple, interactive **Document Summarization Web App** built using **FastAPI** and integrated with the **DeepSeek** model via **OpenRouter API**. The app allows users to input text or upload documents (PDF, DOCX, or TXT) and receive AI-generated summaries in various styles — **Brief**, **Detailed**, or **Bullet Points**.

---

## 🚀 Features

- 🔤 **Text & File Input**: Summarize direct text or upload a document
- 🎯 **Multiple Styles**: Choose between Brief, Detailed, or Bullet Point summaries
- 🧠 **Powered by LLM (DeepSeek)**: Summaries are generated using a state-of-the-art language model
- 📁 **Supports PDF, DOCX, TXT**
- 📡 **Error Handling**: Clear messages for invalid input, oversized files, and API failures
- ⚡ **Beautiful UI**: TailwindCSS for sleek, responsive interface
- 🧪 **Input validation** for empty fields and file size limits
- 💾 **Downloadable Summaries** (optional enhancement)

---

## 🗂️ Project Structure

Document_summarizer/
├── main.py          # FastAPI backend
├── summarize.py     # LLM logic + file parsing
├── models.py        # Pydantic models and enums
├── templates/
│ └── index.html     # Web UI (TailwindCSS + JS)
├── .env             # API keys (not committed)
├── requirements.txt # Python dependencies
└── README.md        # You're reading it!




---

## 🛠️ Technologies Used

- **Backend**: FastAPI
- **Frontend**: HTML + TailwindCSS + Vanilla JS
- **File Parsing**: `PyPDF2`, `python-docx`
- **LLM Provider**: [OpenRouter](https://openrouter.ai/) (DeepSeek model)
- **API Calls**: `requests`
- **Env Management**: `python-dotenv`

---

## 🧑‍💻 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/document-summarization-service.git

cd DOCUMENT_SUMMERIZER

### 2. Create a .env file

OPEN_ROUTER_API_KEY=your_openrouter_api_key


### 3. Install dependencies

pip install -r requirements.txt


### 4. Run the server

uvicorn main:app --reload


###5. Visit the App
# Open your browser and go to:

http://localhost:8000
