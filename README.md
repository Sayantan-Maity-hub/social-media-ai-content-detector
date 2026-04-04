# ReelGuard — Real-Time AI Content Detection System

ReelGuard is a multimodal AI-powered system designed to analyze social media content and estimate the likelihood that a post is **AI-generated vs human-created**.

The system processes **images and captions**, combines multiple signals (visual artifacts, hyperrealistic facial patterns, and text features), and returns a **probabilistic authenticity score with human-readable explanations**.

---

## 🚀 Overview

With the rapid growth of AI-generated content on social platforms, it has become increasingly difficult for users to distinguish between real and synthetic media.

ReelGuard addresses this problem by building an **end-to-end detection pipeline** that:

- Accepts an image and caption as input
- Analyzes visual patterns using a CNN-based model
- Detects hyperrealistic facial characteristics (symmetry, smoothness, averageness)
- Evaluates caption text for AI-like linguistic patterns
- Combines all signals using a fusion model
- Returns:
  - AI probability score
  - Risk label
  - Explanation of detected signals

---

## 🧠 Key Features

- Multimodal detection (image + text)
- Artifact-based image analysis (CNN)
- Hyperrealism-based face analysis (symmetry, texture, proportions)
- Text classification using NLP models
- Fusion-based decision system
- Explainable outputs (reason generation)
- FastAPI backend for real-time inference
- Streamlit frontend for interactive testing

---

## 🏗️ System Architecture

User Input (Image + Caption)
│
▼
FastAPI Backend
│
├── Image Artifact Model
├── Face Hyperrealism Module
├── Text Detection Model
│
▼
Fusion Layer
│
▼
Explanation Generator
│
▼
JSON Response → UI Display


---

## 🔬 Detection Strategy

### 1. Image Artifact Detection
Detects:
- unnatural textures
- repeated patterns
- diffusion/GAN artifacts

### 2. Face Hyperrealism Analysis (Key Innovation)
Inspired by research on AI-generated faces:

- overly symmetric faces
- unusually smooth skin texture
- statistically “average” facial structure

> AI faces can appear **more real than real humans** — this module captures that.

### 3. Text Analysis
Detects:
- templated language
- repetitive phrasing
- generic promotional tone

---

## 📊 Example Output

```json
{
  "ai_probability": 81.3,
  "human_probability": 18.7,
  "risk_label": "Likely AI-generated",
  "artifact_score": 0.78,
  "hyperrealism_score": 0.69,
  "text_score": 0.84,
  "reasons": [
    "Facial structure appears unusually symmetric",
    "Skin texture appears smoother than typical camera-captured images",
    "Caption language resembles generated promotional phrasing"
  ]
}
