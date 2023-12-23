# jetson_telloProject
## Instructions:
### 0.0) instally stuff:
    #SOURCE:https://pyimagesearch.com/2020/03/25/how-to-configure-your-nvidia-jetson-nano-for-computer-vision-and-deep-learning/
    #Install system-level dependencies
    sudo apt-get update && sudo apt-get upgrade
    sudo apt-get install git cmake
    sudo apt-get install libatlas-base-dev gfortran
    sudo apt-get install libhdf5-serial-dev hdf5-tools
    sudo apt-get install python3-dev
    sudo apt-get install nano locate

    #SciPy
    sudo apt-get install libfreetype6-dev python3-setuptools
    sudo apt-get install protobuf-compiler libprotobuf-dev openssl
    sudo apt-get install libssl-dev libcurl4-openssl-dev
    sudo apt-get install cython3

    #XML stuff cor TensorFlow
    sudo apt-get install libxml2-dev libxslt1-dev

    #Update CMake
    wget http://www.cmake.org/files/v3.13/cmake-3.13.0.tar.gz
    tar xpvf cmake-3.13.0.tar.gz cmake-3.13.0/
    cd cmake-3.13.0/
    ./bootstrap --system-curl
    make -j4

    #update bash profile
    echo 'export PATH=/home/nvidia/cmake-3.13.0/bin/:$PATH' >> ~/.bashrc
    source ~/.bashrc

    #OpenCV system-level dependencies
    sudo apt-get install build-essential pkg-config
    sudo apt-get install libtbb2 libtbb-dev

    #codecs and Image libraries
    sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
    sudo apt-get install libxvidcore-dev libavresample-dev
    sudo apt-get install libtiff-dev libjpeg-dev libpng-dev

    #GUI libraries
    sudo apt-get install python-tk libgtk-3-dev
    sudo apt-get install libcanberra-gtk-module libcanberra-gtk3-modul

    #USB webcam stuff
    sudo apt-get install libv4l-dev libdc1394-22-dev
    #first run 'sudo apt-get install python-numpy python3-numpy'
    #pip3 install cython
    #pip3 install numpy==1.13.3
    #pip3 install -U pandas
    
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

### 17.) If you want to buld from source:
    cd jetson-inference
    mkdir build
    cd build
    cmake ../
    make -j$(nproc)
    sudo make install
    sudo ldconfig

