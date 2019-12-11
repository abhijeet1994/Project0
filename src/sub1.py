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
    a = str(a)
    part[1] = a
    

def callback2(data):
    a =  ( "%s", data.data)
    a = str(a)
    part[0] = a
    print(part[0] + part[1])    

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    print("im here")
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback1)
    rospy.Subscriber("chatter2", String, callback2)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    part = ["this", "should work"]
    listener()

