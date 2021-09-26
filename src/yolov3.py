import cv2
from utils import *
from darknet import Darknet
import sys

cfg_file = '../cfg/yolov3.cfg'
weight_file = '../weights/yolov3.weights'
namesfile = '../data/coco.names'

# Load the network architecture
m = Darknet(cfg_file)

# Load the pre-trained weights
m.load_weights(weight_file)

# Load the COCO object classes
class_names = load_class_names(namesfile)

# Sets the NMS threshold
nms_thresh = 0.6

# Set the IOU threshold
iou_thresh = 0.4



def YOLO_detect(original_image_frame):
    
    ''' This module detects the objects in the provided image frame, 
    by finding coordinates of bounding boxes
    
    arguments:
    original_image_frame - the initial frame where objects are to be detected
    
    returns:
    bboxes - the coordinates of the bounding boxes for multiple objects in the frame
    '''
    
    original_image_frame = cv2.cvtColor(original_image_frame, cv2.COLOR_BGR2RGB)   
    resized_image = cv2.resize(original_image_frame, (m.width, m.height))
    boxes = detect_objects(m,resized_image,iou_thresh,nms_thresh)
    bboxes = get_box_coordinates(original_image_frame, boxes, class_names, plot_labels=True)
    return bboxes






def YOLO_detect_and_plot(original_image_frame):
    
    ''' This module detects the objects in the provided image frame using the YOLO_detect module
    and plots the bounding boxes around the detected objects in the frame
    
    arguments:
    original_image_frame - the initial frame where objects are to be detected
    
    returns:
    bboxes - the coordinates of the bounding boxes for multiple objects in the frame
    '''
    
    original_image_frame = cv2.cvtColor(original_image_frame, cv2.COLOR_BGR2RGB)   
    resized_image = cv2.resize(original_image_frame, (m.width, m.height))
    boxes = detect_objects(m,resized_image,iou_thresh,nms_thresh)
    print_objects(boxes, class_names)
    plot_boxes(original_image_frame, boxes, class_names, plot_labels = True)
    bboxes = get_box_coordinates(original_image_frame, boxes, class_names, plot_labels=True)
    return bboxes
