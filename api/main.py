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

def validate_image(upload_file: UploadFile) -> Image.Image:  # validate uploaded image and return a PIL Image object.
    if not upload_file.content_type or not upload_file.content_type.startwith("image/"):
        raise HTTPException(status_code = 400, details = "Uploaded file must be and image.")
    
    try:
        image_bytes = upload_file.file.read()
        image = Image.open(BytesIO(image_bytes)).covert("RGB")
        return image
    except Exception as exc:
        raise HTTPException(status_code = 400, details = "Invalid image file.") from exc
    
    

