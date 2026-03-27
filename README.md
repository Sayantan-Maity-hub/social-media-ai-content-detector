# AI Content Detector

A starter project for classifying images as **AI-generated** or **real**.

## What this project does
- Loads image datasets from folder structure
- Trains a simple CNN baseline in PyTorch
- Evaluates validation accuracy
- Saves trained model weights
- Runs prediction on a single image
- Provides a small Flask app for local testing

## Folder format

```text
data/processed/
├── train/
│   ├── ai/
│   └── real/
└── val/
    ├── ai/
    └── real/
    