import cv2

# --------------------------------------------------
# STEP 1: Mobile camera stream URL
# Replace PHONE_IP with the IP shown in IP Webcam app
# --------------------------------------------------
camera_url = "http://172.18.109.242:8080/video"

# --------------------------------------------------
# STEP 2: Create a VideoCapture object
# OpenCV treats the mobile stream like a webcam
# --------------------------------------------------
cap = cv2.VideoCapture(camera_url)

# Check if the camera stream is opened successfully
if not cap.isOpened():
    print("Error: Cannot access mobile camera")
    exit()

print("Mobile camera connected successfully")

# --------------------------------------------------
# STEP 3: Read frames continuously
# --------------------------------------------------
while True:
    # Read a frame from the mobile camera
    ret, frame = cap.read()

    # ret = True if frame is read correctly
    if not ret:
        print("Failed to receive frame")
        break

    # --------------------------------------------------
    # STEP 4: Display the frame on laptop screen
    # --------------
