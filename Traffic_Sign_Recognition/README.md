# Traffic Signal Recognition

#### For this era of the technologically advanced, the development of autonomous vehicles is a possible significant transportation option in the future. Autonomous vehicles, when driving on the road, need to detect the location of traffic signs and identify the current traffic signs and determine the direction or speed of travel. I want to make a traffic sign recognition system using to front camera of a vehicle to detect traffic signs and study how the system can be applied to autonomous vehicles
___
### Technologies and Tools
1. Object Detection
2. Yolov 5
3. CNN Model
4. VGG16 Model
5. Deep Learning
___
### Dataset
<https://www.kaggle.com/datasets/shanmukh05/traffic-sign-cropped>
___
### System structure and Experiment
* Classify of traffic signal
1. Transfer Learning
    1. Download photos for 42 types of traffic signals from Kaggle, but only choose 23 types of traffic singals from Taiwan usually used that which totals 15,120 photos
    2. Use the VGG16 Model to train my model

* Display accuracy of VGG16 Model
    1. Accuracy: 98.41%
    2. Training time: 4H 8M
    3. Epochs: Estimated training of 200 epochs, but model training in  epoch 22 has the best accuracy
### Epoch
![attachment1](/Traffic_Sign_Recognition/attachment/attachment1.jpg)
### Accuracy
![attachment2](/Traffic_Sign_Recognition/attachment/attachment2.jpg)

* System of traffic signal recognition
2. Training model of Yolov5 for detecting traffic signals
    1. Choose 21 types of traffic signals which total 4,457 photos
    2. Use LabelImg to draw a square mark for the traffic signal on each photo and save the format of the mark voc xml
    3.  Changed the format from vov xml to format of Yolov5
    4.  Train the Model Yolov5, the higher the better achieve an accuracy of mAP@0.5 0.7 and mAP@0.95 0.6 or above

* Display accuravy of Yolov5
    1. Accuracy: mAP@0.5 92.9% & mAP@0.5-0.95 73.7%
    2. Training time: 1H
    3. Epoch: 20 times 
![attachment3](/Traffic_Sign_Recognition/attachment/attachment3.jpg)
![attachment4](/Traffic_Sign_Recognition/attachment/attachment4.jpg)
![attachment5](/Traffic_Sign_Recognition/attachment/attachment5.jpg)
![attachment6](/Traffic_Sign_Recognition/attachment/attachment6.jpg)

3.  Set up a Django server and detect from AI

* Display for the result
![attachment7](/Traffic_Sign_Recognition/attachment/attachment7.jpg)
![attachment8](/Traffic_Sign_Recognition/attachment/attachment8.jpg)