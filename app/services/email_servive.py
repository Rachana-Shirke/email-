from app.services.ai_service import generate_ai_email
from app.utils.prompt_builder import build_prompt

def generate_email(request):
    
    prompt = build_prompt(
        request.purpose,
        request.tone,
        request.details
    )

    email = generate_ai_email(prompt)

    return {"email": email}