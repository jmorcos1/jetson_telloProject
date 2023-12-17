#!/bin/bash
echo "ExecStart=${PWD}/jupLab_run.sh" > ES_path
sudo sed -ri "s#.*ExecStart=.*#$(cat ES_path)#g" ./jupyter.service
sudo cp ./jupyter.service /etc/systemd/system/
