# Mobile Camera Stream Capture with OpenCV

A Python project that connects to a mobile device's camera stream over a local IP network to capture static images and display real-time video feeds using OpenCV.

## Features

Single Frame Capture (`Laptop_Control.py`): Connects to the IP camera stream, captures a single frame, and saves it locally as `mobile_camera_image.jpg`.
Live Video Streaming (`Mobile_Camera.py`): Continuously reads and displays a live video feed from a mobile device camera.
Stream Diagnostics: Checks connection status and provides feedback if the stream cannot be accessed.

## Prerequisites & Requirements

Python 3.x installed on your system.
OpenCV library: Install it using pip:
  ```bash
  pip install opencv-python

File Structure

├── Laptop_Control.py   # Script to capture and save a single image
├── Mobile_Camera.py   # Script to connect and display live camera feed
└── README.md           # Project documentation