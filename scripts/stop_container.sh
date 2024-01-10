#!/bin/bash
set -e
containerID = docker ps | awk -F " " '{print $1}'
sudo docker rm -f $containerID
