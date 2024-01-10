#!/bin/bash
set -e
docker pull docker pull sumit0058/codebuild-flask-app:latest
docker run -d -p 5000:5000 sumit0058/codebuild-flask-app:latest
