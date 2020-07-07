# PX4 Simulation for sUAS Object Detection

This repository holds the supporting files needed to adjust the camera angles and run tests in a Gazebo simulation. This work supports the publication by Cadet Curtis Manore, Mr. Pratheek Manjunath, and Dr. Dominic Larkin titled "Maximizing Object Detection Using sUAS."

## Dependencies

* [Gazebo Simulation Environment](https://github.com/osrf/gazebo)
* [ROS](https://www.ros.org/install/)
* [MAVROS](https://dev.px4.io/v1.9.0/en/ros/mavros_installation.html)
* [QGroundControl](https://docs.qgroundcontrol.com/en/getting_started/download_and_install.html#ubuntu)
* [Darknet](https://github.com/pjreddie/darknet)
* [PX4 Firmware](https://github.com/PX4/Firmware)
  * **Note**: PX4 sitl_gazebo must be installed seperately and the folder replaced in the PX4 Firmware/Tools directory. sitl_gazebo GitHub repository located [here](https://github.com/PX4/sitl_gazebo).

## Modifications to PX4 Firmware

Within the [modified_px4_files](https://github.com/cmanore25/suas_px4sim2/tree/master/modified_px4_files) directory is the files modified to change the camera angle and object tilt angle in the Gazebo Simulation.
