

---

# 🕵️ Viola-Jones Face Detection App

![Python](https://img.shields.io/badge/python-3.8+-blue) ![Streamlit](https://img.shields.io/badge/streamlit-v1.30-orange) ![OpenCV](https://img.shields.io/badge/opencv-v4.8-blue)

A **real-time face detection** web application built with **Streamlit** using the **Viola-Jones (Haar Cascade) algorithm**.
Upload an image or use your webcam, adjust detection parameters, customize rectangle color, and download annotated results.

---

## 🎥 Demo

![Demo GIF](https://via.placeholder.com/600x300.png?text=Demo+GIF+Here)
*Replace the above with your own demo GIF showing face detection in action.*

---

## 🚀 Features

* **Face Detection**: Detects faces in images using OpenCV Haar Cascades.
* **Adjustable Parameters**: `scaleFactor` and `minNeighbors` for fine-tuning detection.
* **Customizable Rectangles**: Choose color and thickness for face bounding boxes.
* **Upload & Webcam Input**: Upload JPG/PNG images or take a photo directly.
* **Download Annotated Images**: Save processed images to your device.
* **Interactive Instructions**: Step-by-step guidance inside the app.

---

## 📸 Screenshots

### Original Image

![Original Image](https://via.placeholder.com/400x300.png?text=Original+Image)

### Annotated Image

![Annotated Image](https://via.placeholder.com/400x300.png?text=Annotated+Image)

*Replace the above placeholders with actual screenshots from your app.*

---

## 📦 Requirements

* Python 3.8+
* Install dependencies:

```bash
pip install streamlit opencv-python pillow numpy
```

For extended OpenCV features:

```bash
pip install opencv-contrib-python
```

* Required file: `haarcascade_frontalface_default.xml` (Haar cascade classifier)

---

## ▶️ Running the App

1. Clone the repository:

```bash
git clone https://github.com/yourusername/viola-jones-face-detection.git
cd viola-jones-face-detection
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. The app opens in your browser.

---

## 📘 How to Use

1. **Upload an image** (JPG/PNG) or **take a picture**.
2. Adjust detection parameters:

   * **scaleFactor**: Smaller → more accurate but slower
   * **minNeighbors**: Higher → fewer false positives
   * **Rectangle color** and **thickness**
3. Click **Detect Faces**.
4. View:

   * Original image
   * Annotated image with bounding boxes
   * Detected face coordinates (x, y, w, h)
5. Click **Download annotated image** to save it.

---

## ⚙️ How It Works

1. Convert the image to **grayscale**.
2. Use OpenCV **Haar cascade classifier** to detect faces.
3. Draw rectangles around faces using **user-defined color and thickness**.
4. Display annotated image and allow download.

---

## 📚 Technologies Used

| Technology | Purpose                               |
| ---------- | ------------------------------------- |
| Streamlit  | Web UI                                |
| OpenCV     | Haar Cascade face detection & drawing |
| Pillow     | Image handling                        |
| NumPy      | Array manipulation                    |

---

## 📝 Notes

* Ensure **OpenCV** is installed:

```bash
pip install opencv-python
```

* Keep `haarcascade_frontalface_default.xml` in the project directory.
* Works best with **well-lit images** and **clearly visible faces**.

---

## 📄 License

This project is **free to use and modify** for educational purposes.

---

## 💡 Pro Tips

* Lower `scaleFactor` (close to 1.05) for better accuracy on high-resolution images.
* Increase `minNeighbors` to reduce false positives.
* Use contrasting rectangle colors for better visualization.

---


