# TrackEA : An Enhanced Object Tracking Algorithm

Pronounced : trachea (truh·**kee**·uh)  
  
  
This is an implementation of an enhanced object tracking algorithm that uses an improvised re-initialisation strategy for more astute tracking.  
Please see the presentation.pdf for more details.  

## How to use

### Directory Structure

```
TrackEA
│   README.md
└───cfg
|   | yolov3.cfg
└───data
|   | coco.names
└───Prelims
|   | Presentation.pdf
|   | Tutorial Notebook for Object Tracking.ipynb
└───Videos
|   | videos.mp4
└───weights
|   | yolov3.weights
|   changeable_params.py  
|   darknet.py  
|   Detection and Tracking (Multi Object Tracker).ipynb  
|   Explanatory Notebook.ipynb  
|   install.txt  
|   multi_obj_tracker.py  
|   README.md  
|   run.py  
|   tracking.gif  
|   utils.py  
|   yolov3.py    
```

### Dependencies
The broad requirements for running the code are:
* pytorch=1.8.1
* opencv=4.5.0
* matplotlib=3.3.4   
(Note that the MultiObject Tracker modules are depreciated in OpenCV 4.5.1 onwards)
  
If creating a new environment, please use the install.txt file.  

### Running
The run.py file contains the main script that drives the code.  
The changeable_params.py file contains the file where contents may be modified - mainly the path to the video, type of tracker etc.
