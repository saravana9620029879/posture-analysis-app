import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(page_title="Posture Analysis", layout="centered")

st.title("🧍 Posture Analysis Tool (Simulated)")
st.write("Upload a side or back posture photo to get simulated results and annotations.")

uploaded_file = st.file_uploader("📷 Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Draw annotations
    draw = ImageDraw.Draw(image)

    # Dummy coordinates for simulated issues
    draw.line((150, 50, 150, 200), fill="red", width=3)
    draw.text((160, 50), "Elevated Shoulder", fill="red")

    draw.line((200, 300, 250, 400), fill="blue", width=3)
    draw.text((260, 350), "Possible Scoliosis", fill="blue")

    draw.line((100, 150, 180, 150), fill="green", width=3)
    draw.text((100, 160), "Forward Head Posture", fill="green")

    st.image(image, caption="🩺 Simulated Posture Annotations", use_column_width=True)

    # Simulated diagnostic text
    st.markdown("### 📝 Simulated Diagnosis")
    st.success("""
- Right shoulder appears elevated
- Mild spinal curve suggesting scoliosis
- Forward head posture detected
- Recommendation: Consult a physiotherapist
""")

