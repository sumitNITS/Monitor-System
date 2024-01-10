#!/bin/bash
set -e
sudo docker pull docker pull sumit0058/codebuild-flask-app:latest
sudo docker run -d -p 5000:5000 sumit0058/codebuild-flask-app:latest
