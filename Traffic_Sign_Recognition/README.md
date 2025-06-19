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
![](https://github.com/calvink11/my_project/blob/master/Traffic_Sign_Recognition/attachment/attachment1.jpg?raw=true)
### Accuracy
![](https://github.com/calvink11/my_project/blob/master/Traffic_Sign_Recognition/attachment/attachment2.jpg?raw=true)

* System of traffic signal recognition
2. Training model of Yolov5 for detecting traffic signals
    1. Choose 21 types of traffic signals which total 4,457 photos
    2. Use LabelImg to draw a square mark for the traffic signal on each photo and save the format of the mark vcc xml
    3.  
