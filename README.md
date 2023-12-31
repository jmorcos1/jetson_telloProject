# jetson_telloProject
    '''
    This repo contains a fork of jetson_tello and builds upon it
    2 goals:
    1.) make it work on (my) jetson
    2.) make it do something cool for my project

    Main reason for Forking:
    Combining (and patching) 2 repos from @robagar

    > ece_drone_App.py
        The main project app
    > project.ipynb
        The main project notebook, for testing, training, etc.
    > my-dection.py
        Example from https://github.com/dusty-nv/jetson-inference/blob/master/docs/detectnet-example-2.md
    > test.py
        Make sure you can import and run the basics

    
    See below for environment setup instructions to 'build' and run the project 
    '''
## Instructions:
### NOTE: start here if you just got a new Jetson Nano Developer Kit or you want to (re)FLASH your SD card image
### 0.0) Flashing Jetpack 4.6.4:
    #0). have a 64 GB SD and a PC with an SD card reader
    #1.) Go to https://developer.nvidia.com/jetpack-sdk-464 and download the Jetson Nano Developer Kit SD card Image (4.6.4) --it's a big file
    #2.) Follow these instructions: https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write
    #2.1) https://www.sdcard.org/downloads/formatter/sd-memory-card-formatter-for-windows-download/
![image](https://github.com/jmorcos1/jetson_telloProject/assets/32444584/f62b508d-8168-43ce-9227-a2cc3019b86f)
    #2.2) https://etcher.balena.io/
![image](https://github.com/jmorcos1/jetson_telloProject/assets/32444584/978f38df-7fdc-4ca0-b631-c6bcbc884b41)
![image](https://github.com/jmorcos1/jetson_telloProject/assets/32444584/40f21afd-286b-4e08-b38e-f7fc205388d5)

    #NOTE: for some it may be easier to do the first boot with HDMI connected to monitor and keyboard/mouse connected to jetson
    #SEE: https://www.youtube.com/watch?v=uvU8AXY1170
    #3.) Once the SD card is ready, insert it and set up your jetson in headless mode:
    # Insert the SD card into the slot on the Jetson
    # Insert the Power cable to the jetson to power it on (give it a minute to boot up)
    # Connect micro-sd on jetson to USB on your PC
    # Open up a Serial Terminal Connection to the Nano using the correct COM port and an app such as Putty or Tera Term
    #Review and accept NVIDIA Jetson software EULA
    #Select system language, keyboard layout, and time zone
    #Create username, password, and computer name
    #Select APP partition size—it is recommended to use the max size suggested

    #Set up network of choice (that is on you)

    #Now open your ssh tunnel to your jetson (not COM/Serial, SSH!)
    # do this using the network you set up, or the l4tbridge (192.168.55.1) usb

    #Set the swap Space
    # Disable ZRAM:
    sudo systemctl disable nvzramconfig

    # Create 4GB swap file
    sudo fallocate -l 4G /mnt/4GB.swap
    sudo chmod 600 /mnt/4GB.swap
    sudo mkswap /mnt/4GB.swap

    # Append the following line to /etc/fstab
    sudo su
    echo "/mnt/4GB.swap swap swap defaults 0 0" >> /etc/fstab
    exit

    # REBOOT!

### NOTE: start here if you have a pretty freshly flashed jetson and/or you want to make sure you have the essentials
### 0.1) instally stuff:
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

    #pip and pip3
    sudo apt install python3-pip
    sudo apt-get install python-pip

    #pybind11
    pip install pybind11
    pip3 install pybind11

    # More Essentials
    sudo apt-get update
    sudo apt-get install build-essential
    sudo apt-get install libffi-dev -y
    
    # JupyterLab
    pip3 install --upgrade setuptools
    pip3 install pyzmq==20.0.0
    pip3 install packaging
    pip3 install jupyterlab

    
### NOTE: start here if you are first cloning the project    
### 0.2) do this (https://github.com/dusty-nv/jetson-containers/blob/master/docs/setup.md):
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

    #!!! Pybind 11
    #you need to find the pybind 11 directory
    #I found it by:
    pip show pybind11
    #but you need to get all the way into the subdirectory where the cmake files are.  In my case it is this:
    /usr/local/lib/python3.6/dist-packages/pybind11/share/cmake/pybind11

    #copy that directory for you. then edit the CMakeLists.txt file
    #around Line 28, before the find_package(pybind11) line, add this line
    set(pybind11_DIR /usr/local/lib/python3.6/dist-packages/pybind11/share/cmake/pybind11)
    #with the directory for your system

    #Save that and Now we are ready
    pip3 install .
    
### 4.) cd ..
### 5.) clone this project: https://github.com/dusty-nv/jetson-inference
    #https
    git clone --recursive --depth=1 https://github.com/dusty-nv/jetson-inference
    #ssh
    git clone --recursive --depth=1 git@github.com:dusty-nv/jetson-inference.git
    
    
### 6.) Don't build from source, we're gonna use the docker container
### 7.) #you should still be in the repos directory
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
    # If you want to setup a jupyter system service (see: https://janakiev.com/blog/jupyter-systemd/),
    # then read SETUP.txt inside scripts and follow those instructions
    # after running that, you can open the jupyterlab in a browser and work in there from then on

### NOTE: start here (skip all previous) if this is not your initial setup
### 14.) to run a jetson-inference docker container and mount some directories:
    cd jetson_telloProject/scripts
    ./fProject_docker_run.sh

### NOTE: If not using the container, see Appendix B
### 15.) Inside the container (root@user-desktop:/#) [or on your jetson if not using container]:
    cd /jetson_telloProject/scripts
    ./in_container_setup.sh
    # it will take some time because it needs to install a bunch of things including jupyterlab and h264decoder inside the container...
    # monitor loosley; it will prompt you to say yes [Y] for a couple of install steps toward the end
    
    # at the end it will prompt you to download ML netowrks
    # Download any you wish (they will download into networks folder(s) in jetson-inference)
    # ! Make Sure to download the FaceNet and SSD-Mobilenet-v2 options:
    ![image](https://github.com/jmorcos1/jetson_telloProject/assets/32444584/0b3a1f72-dc9f-4e54-a08f-1116a3140ce4)
    ![image](https://github.com/jmorcos1/jetson_telloProject/assets/32444584/1195621c-e490-4b92-b67f-9788be0f909e)

    #if you have all the networks you need, just select Quit

    #to download more networks (from inside container):
    cd /jetson-inference/tools
    ./download-models.sh

    
### 16.) Inside the container (root@user-desktop:/#), run a jupyterlab server:
    cd /jetson_telloProject/scripts
    ./jupLab_run2.sh
    # open the jupyterlab link in a browser
    
### 17.) Continue using jupyter lab in the container to run, test, edit code (and outside the container at the same time ;)
    # using this method you can have your main ssh tunnel running on your host pc
    # plus a constantly running jupyter lab server (see step 13)
    # and a jupyterlab server running inside the container (use this to run and test code)

#
#

### Appendix I.) Connecting the drone to Jetson:
    #have a wifi dongle hooked up
    #turn on tello
    #do this from outside container:
    sudo nmcli device wifi list
    sudo nmcli device wifi connect <TELLO-****>

### Appendix A.) Testing Example code:
    # Use test.py to check that things can import correctly and detectnet is working
    # ece_drone_App.py is a work in progress app that requires the drone connected to jetson by wifi
    #    More info on the repo I forked this from
    
    #
    #
    
    #test.py:
    #!/usr/bin/env python3
    import asyncio
    from jetson.inference import detectNet
    import jetsonTelloVideo.jetson_tello.app as jt

    #Face, Object Detectors:
    face_detector = detectNet("facenet", threshold=0.5)
    object_detector = detectNet("ssd-mobilenet-v2", threshold=0.5)


### Appendix B.) If you want to buld from source (on device, not inside any containers):
    cd jetson-inference
    mkdir build
    cd build
    cmake ../
    make -j$(nproc)
    sudo make install
    sudo ldconfig

### 15.B.) Not using container:
    cd /jetson_telloProject/scripts
    ./no_container_setup.sh
    # Download any ML Networks you wish (they will download into networks folder(s) in jetson-inference)
    # ! Make Sure to download the FaceNet and SSD-Mobilenet-v2 options:
    ![image](https://github.com/jmorcos1/jetson_telloProject/assets/32444584/0b3a1f72-dc9f-4e54-a08f-1116a3140ce4)
    ![image](https://github.com/jmorcos1/jetson_telloProject/assets/32444584/1195621c-e490-4b92-b67f-9788be0f909e)

    #if you have all the networks you need, just select Quit

    #to download more networks (from inside container):
    cd /jetson-inference/tools
    ./download-models.sh
    
### 17.B) Continue using jupyter service to run, test, edit code
    # using this method you can have your main ssh tunnel running on your host pc
    # plus a constantly running jupyter lab server (see step 13)
    # No need for container, doing everything directly on the jetson
