#!/usr/bin/env python
import math
import csv
import rospy
from geometry_msgs.msg import PoseStamped

distance_xy = 0

def writeToCSV(distance):
    with open('distance90deg.csv', 'a+') as write_obj:
        thewriter = csv.writer(write_obj)
        thewriter.writerow([distance])

def callback(msg):
    global distance_xy
    hydrantLocation = [0.00, 0.50, 0.25] # x, y, and z of the fire hydrant
    quadLocation = msg.pose.position
    distance_xy = math.sqrt((quadLocation.x - hydrantLocation[0]) ** 2 + (quadLocation.y - hydrantLocation[1]) ** 2)
    

    # if publish distance topic, call "talker" here, then use rate(2) in talker?

    # rospy.loginfo(distance_xy)
    # rospy.loginfo(rospy.get_caller_id() + "Distance: %s", distance_xy)



def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    #initialize csv file
    with open('distance90deg.csv', 'w') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['distance'])  # header

    rospy.init_node('distance', anonymous=True)


    rospy.Subscriber("/mavros/local_position/pose", PoseStamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    r = rospy.Rate(4) # 2hz
    while not rospy.is_shutdown():
        writeToCSV(distance_xy)
        r.sleep()


if __name__ == '__main__':
    listener()
