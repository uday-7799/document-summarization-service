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

document-summarization-service/
├── main.py             # FastAPI app entry
├── summarize.py        # LLM logic + file parsing
├── models.py           # Pydantic request/response models
├── templates/
│   └── index.html      # UI with TailwindCSS & JS
├── .env                # API key file (not committed)
├── requirements.txt    # Python dependencies
└── README.md           # Project info



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

### 1. Clone the repository
git clone https://github.com/uday-7799/document-summarization-service.git

cd document-summarization-service

### 2. Create a .env file
#### Add your OpenRouter API key to a file named .env in the root directory
OPEN_ROUTER_API_KEY=your_openrouter_api_key

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the FastAPI server
uvicorn main:app --reload

### 5. Open your browser and visit
http://localhost:8000





## 🎬 Demo

👉 [Click here to watch the demo video](./demo.mp4)




## 🧠 How It Works

```text
1. User enters text or uploads a .txt, .pdf, or .docx file
2. Text is extracted and a prompt is generated based on the selected style
3. Prompt is sent to the DeepSeek model via OpenRouter API
4. Response (summary) is displayed in the browser
5. Errors (if any) are shown clearly to the user



## 🧠 Design Approach & Implementation Details

The application was designed to be modular, lightweight, and easy to use. FastAPI was chosen for its speed and simplicity in building APIs. The frontend is built using HTML and TailwindCSS to create a responsive and clean UI. Users can enter text directly or upload supported file types 
(`.txt`, `.pdf`, `.docx`). These files are processed using `PyPDF2` and `python-docx` to extract raw text.

Based on the selected summarization style (Brief, Detailed, Bullet Points), a prompt is dynamically constructed and sent to the DeepSeek LLM via the OpenRouter API. The API response is parsed and displayed on the frontend using vanilla JavaScript. The project includes input validation, error handling, and environment configuration via `.env` for secure API key management.

The entire solution is container-ready and follows a separation of concerns: frontend (template), backend logic (summarize.py), data models (models.py), and routing (main.py).
