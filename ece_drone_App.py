#!/usr/bin/env python3
import asyncio
from jetson.inference import detectNet
from jetson.utils import videoOutput
import jetsonTelloVideo.jetson_tello.app as jt

# Output streaming display
display = videoOutput("rtp://192.168.1.13:1234")
display2 = videoOutput("videos/droneTest1.mp4")
print('Created RTP Stream')

# Face, Object Detectors:
#face_detector = detectNet("facenet", threshold=0.5)
#face_detector.SetTrackingEnabled(True)
#face_detector.SetTrackingParams(minFrames=3, dropFrames=15, overlapThreshold=0.5)

object_detector = detectNet("ssd-mobilenet-v2", threshold=0.5)
object_detector.SetTrackingEnabled(True)
object_detector.SetTrackingParams(minFrames=3, dropFrames=15, overlapThreshold=0.5)
print('Created Object detector')

#print(object_detector.GetTrackingParams())


# Frames and data Dictionary
frameData = {}

#*Detection Functions
def detect_objects(cuda):
    '''
    Detect objects in a cuda object
    '''
    print('[DETECT-Objects]')
    print('------------------------')
    object_detections = object_detector.Detect(cuda)
    #display.Render(cuda)
    #display.SetStatus("Object Detection | Network {:.0f} FPS".format(object_detector.GetNetworkFPS()))
    print('objects:')
    for d in object_detections:
        print(d)
    return object_detections

def detect_faces(cuda):
    '''
    Detect faces in a cuda object
    '''
    print('[DETECT-Faces]')
    print('------------------------')
    #import pdb; pdb.set_trace()
    face_detections = face_detector.Detect(cuda)
    #display.Render(cuda)
    #display.SetStatus("Object Detection | Network {:.0f} FPS".format(face_detector.GetNetworkFPS()))
    print('faces:')
    for d in face_detections:
        print(d)
    return face_detections

def process_frame_action(drone, frame, cuda):
    '''
    Define what to do with each processed frame (cuda) from drone camera
    '''
    # A frame with a cudo object is ready to be processed
    print('Frame:',frame.number, '-', frame.width, 'x', frame.height)
    frameData[frame] = []
    
    # Do stuff with the cuda
    ### Detect Objects
    frameData[frame].append(detect_objects(cuda))
    display.Render(cuda)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(object_detector.GetNetworkFPS()))
    display2.Render(cuda)
    sdisplay.SetStatus("Object Detection | Network {:.0f} FPS".format(object_detector.GetNetworkFPS()))
    
    # frameData[frame].append(detect_faces(cuda))
    # display.Render(cuda)
    # display.SetStatus("Face Detection | Network {:.0f} FPS".format(face_detector.GetNetworkFPS()))
    
    
#*Drone Functions (Async)
async def fly(drone):
    '''
    basic fly sequence
    '''
    await drone.takeoff()
    print('We Are Flying!!!')
    await asyncio.sleep(3)
    await drone.move_up(20)
    
    for i in range(8):
        await asyncio.sleep(10)
        print('Turning!')
        print(len(frameData))
        await drone.turn_clockwise(45)
    await asyncio.sleep(3)
    await drone.land()

#App
def main():
    jt.run_jetson_tello_app(fly, process_frame=process_frame_action)
    
if __name__ == "__main__":
    main()