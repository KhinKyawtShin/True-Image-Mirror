import cv2

def show_webcam():
    # 0 is the default camera, 1 is extranal camera, 2 is second external camera
    cam = cv2.VideoCapture(0)
    cv2.namedWindow('my webcam', cv2.WINDOW_NORMAL)
    while True:
        # Read a frame from the webcam
        ret, frame = cam.read()
        if not ret: 
            break
        # Display the frame in a window named 'my webcam'
        cv2.imshow('my webcam', frame)
        # Break the loop if the 'Esc' key (ASCII 27) is pressed
        if cv2.waitKey(1) == 27: 
            break
    # Release the webcam and close the window
    cam.release()
    cv2.destroyAllWindows()

def main():
    # Call the show_webcam function
    show_webcam()

if __name__ == '__main__':
    # Run the main function if this script is executed
    main()