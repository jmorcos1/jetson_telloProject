# jetson_telloProject
## Instructions:
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
### 6.) Don't build from source, we're gonna us the docker container
### 7.) inside jetson-inference:
-> go to docker folder, edit run.sh, line #64:
    ### DOCKER_ROOT="/jetson-inference"	# where the project resides inside docker
    DOCKER_ROOT="/home/jetson-inference"	# where the project resides inside docker
### 8.) cd ..
### 9.) clone into THIS repo (jetson_telloProject) with --recursive flag
### 10.) cd jetson_telloProject/scripts    
### 11.) make each .sh script executable (chmod +x <script.sh)
### 12.) echo "export ARCH=$(uname -m)" >> ~/.bashrc
### 13.) source ~/.bashrc
### 14.(recommended):
    If you want to setup a jupyter system service (see: https://janakiev.com/blog/jupyter-systemd/),
    then read SETUP.txt inside scripts and follow those instructions
### 15.) to run a jetson-inference docker container and mount some directories run (from scripts folder):
    ./fProject_docker_run.sh
### 16.) Use the container to test your code.  Inside the container (root@user-desktop:/#):
    cd ..
    cd home
    cd jetson_telloProject
    python3 ece_drone_App.py

### 16.) Continue using jupyter lab view or change the code, use the container for running and testing the code
