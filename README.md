# TrackEA : An Enhanced Object Tracking Algorithm

Pronounced : trachea (truh·**kee**·uh)  
  
  
This is an implementation of an enhanced object tracking algorithm that uses an improvised re-initialisation strategy for more astute tracking.  
Please see the presentation.pdf for more details.  

## How to use

### Directory Structure

```
TrackEA
│   
└─── README.md
|
└─── install.txt : package requirements 
|
└─── Tutorial Notebooks/ : Background and Brief Tutorial 
|    └─── Presentation.pdf
|    └─── Single Object Tracking.ipynb
|    └─── Detection and Multi-Object Tracking.ipynb
|    └─── Explanatory Notebook (Final).ipynb
|
└─── cfg/ : yolov3 layer configurations
|    └─── yolov3.cfg
|
└─── data/ : COCO dataset object categories
|    └─── coco.names
|
└─── Videos/ : Videos in which Objects are to be Tracked 
|    └─── video*.mp4
|
└─── weights/ : pretained network weights  
|    └─── yolov3.weights
|
└─── src/
|    └─── darknet.py : implementation of the Network in Pytorch
|    └─── changeable_params.py : parameters which can be changed before tracking 
|    └─── multi_obj_tracker.py : module for tracking multiple objects 
|    └─── run.py : module which drives the software
|    └─── utils.py  : utility functions for the driver code
|    └─── yolov3.py : code to draw bounding boxes for ROI selection   
```

### Dependencies
The broad requirements for running the code are:
* pytorch=1.8.1
* opencv=4.5.0
* matplotlib=3.3.4   
(Note that the MultiObject Tracker modules are deprecated in OpenCV 4.5.1 onwards)
  
If creating a new environment, please use the install.txt file.  

### Instructions for Use:
1. Clone the repository using ```git clone https://github.com/sudipto-g/TrackEA```
2. Activate the necessary environment
3. In the root of the directory, enter the following: ```cd src && python run.py```  
  
    
    
The run.py file contains the main script that drives the code.  
The changeable_params.py file contains the file where contents may be modified - mainly the path to the video, type of tracker etc.  
