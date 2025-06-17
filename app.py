
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import openai
import io
import base64

# Set your OpenAI API Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🧍‍♂️ AI-Powered Posture Analysis")

uploaded_file = st.file_uploader("Upload a patient's posture image (back or side view)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze Posture"):
        with st.spinner("Analyzing..."):
            # Convert image to base64
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode()

            # Call OpenAI Vision
            response = openai.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": 
                             "You are a posture analysis expert. Look at this image and annotate any visible musculoskeletal issues (e.g., scoliosis, kyphosis, forward head posture, uneven shoulders, dislocated joints). Mark them clearly with arrows or lines and add text annotations."},
                            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64}"}}
                        ],
                    }
                ],
                max_tokens=1000,
            )

            result = response.choices[0].message.content
            st.markdown("### 🩺 Posture Report")
            st.write(result)
            st.success("Analysis complete!")
