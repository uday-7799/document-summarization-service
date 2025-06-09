
import os
import requests
from io import BytesIO
import PyPDF2
import docx
from dotenv import load_dotenv
from models import SummarizationStyle, SummaryResponse  # Ensure this file and enums are defined

load_dotenv()

# Load API key for OpenRouter
api_key = os.getenv("OPEN_ROUTER_API_KEY")
if not api_key:
    raise EnvironmentError("OPEN_ROUTER_API_KEY not found in environment.")

# OpenRouter API and DeepSeek model details
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "deepseek/deepseek-r1-0528:free"  

def extract_text_from_file(file_bytes: bytes, filename: str) -> str:
    """Extract text from PDF, DOCX, or plain text files."""
    try:
        if filename.endswith(".pdf"):
            reader = PyPDF2.PdfReader(BytesIO(file_bytes))
            return "\n".join([page.extract_text() or "" for page in reader.pages])
        elif filename.endswith(".docx"):
            doc = docx.Document(BytesIO(file_bytes))
            return "\n".join([para.text for para in doc.paragraphs])
        else:
            return file_bytes.decode("utf-8")
    except Exception as e:
        raise ValueError(f"Failed to extract text: {str(e)}")

def generate_prompt(text: str, style: SummarizationStyle) -> str:
    """Generate summarization prompt based on selected style."""
    if style == SummarizationStyle.BRIEF:
        return (
            "Summarize the following text in 1-2 clear sentences. "
            "Do not include any special characters like asterisks (*):\n\n"
            f"{text}"
        )
    elif style == SummarizationStyle.DETAILED:
        return (
            "Write a detailed summary of the following text. "
            "Avoid using special characters like asterisks (*):\n\n"
            f"{text}"
        )
    elif style == SummarizationStyle.BULLETS:
        return (
            "Summarize the following text into 5-7 concise bullet points. "
            "Use '-' or '→' to format each point. Do not use asterisks (*):\n\n"
            f"{text}"
        )
    return f"Summarize the following text. Avoid using asterisks:\n\n{text}"


def summarize_text(text: str, style: SummarizationStyle) -> SummaryResponse:
    """Call OpenRouter DeepSeek model to summarize text."""
    if not text.strip():
        return SummaryResponse(summary="", error="Input text is empty")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Truncate very long text to avoid API limits
    max_input_length = 10000  # ~10k characters
    if len(text) > max_input_length:
        text = text[:max_input_length] + "\n\n[Text truncated due to length]"

    prompt = generate_prompt(text, style)

    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "max_tokens": 2000,
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()

        summary = result["choices"][0]["message"]["content"].strip()
        return SummaryResponse(summary=summary)

    except requests.exceptions.RequestException as e:
        return SummaryResponse(summary="", error=f"API error: {str(e)}")