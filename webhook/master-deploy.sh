#!/bin/bash

echo "Deploying develop branch at $(date)" >> /home/coffeecup/deployment_log.txt

cd /home/coffeecup/

git pull origin master

service gunicorn restart

