#!/bin/bash
cd /home/user1/src/Firmware
roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557" &
# rosrun topic_tools throttle messages /mavros/local_position/pose 2.0 &
rosrun distance_xy distance.py &
wait &
make px4_sitl gazebo_iris PX4_SIM_SPEED_FACTOR=10
