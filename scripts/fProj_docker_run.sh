#!/bin/bash
#*Jetson_Inference Container
../jetson-inference/docker/run.sh \
-v /home/ece498:/home \
-v /bin:/bin \
-v /dev:/dev \
-v /lib:/lib \
-v /usr:/usr \
-v /run:/run
#*_JETSON_ML Container:
#Option?
# sudo docker run -it --rm --runtime nvidia --network host \
# 	-v /bin:/bin \
# 	-v /dev:/dev \
# 	-v /lib:/lib \
# 	-v /usr:/usr \
# 	-v /run:/run \
# 	-v /home/ece498:/home \
# 	--privileged \
# 	--pid=host \
# 	nvcr.io/nvidia/l4t-ml:r32.7.1-py3
