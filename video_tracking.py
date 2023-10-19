from ultralytics import YOLO
import cv2
import time

# Load a model
model = YOLO('runs\detect\\train\weights\\best.pt')
#Video Source
src = ""

#Load Video
cap = cv2.VideoCapture(src)

ret = True

now = time.time()

frame_id = 0

#While getting frames from the video
while ret:
    frame_id += 1
    
    #Read frame
    ret, frame = cap.read()
    
    #Resize screen
    height, width, channels = frame.shape
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', width, height)
    
    #Detect and track object
    results = model.track(frame, persist=True)
    
    #Plot detections
    frame_ = results[0].plot()
    
    #Calculate frames
    elapsed_time = time.time() - now
    fps = frame_id / elapsed_time
    
    #Adds on screen the number of objects detected
    cv2.putText(frame_, str(f"Objetos en pantalla: {len(results[0])}"), (0,50), cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),2)
    #Adds on screen the fps
    cv2.putText(frame_, "FPS: " + str(fps), (0, 90), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 2)
    
    #Visualize
    cv2.imshow("frame", frame_)
    
    #Stops of user clicks letter 'q'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    