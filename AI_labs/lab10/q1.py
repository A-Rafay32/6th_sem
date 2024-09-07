import cv2
import torch
from models.experimental import attempt_load
from utils.general import non_max_suppression, scale_coords
from utils.datasets import letterbox

# Load model
model = attempt_load('best.pt', map_location='cpu')  # Adjust as needed
model.eval()

# Initialize video capture
cap = cv2.VideoCapture(0)  # 0 for webcam or provide video file path

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess frame
    img = letterbox(frame, 640)[0]
    img = img[:, :, ::-1].transpose(2, 0, 1)
    img = np.ascontiguousarray(img)

    # Run inference
    with torch.no_grad():
        pred = model(img, augment=False)[0]
        pred = non_max_suppression(pred, 0.25, 0.45, classes=None, agnostic=False)

    # Process detections
    for det in pred:
        if len(det):
            det[:, :4] = scale_coords(img.shape[1:], det[:, :4], frame.shape).round()

            for *xyxy, conf, cls in reversed(det):
                label = f'{conf:.2f}'
                cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0, 255, 0), 2)
                cv2.putText(frame, label, (int(xyxy[0]), int(xyxy[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display frame
    cv2.imshow('Traffic Sign Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
