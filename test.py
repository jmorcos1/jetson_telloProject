#!/usr/bin/env python3
import asyncio
from jetson.inference import detectNet
import jetsonTelloVideo.jetson_tello.app as jt


#Face, Object Detectors:
face_detector = detectNet("facenet", threshold=0.5)
object_detector = detectNet("ssd-mobilenet-v2", threshold=0.5)
