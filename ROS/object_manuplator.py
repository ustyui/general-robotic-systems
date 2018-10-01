#!/usr/bin/env python2

#play it with key_publisher.py
import rospy
from std_msgs.msg import String
from time import sleep

class Values(object):
    def __init__(self):
        self.value = 100

def callback(msg,args):
    banana = args
    banana.value += 2


if __name__ == "__main__":
    rospy.init_node('valuechanger')
    rate=rospy.Rate(20)
    banana = Values()
    banana.value = 101
    rospy.Subscriber('keys', String, callback, banana)
    while not rospy.is_shutdown():
        
        print (banana.value)
        rate.sleep()
        
    rospy.spin()


