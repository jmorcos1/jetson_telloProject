import asyncio
import jetson_inference
import jetsonTello.jetson_tello.app as jt

#Face, Object Detectors:
face_detector = jetson_inference.detectNet("facenet", threshold=0.5)
object_detector = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

#Frames and data Dictionary
frameData = {}

def detect_faces(cuda):
    '''
    Detect faces in a cuda object
    '''
    print('[DETECT-Faces]')
    print('------------------------')
    face_detections = face_detector.Detect(cuda)
    print('faces:')
    for d in face_detections:
        print(d)
    return face_detections

def detect_objects(cuda):
    '''
    Detect objects in a cuda object
    '''
    print('[DETECT-Objects]')
    print('------------------------')
    object_detections = object_detector.Detect(cuda)
    print('objects:')
    for d in object_detections:
        print(d)
    return object_detections
        
def process_frame_action(drone, frame, cuda):
    '''
    Define what to do with each processed frame (cuda) from drone camera
    '''
    # A frame with a cudo object is ready to be processed
    print('Frame:',frame)
    frameData[frame] = []
    
    # Do stuff with the cuda
    frameData[frame].append(detect_faces(cuda))
    frameData[frame].append(detect_objects(cuda))
    

async def fly(drone):
    '''
    basic fly sequence
    '''
    await drone.takeoff()
    for i in range(4):
        print(frameData.len())
        await drone.turn_clockwise(90)
        await asyncio.sleep(3)
    await drone.land()