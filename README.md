# jetson_telloProject
## Instructions:
### 1.) go to wherever you keep your repos (or a new folder):
    cd path/to/local/repos
### 2.) clone this project: https://github.com/robagar/h264decoder
### 3.):
    cd h264decoder
    sudo apt install libswscale-dev libavcodec-dev libavutil-dev
    pip install .
### 4.) cd ..
### 5.) clone this project: https://github.com/dusty-nv/jetson-inference
    git clone --recursive --depth=1 https://github.com/dusty-nv/jetson-inference
    cd jetson-inference
### 1.) clone into THIS repo (jetson_telloProject) with --recursive flag
### 2.) cd jetson_telloProject
### 3.) clone this project: https://github.com/robagar/h264decoder

### 5.) sudo apt install libswscale-dev libavcodec-dev libavutil-dev
### 6.) pip install .
### 7.) cd ..
### 8.) clone this project: https://github.com/dusty-nv/jetson-inference
### 8.5):
    cd jetson-inference
    sudo vi Dockerfile
    #add the following lines toward the end of the file (but before the ENV line):
        # Install Docker inside the Docker container
        RUN apt-get update && apt-get install -y docker.io
    
### 9.) cd scripts
### 10.) make each .sh script executable
### 11.) echo "export ARCH=$(uname -m)" >> ~/.bashrc
### 12.) source ~/.bashrc
### 13.(optional):
    If you want to setup a jupyter system service (see: https://janakiev.com/blog/jupyter-systemd/),
    then read the SETUP.txt script and follow those instructions
### 14.):
    to run a jetson-inference docker container and mount some directories run:
    ./fProject_docker_run.sh
### 15.) Use the container to test your code.  Inside the container (root@user-desktop:/#):
    cd ..
    cd home
    cd jetson_telloProject
    python3 ece_drone_App.py

### 16.) Continue using jupyter lab view or change the code
