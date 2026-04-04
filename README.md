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
