from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from models import SummarizationStyle, SummarizeRequest, FileUploadRequest, SummaryResponse
from summarize import summarize_text, extract_text_from_file
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/summarize/text")
async def summarize_text_api(request: SummarizeRequest) -> SummaryResponse:
    try:
        # Ensure style is properly converted to enum
        style = SummarizationStyle(request.style)
        return summarize_text(request.text, style)
    except ValueError as e:
        return SummaryResponse(summary="", error=str(e))

@app.post("/summarize/file")
async def summarize_file(file: UploadFile, style: str = Form(...)) -> SummaryResponse:
    if not file.filename:
        return SummaryResponse(summary="", error="No file uploaded")
    
    try:
        file_bytes = await file.read()
        text = extract_text_from_file(file_bytes, file.filename)
        style_enum = SummarizationStyle(style.lower())
        return summarize_text(text, style_enum)
    except ValueError as e:
        return SummaryResponse(summary="", error=str(e))
    except Exception as e:
        return SummaryResponse(summary="", error=f"File processing error: {str(e)}")
    
# Endpoint to check API status (for loader)
@app.get("/api/status")
async def api_status():
    return JSONResponse({"status": "ok"})