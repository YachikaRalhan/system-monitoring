#!/bin/bash

echo "removing old container ..."
sudo docker ps | grep flask-image | xargs sudo docker rm -f

echo "removing old image ..."
sudo docker images| grep flask-image | xargs sudo docker rmi

echo "recreating the flask-image ..."
sudo docker build -t flask-image:latest .

echo "running images ..."
sudo docker-compose up 

curl http://localhost:8089/health