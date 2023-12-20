#!/bin/bash
#*JETSON_ML Container:
sudo docker run -it --rm --runtime nvidia --network host \
	-v /bin:/bin \
	-v /dev:/dev \
	-v /lib:/lib \
	-v /usr:/usr \
	-v /run:/run \
    -v /etc:/etc \
    -v ${HOME}:/home \
	--privileged \
	--pid=host \
	nvcr.io/nvidia/l4t-ml:r32.7.1-py3
