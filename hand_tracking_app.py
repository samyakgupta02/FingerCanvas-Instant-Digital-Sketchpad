import cv2
from handTracker import HandTracker

def main():
    # Initialize the hand tracker
    detector = HandTracker()

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        # Find hands in the frame
        frame = detector.findHands(frame)

        # Display the frame
        cv2.imshow('Hand Tracking', frame)

        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
