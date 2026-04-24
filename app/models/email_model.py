from pydantic import BaseModel

class EmailRequest(BaseModel):
    purpose: str
    tone: str
    details: str