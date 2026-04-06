import requests
import stramlit as st
from PIL import Image
API_URL = "http://127.0.0.1:8000/analyze-post"
st.set_page_config(page_title="ReelGuard", layout="wide")
st.title("ReelGuard")
st.subheader("Real-Time AI Content Detection for Social Media")
