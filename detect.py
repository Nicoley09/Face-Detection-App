import cv2
import os

def get_default_cascade_path():
    """
    Return path to default frontal face Haar cascade that comes with OpenCV.
    """
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    return cascade_path

def load_cascade(cascade_path=None):
    """
    Load a CascadeClassifier. If cascade_path is None, use default.
    Returns cv2.CascadeClassifier instance.
    """
    if cascade_path is None:
        cascade_path = get_default_cascade_path()
    if not os.path.exists(cascade_path):
        raise FileNotFoundError(f"Haar cascade file not found at: {cascade_path}")
    classifier = cv2.CascadeClassifier(cascade_path)
    if classifier.empty():
        raise RuntimeError("Failed to load Haar cascade classifier.")
    return classifier

def detect_faces(gray_image, cascade, scaleFactor=1.1, minNeighbors=5, minSize=(30,30)):
    """
    Run cascade.detectMultiScale on the grayscale image.
    Returns list of rectangles (x, y, w, h).
    """
    faces = cascade.detectMultiScale(
        gray_image,
        scaleFactor=float(scaleFactor),
        minNeighbors=int(minNeighbors),
        minSize=minSize
    )
    return faces
