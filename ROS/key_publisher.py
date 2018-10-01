#!/usr/bin/env python2

import rospy
import sys, select, tty, termios
from std_msgs.msg import String

dev_freshrate = 100

if __name__ == '__main__':
    key_pub = rospy.Publisher('keys', String, queue_size = 1)
    rospy.init_node("key_to_buttons")
    rate = rospy.Rate(dev_freshrate)
    #BEGIN TERMIOS
    old_attr = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    #END TERMIOS
    print ("[NEWS]Publishing keystrokes. Press Ctrl-C to exit...")
    while not rospy.is_shutdown():
        #BEGIN SELECT
        if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:
            key_pub.publish(sys.stdin.read(1))
        rate.sleep()
        #END SELECT
    #BEGIN TERMIOS_END
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)
    #END TERMIOS_END
#END ALL
