#!/usr/bin/env python
import rospy
from std_msgs.msg import String
"""
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
"""
def callback1(data):
    a = ( "I heard %s", data.data)
    print(a)
    print(a.type)
    return a

def callback2(data):
    a =  ( "%s", data.data)
    print (a)
    print(a.type)
    return a
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    part2 = rospy.Subscriber("chatter", String, callback1)
    part1 = rospy.Subscriber("chatter2", String, callback2)

    print (part1 + part2)	
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

