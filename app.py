import streamlit as st
from utils import load_image_from_bytes, hex_to_bgr, draw_faces, bgr_to_rgb
from detect import load_cascade, detect_faces
from PIL import Image
import numpy as np
import tempfile
import cv2

st.set_page_config(page_title="Viola-Jones Face Detection", layout="centered")

# --------------------------------
# Header & Instructions
# --------------------------------
st.title("🕵️ Viola-Jones Face Detection (Haar Cascade)")

st.markdown("""
### **How to Use This App**
1. **Upload an image** or use your **camera**.
2. Adjust **scaleFactor** and **minNeighbors** to control detection accuracy.
3. Choose **rectangle color** and **line thickness**.
4. Press **Detect faces**.
5. **Download** the processed image.

This app uses the **Viola-Jones Haar Cascade Algorithm** for real-time face detection.
""")

with st.expander("ℹ️ Parameter tips"):
    st.write("- **scaleFactor**: How much the image size is reduced at each scale. Lower values → more accurate but slower.")
    st.write("- **minNeighbors**: How many detection rectangles must overlap to confirm a face. Higher values → fewer false positives.")

# --------------------------------
# Image Input + Controls
# --------------------------------
col1, col2 = st.columns(2)

with col1:
    uploaded = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])
    cam = st.camera_input("Or take a picture")

with col2:
    scale_factor = st.slider("scaleFactor", 1.01, 2.0, 1.10, 0.01)
    min_neighbors = st.slider("minNeighbors", 1, 10, 5)
    rect_color = st.color_picker("Rectangle color", "#00FF00")
    thickness = st.slider("Rectangle thickness", 1, 10, 2)

# --------------------------------
# Load Haar Cascade
# --------------------------------
try:
    cascade = load_cascade()
except Exception as e:
    st.error(f"Failed to load Haar Cascade: {e}")
    st.stop()

# --------------------------------
# Read Input Image
# --------------------------------
image_bgr = None

if uploaded:
    image_bgr = load_image_from_bytes(uploaded.read())
elif cam:
    image_bgr = load_image_from_bytes(cam.read())

# --------------------------------
# Display + Detection
# --------------------------------
if image_bgr is not None:

    st.subheader("Original Image")
    st.image(bgr_to_rgb(image_bgr), use_column_width=True)

    if st.button("Detect faces"):

        gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

        try:
            faces = detect_faces(
                gray,
                cascade,
                scaleFactor=scale_factor,
                minNeighbors=min_neighbors
            )
        except Exception as e:
            st.error(f"Detection error: {e}")
            st.stop()

        # Results
        if len(faces) == 0:
            st.warning("No faces detected. Try lowering scaleFactor or minNeighbors.")
        else:
            st.success(f"Detected **{len(faces)}** face(s).")

        # Draw rectangles
        color_bgr = hex_to_bgr(rect_color)
        annotated_bgr = draw_faces(
            image_bgr.copy(),
            faces,
            color_bgr=color_bgr,
            thickness=thickness
        )
        annotated_rgb = bgr_to_rgb(annotated_bgr)

        st.subheader("Annotated Image")
        st.image(annotated_rgb, use_column_width=True)

        # Show coordinates
        if len(faces) > 0:
            st.write("Detected face coordinates (x, y, w, h):")
            st.json([tuple(map(int, box)) for box in faces])

        # Create download file
        tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        Image.fromarray(annotated_rgb).save(tmp.name)

        with open(tmp.name, "rb") as f:
            st.download_button(
                "Download annotated image",
                data=f,
                file_name="annotated_faces.png",
                mime="image/png"
            )

else:
    st.info("📌 Upload an image or take a picture to begin.")
