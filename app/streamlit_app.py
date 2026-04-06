import requests
import stramlit as st
from PIL import Image
API_URL = "http://127.0.0.1:8000/analyze-post"
st.set_page_config(page_title="ReelGuard", layout="wide")
st.title("ReelGuard")
st.subheader("Real-Time AI Content Detection for Social Media")

col1, col2 = st.columns(2)
with col1:
    uploaded_image = st.file_uploader("Upload and image to analyze", type=["jpg", "jpeg", "png"])
    caption = st.text_area("Enter caption", height = 150)

    analyze_button  = st.button("Analyze Post")


