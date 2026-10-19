import cv2

camera_url = "http://172.18.109.242:8080/video"
cap = cv2.VideoCapture(camera_url)

# Capture one frame
ret, frame = cap.read()

if ret:
    # Save captured image
    cv2.imwrite("mobile_camera_image.jpg", frame)
    print("Image saved successfully")

else:
    print("Failed to capture image")

cap.release()
