#!/bin/bash
#*Jetson_Inference Container
cd ../jetson-inference 
docker/run.sh \
-v ${HOME}:/home
#-r /bin/bash /home/jetson_telloProject/scripts/jupLab_run2.sh
# -v /bin:/bin \
# -v /dev:/dev \
# -v /lib:/lib \
# -v /run:/run \
# -v /etc:/etc \
# -v /var/run/docker.sock:/var/run/docker.sock \
# -v /usr/local/cuda-10.2/targets/aarch64-linux/lib:/usr/local/cuda-10.2/targets/aarch64-linux/lib
