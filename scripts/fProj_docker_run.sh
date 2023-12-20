#!/bin/bash
#*Jetson_Inference Container
cd ../../jetson-inference 
docker/run.sh \
-v ${HOME}/repos/jetson_telloProject:/jetson-inference/build/aarch64/bin/jetson_telloProject \
-v ${HOME}/.local/bin:/home/.local/bin \
-v /usr/local/cuda-10.2/targets/aarch64-linux/lib:/usr/local/cuda-10.2/targets/aarch64-linux/lib \
-v /usr/lib/aarch64-linux-gnu:/usr/lib/aarch64-linux-gnu
#-v ${HOME}/.local/lib/python3.6/site-packages:/home/.local/lib/python3.6/site-packages \
#-r /bin/bash /home/jetson_telloProject/scripts/jupLab_run2.sh
# -v /bin:/bin \
# -v /dev:/dev \
# -v /lib:/lib \
# -v /run:/run \
# -v /etc:/etc \
# -v /var/run/docker.sock:/var/run/docker.sock \
# -v /usr/local/cuda-10.2/targets/aarch64-linux/lib:/usr/local/cuda-10.2/targets/aarch64-linux/lib
