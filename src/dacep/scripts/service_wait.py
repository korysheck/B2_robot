#!/usr/bin/env python
import rospy
#from srv import *
from std_msgs.msg import Byte
from std_srvs.srv import *

def handle_add_two_ints(req):
    print "zastavuji"
    rospy.loginfo("zastavuji")
    rospy.sleep(3.)
    print "jedu dal"
    rospy.loginfo("jedu dal")
    return []


def add_two_ints_server():    
    rospy.init_node('sleep_service_server')
    rospy.Service('sleep_service', Empty, handle_add_two_ints)
    print "service ready."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
