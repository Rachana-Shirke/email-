from fastapi import FastAPI
from app.api.routes import email

app = FastAPI(title="AI Email Generator")

app.include_router(email.router)