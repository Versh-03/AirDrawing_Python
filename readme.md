# Air Draw — Hand Tracking Canvas

> Turn your webcam into a digital sketchbook using just your hand.

## What is this?

This application tracks your hand movements in real-time, allowing you to paint in the air using simple gestures. By combining MediaPipe's computer vision with OpenCV's image processing, it transforms your physical movements into a digital overlay on your live webcam feed.

---

## Features

- **Fluid motion tracking** — follows your index finger with minimal latency
- **Gesture control** — raise index + middle finger to stop drawing, index only to draw
- **Live blending** — drawing is layered directly over your webcam feed
- **Quick reset** — press `C` to clear the canvas instantly
- **Clean exit** — press `Q` to quit

---

## Getting Started

### Prerequisites

- Python 3.8+
- A working webcam

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Versh-03/AirDrawing_Python.git
   ```

2. Install dependencies
   ```bash
   pip install opencv-python mediapipe==0.10.5 numpy
   ```

3. Run the app
   ```bash
   python main.py
   ```

---

## How It Works
1. **Detection** — MediaPipe identifies 21 landmark points on your hand every frame
2. **Targeting** — the app monitors landmark 8 (index fingertip) for position
3. **Gesture validation** — compares fingertip position against knuckle position to detect drawing state
4. **Pathing** — calculates distance between current and previous finger position and draws a line between them
5. **Blending** — merges the webcam frame and drawing canvas using weighted transparency

---

## Tech Stack
- [OpenCV](https://opencv.org/) — webcam capture, image processing, drawing
- [MediaPipe](https://mediapipe.dev/) — real-time hand landmark detection
- [NumPy](https://numpy.org/) — canvas creation and image manipulation

---

## License

MIT
