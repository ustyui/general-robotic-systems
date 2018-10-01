#!/usr/bin/env python2

"""
a key receiver
Author: ustyui
"""
#Your device name here
dev_name = 'device'

#ros modules
import rospy
from std_msgs.msg import String

def keys_callback(msg):
    if len(msg.data) == 0:
        return
    #a window of testing the key
    print (msg.data)
    if(msg.data == 'a'): #just for an exmaple
        print('something')
    
    return

if __name__ == "__main__":
    rospy.init_node('keys_to_' + dev_name)
    rospy.Subscriber('keys', String, keys_callback)

    rospy.spin()
