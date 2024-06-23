#!/bin/bash
source install/local_setup.bash && \
    export GSCAM_CONFIG='udpsrc port=5000 caps="application/x-rtp" ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert' && \
    ros2 run gscam2 gscam_main --ros-args -p sync_sink:=true -p preroll:=true