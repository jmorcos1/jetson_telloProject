#!/usr/bin/env python3
from jetson.inference import detectNet
from jetson.utils import videoSource, videoOutput


net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("/dev/video0")
display = videoOutput("rtp://192.168.1.13:1234")
#Check IP address^

net.SetTrackingEnabled(True)
net.SetTrackingParams(minFrames=3, dropFrames=15, overlapThreshold=0.5)