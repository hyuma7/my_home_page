import cv2
import pytesseract
from moviepy.editor import VideoFileClip
import os 

def extract_text_from_video(video_path, roi, frame_interval=120):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % frame_interval == 0:
            x, y, w, h = roi
            roi_frame = frame[y:y+h, x:x+w]
            roi_frame = improve_test_accuracy(roi_frame)
            
            custom_oem_psm_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist="0123456789"'
            text = pytesseract.image_to_string(roi_frame, config=custom_oem_psm_config).strip()

            if text and text.isdigit():
                num : int = int(text)
                yield frame_count, num
        
        frame_count += 1
    cap.release()


def improve_test_accuracy(target):
    # BGR to Gray conversion
    gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    
    # Gaussian blur for noise reduction
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Simple binary thresholding
    binaryThreshold = 189
    ret, binaried = cv2.threshold(blurred, binaryThreshold, 255, cv2.THRESH_BINARY_INV)
    
    # Morphological closing to connect broken parts of the characters
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
    closed = cv2.morphologyEx(binaried, cv2.MORPH_CLOSE, kernel)
    
    return closed

if __name__ == "__main__":
    # Example usage
    video_path = "../data/test.mp4"
    output_video_path = "../data/path_to_save_cut_video.mp4"
    
    # Define region of interest (ROI) (x, y, w, h)
    roi = (115, 110, 150, 55)
    
    texts = extract_text_from_video(video_path, roi)
    for t in texts:
        print(t)
