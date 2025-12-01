import io
from PIL import Image
import numpy as np
import cv2

def load_image_from_bytes(image_bytes: bytes):
    """
    Load image bytes (uploaded file or camera bytes) -> OpenCV BGR ndarray.
    """
    img_pil = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = np.array(img_pil)[:, :, ::-1]  # RGB -> BGR for OpenCV
    return img

def hex_to_bgr(hex_color: str):
    """
    Convert '#RRGGBB' hex string to BGR tuple for OpenCV functions.
    """
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (b, g, r)

def draw_faces(img_bgr, faces, color_bgr=(0,255,0), thickness=2):
    """
    Draw rectangles around faces on a copy of the image and return BGR ndarray.
    faces: iterable of (x, y, w, h)
    """
    annotated = img_bgr.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(annotated, (x, y), (x+w, y+h), color_bgr, thickness)
    return annotated

def bgr_to_rgb(img_bgr):
    """Convert BGR (OpenCV) to RGB (PIL/Streamlit display)"""
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
