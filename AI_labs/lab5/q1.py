import cv2

# Load pre-trained Haar cascade classifiers for face, eye, nose, and smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')  # Adjust the path accordingly

# Function to detect faces, eyes, noses, and smiles
def detect_faces_eyes_nose_smiles(image):
    if image is None:
        print("Error: Unable to read the image.")
        return None

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the detected faces, eyes, noses, and smiles
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]

        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # Detect nose within the face region
        nose = nose_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=5)
        for (nx, ny, nw, nh) in nose:
            cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (0, 0, 255), 2)

        

    return image

# Test on an image
image_path = 'T33DPT-920x538.jpg'  # Replace with the path to your image
image = cv2.imread(image_path)
result_image = detect_faces_eyes_nose_smiles(image)
if result_image is not None:
    # Display the result
    cv2.imshow('Face, Eye, Nose, and Smile Detection', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
