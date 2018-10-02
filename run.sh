#!/usr/bin/env bash

docker run -itd --name garage-door-opener --restart unless-stopped --privileged -p 8081:8081 garage-door-opener