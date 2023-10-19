from ultralytics import YOLO

#Loads model
model = YOLO('runs\detect\\train\weights\\best.pt')

#Detects classes on screen and saves the result somewhere
test = model.predict("yolo\\training\\test.jpg", save=True, save_txt=True)

#Prints number of detections
print(len(test[0]))