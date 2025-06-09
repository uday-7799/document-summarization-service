
from pydantic import BaseModel, validator
from enum import Enum
from typing import Optional

class SummarizationStyle(str, Enum):
    BRIEF = "brief"
    DETAILED = "detailed"
    BULLETS = "bullets"

class SummarizeRequest(BaseModel):
    """Request model for text summarization"""
    text: str
    style: str  # String input that gets validated

    @validator('style')
    def validate_style(cls, v):
        """Convert string to valid enum value"""
        try:
            return SummarizationStyle(v.lower().strip())
        except ValueError:
            valid_styles = [e.value for e in SummarizationStyle]
            raise ValueError(
                f"Invalid style '{v}'. Must be one of: {valid_styles}"
            )
            

class FileUploadRequest(BaseModel):
    """Request model for file upload summarization"""
    file_bytes: bytes
    filename: str
    style: str  # Same style handling as above

    @validator('style')
    def validate_style(cls, v):
        """Reuse the same style validation"""
        return SummarizeRequest.validate_style(v)

class SummaryResponse(BaseModel):
    """Standard response model"""
    summary: str
    error: Optional[str] = None