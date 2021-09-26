import cv2
import sys
from changeable_params import *
from yolov3 import *

cnt = 0

def createTrackerByName(trackerType):
    '''
    This module instantiates a required object tracker and returns the same
    
    arguments:
    trackerType - name of the tracker to be instantiated
    
    returns:
    tracker - the instance of the tracker to be used for tracking
    '''
    # Create a tracker based on tracker name
    if trackerType == trackerTypes[0]:
        tracker = cv2.TrackerBoosting_create()
    elif trackerType == trackerTypes[1]: 
        tracker = cv2.TrackerMIL_create()
    elif trackerType == trackerTypes[2]:
        tracker = cv2.TrackerKCF_create()
    elif trackerType == trackerTypes[3]:
        tracker = cv2.TrackerTLD_create()
    elif trackerType == trackerTypes[4]:
        tracker = cv2.TrackerMedianFlow_create()
    elif trackerType == trackerTypes[5]:
        tracker = cv2.TrackerGOTURN_create()
    elif trackerType == trackerTypes[6]:
        tracker = cv2.TrackerMOSSE_create()
    elif trackerType == trackerTypes[7]:
        tracker = cv2.TrackerCSRT_create()
    return tracker





def initialise_MO_tracker(tracker_type, frame, bboxes):
    '''
    This module creates and initialises a multiobject tracker
    
    arguments:
    tracker_type - the name of the tracker to be used for tracking
    frame - the initial frame captured
    bboxes - the bounding boxes of the initial frame, as detected by YOLOv3
    
    returns:
    muliTracker - the multitracker object  
    '''
    # Create MultiTracker object
    multiTracker = cv2.MultiTracker_create()
    # Initialize MultiTracker 
    for bbox in bboxes:
        multiTracker.add(createTrackerByName(tracker_type), frame, bbox)
    return multiTracker





def init_frame():
    '''
    This module captures the first frame and passes it to the YOLOv3 detector
    which plots the first frame with detected objects
    
    arguments:
    none
    
    returns:
    multiTracker - the multiTracker object which will be used to track the objects
    '''
    
    # Reading in video
    video = cv2.VideoCapture(video_path)
    # Attempting to reopen the video if video not opened.
    if not video.isOpened():
        print ("Could not open video. Attempt to re-open")
        video.open(video_path)
    # Reading the first frame 
    ok, frame = video.read()
    if not ok:
        print ('Cannot read video')
        sys.exit()
    # Close remaining windows
    cv2.destroyAllWindows()
    video.release()
    
    #Detect objects and Plot bounding boxes
    bboxes = YOLO_detect_and_plot(frame)    
    #Initialise tracking
    multiTracker = initialise_MO_tracker(tracker_type,frame,bboxes)
    
    return multiTracker




def init_and_track(multiTracker):
    '''
    This module initialises the tracker and thereby continues tracking through the remaining frames
    
    arguments:
    multiTracker - the multiTracker object which will be used to track the objects
    
    returns:
    none
    ''' 
    #counts tracking failure
    cnt = 0

    # Reading video
    video = cv2.VideoCapture(video_path)

    # Attempting to reopen the video if video has not opened.
    if not video.isOpened():
        print ("Could not open video. Attempt to re-open")
        video.open(video_path)

    #Begin Tracking
    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break
        
        # Start timer
        timer = cv2.getTickCount()

        # get updated location of objects in subsequent frames
        ok, boxes = multiTracker.update(frame)
    
        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

        # draw tracked objects
        if ok:
            for i, newbox in enumerate(boxes):
                p1 = (int(newbox[0]), int(newbox[1]))
                p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    
        if not ok:
            cnt+=1
            if cnt>failure_thresh:  
                ###########   re-initialising the tracker  ###############
                bboxes = YOLO_detect(frame)
                multiTracker = initialise_MO_tracker(tracker_type,frame,bboxes)
                cnt = 0
            else:
                cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
    
        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        # show frame
        cv2.imshow('MultiTracker', frame)
  
        # quit on ESC button
        if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
            break
        
    cv2.destroyAllWindows()
    video.release()
