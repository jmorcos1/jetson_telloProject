#!/bin/bash
#Jetson-Tello
pip3 install asyncio
pip3 install tello-asyncio
pip3 install Pillow
#facenet
cd ../../jetson-inference/tools
./download-models.sh
#get facenet and others