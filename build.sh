#!/usr/bin/env bash

#DOCKER_IMAGE_NAME="garage-door-opener"
#
#if [[ "$(docker images -q ${DOCKER_IMAGE_NAME} 2> /dev/null)" != "" ]]; then
#  echo "Docker image exists..."
#  echo "Removing existing image..."
#  docker image rm ${DOCKER_IMAGE_NAME}
#  echo "Done."
#fi

if [ ! -f .config.yaml ]; then
  echo "Config file not found!"
  read -p "Enter 'authkey': " authkey
  read -p "Enter 'port': " port
  cat <<EOF > .config.yaml
---
authkey: ${authkey}
port: ${port}
EOF
fi

echo "Building new image..."
docker build -t garage-door-opener .
echo "Done."