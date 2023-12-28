#!/bin/bash
#Essentials
apt-get update
apt-get install build-essential
apt-get install libffi-dev -y
#Jupyter
pip3 install --upgrade setuptools
pip3 install jupyterlab
#h264Decoder
apt install libswscale-dev libavcodec-dev libavutil-dev
pip3 install pybind11
cd /h264decoder
rm -rf build/
pip3 install .
#Jetson-Tello
pip3 install asyncio
pip3 install tello-asyncio
#facenet
cd /jetson-inference/tools
./download-models.sh
#get facenet
