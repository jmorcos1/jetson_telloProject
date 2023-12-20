# jetson_telloProject
## Instructions:
### 0.0) instally stuff:
    pip3 install cython
    pip3 install numpy
    pip3 install -U pandas
### 0.1) do this (https://github.com/dusty-nv/jetson-containers/blob/master/docs/setup.md):
### Add "default-runtime": "nvidia" to your /etc/docker/daemon.json configuration file before attempting to build the containers:
    {
        "runtimes": {
            "nvidia": {
                "path": "nvidia-container-runtime",
                "runtimeArgs": []
            }
        },

        "default-runtime": "nvidia"
    }
### 1.) Create a repos folder in home directory:
    cd ~
    mkdir repos
    # or if you already have this folder existing, great:
    cd ~/repos
### 2.) clone this project: https://github.com/robagar/h264decoder
### 3.):
    cd h264decoder
    sudo apt install libswscale-dev libavcodec-dev libavutil-dev
    pip3 install .
### 4.) cd ..
### 5.) clone this project: https://github.com/dusty-nv/jetson-inference
    git clone --recursive --depth=1 https://github.com/dusty-nv/jetson-inference
    cd jetson-inference
### 6.) Don't build from source, we're gonna use the docker container
### 7.) cd ..
### 8.) clone into THIS repo (jetson_telloProject) with --recursive flag
    #ssh
    git clone --recursive --depth=1 git@github.com:jmorcos1/jetson_telloProject.git
    #https
    git clone --recursive --depth=1 https://github.com/jmorcos1/jetson_telloProject.git
### 9.) cd jetson_telloProject/scripts    
### 10.) make each .sh script executable (chmod +x <script.sh)
### 11.) echo "export ARCH=$(uname -m)" >> ~/.bashrc
### 12.) source ~/.bashrc
### 13.(recommended):
    If you want to setup a jupyter system service (see: https://janakiev.com/blog/jupyter-systemd/),
    then read SETUP.txt inside scripts and follow those instructions
### 14.) to run a jetson-inference docker container and mount some directories run (from scripts folder):
    ./fProject_docker_run.sh
### 15.) Inside the container (root@user-desktop:/#):
    cd jetson_telloProject/scripts
    ./jupLab_run2.sh
    # will take some time because it needs to install jupyterlab in container...
### 16.) Continue using jupyter lab in the container to run, test, edit code
