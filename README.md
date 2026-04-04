# AI Content Detector

A starter project for classifying images as **AI-generated** or **real**.

## What this project does
- Loads image datasets from folder structure
- Trains a simple CNN baseline in PyTorch
- Evaluates validation accuracy
- Saves trained model weights
- Runs prediction on a single image
- Provides a small Flask app for local testing

# Setup
python -m venv .venv
# Windows
.venv\Scripts\activate
#Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt

# Train
python train.py

# Predict
python predict.py --image sample_images/test.jpg --weights models/best_model.pt

# Run local web app
python app.py

# Notes 
This is a baseline starter.Better results usually reqire:
stronger datasets
better augmentation
transfer learning
metadata analysis
calibration and threshhold tuning
---
## requirements.txt

```text
torch 
torchvision
pillow
numpy
scikit-learn
matplotlib
flask 
```
# 


.gitignore

_pycache/
*.pyc
.venv/
models/*.pt
models/*.pth
.Ds_store
Thumbs.db
