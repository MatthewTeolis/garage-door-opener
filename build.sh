#!/usr/bin/env bash

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