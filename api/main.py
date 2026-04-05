from io import BytesIO
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image

from src.models.fusion import fuse_scores
from src.interference.explain import generate_resons

app = FastAPI(title = "ReelGuard API", version = "0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/helth")
def health_check():
    return {"status": "ok"}

