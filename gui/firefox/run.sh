#!/bin/bash

# run socat for X (mac only)
if [ $(ps -ef | grep socat | grep "LISTE[N]"; echo ${?}) -ne 0 ]; then
    socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"${DISPLAY}\" &
    pid=$(ps -ef | grep socat | grep "LISTE[N]" | awk '{print $2}')
fi

# set display
DISPLAY="$(ipconfig getifaddr en0):0"
docker run --rm=true -e DISPLAY=${DISPLAY} --net=host firefox
kill ${pid}
