Get Datasets: https://storage.googleapis.com/openimages/web/index.html
OIDv4: https://github.com/EscVM/OIDv4_ToolKit
CVAT: https://www.cvat.ai/

Steps:
*pip install -r the requirements.txt of OIDv4
*pip install ultalytics
*Run OIDv4´s main.py with the following command 
    "Python main.py downloader --classes (Classes separeted by a space) --type_csv train --multiclass --limit (Number of pics to download)"
    Ex: py main.py downloader --classes Hat --type_csv train --limit 10
*Move images to Datasets/dataset/images
*Upload the images to CVAT and create the Labels with YOLO format.
*Move labels to Datasets/dataset/labels
*Give and absolute path of the dataset (datasets\dataset\) to the config.yaml 
*Add the classes to the config.yaml that you selected on CVAT specifying their key and name.
    Ex: 
        # Classes
            names:
            0: Hat 
*Run the object_training.py and wait for it to finish (Will take a while)

Tutorials:
OIDv4 Download Datasets: https://www.youtube.com/watch?v=dLSFX6Jq-F0&list=PLTXKFRNEJgfnBBKwST1bIdkFZRMJ9xM8A&index=4
YOLOv8 Training: https://www.youtube.com/watch?v=m9fH9OWn8YM&list=LL&index=3&t=1515s
