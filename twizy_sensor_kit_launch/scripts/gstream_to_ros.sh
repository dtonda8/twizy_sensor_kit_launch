#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <port>"
    exit 1
fi

source install/local_setup.bash && \
    export GSCAM_CONFIG='udpsrc port='"$1"' caps="application/x-rtp" ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert' && \
    ros2 run gscam2 gscam_main --ros-args -p sync_sink:=true -p preroll:=true -r /image_raw:=/image0_raw