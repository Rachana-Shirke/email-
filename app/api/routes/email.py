from fastapi import APIRouter
from app.models.email_model import EmailRequest
from app.services.email_service import generate_email

router = APIRouter(prefix="/email", tags=["Email"])

@router.post("/generate")
def generate_email_api(request: EmailRequest):
    return generate_email(request)