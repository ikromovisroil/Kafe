#!/bin/bash
mkdir -p /docker/volume/canteen/media
docker container stop canteen
docker rm canteen
docker rmi canteen-image
docker build -t canteen-image .
docker run \
--name canteen \
-v /docker/volume/canteen/media:/home/app/webapp/media \
--net tashmediatrans-network \
-p 2003:2003 \
-d \
canteen-image