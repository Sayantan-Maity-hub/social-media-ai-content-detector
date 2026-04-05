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

@app.post("/analyze-post")
def analyze_post(
    image: UploadFile = File(...),
    caption: str = Form(...),
): # Accept an image and caption runs dummy inference for now, fuses scores, and returns explainations.
    if not caption.strip():
        raise HTTPException(status_code = 400, details = "Caption cannot be empty.")
        
    _ = validate_image(image)
    # Dummy scores for demonstration purposes
    artifact_score = 0.6
    hyperrealism_score = 0.4
    text_score = 0.5

    fused_output = fuse_scores(
        artifact_score = artifact_score,
        hyperrealism_score = hyperrealism_score,
        text_score = text_score,
    )

    reasons = generate_reasons(
        artifact_score = artifact_score, 
        hyperrealism_score = hyperrealism_score,
        text_score = text_score,
    )

    return {
        **fused_output,
        "reasons": reasons,
        "caption_length": len(caption),
        "message": "Analysis completed successfully.",

    }

    

