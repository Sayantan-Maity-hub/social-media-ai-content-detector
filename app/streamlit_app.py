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

with col2:
    st.markdown("### Results")
    result_placeholder = st.empty()
if analyze_button:
    if uploaded_image is None:
        st.error("please upload an image")
    elif not caption.strip():
        st.error("please enter a caption")
    else:
        try:
            files = {
                "image": (uploaded_image.name, uploaded_image.getvalue(), uploaded_image.type)

            }
            data = {
                "caption": caption
            }
            response = requests.post(API_URL, files=files, data=data, timeout=60)
            if response.status_code == 200:
                result = response.json()

                with col1:
                    st.markdown("### Uploaded Image")
                    image = Image.open(uploaded_image)
                    st.image(image, use_container_width=True)

                with col2:
                    st.success("Analysis completed")
                    st.metric("AI Probability", f"{result['ai_probability']:.2f}%")
                    st.metric("Human Probability", f"{result['human_probability']:.2f}%")
                    st.write(f"** Risk Label:** {result['risk_label']}")
                    st.write(f"** Artifact Score:** {result['artifact_score']:.2f}")
                    st.write(f"** Hyperrealism Score:** {result['hyperrealism_score']:.2f}")
                    st.write(f"** Text Score:** {result['text_score']:.2f}")
                    
