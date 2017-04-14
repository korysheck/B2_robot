#!/usr/bin/env python
# Posila benderovi 10x za sekundu twist s rychlosti

import rospy
from geometry_msgs.msg import Twist


def callback(data):
    global twist # potrebuju 'twist' globalne, protoze ji pouziva dalsi funkce
    twist = data
    print(twist)


def listener():
    global twist
    rospy.init_node('bender_list_talk', anonymous=True) # jak se jmenuje tenhle uzel - nemusi to byt nazev skriptu
    rospy.Subscriber("key_input", Twist, callback) # nazev topicu z nehoz odposlouchavam
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10) # nazev topicu do nehoz posilam
    
    r = rospy.Rate(10) # 10hz ... posilam 10x za sekundu
    while not rospy.is_shutdown():
        rospy.loginfo(twist)
        pub.publish(twist)
        r.sleep()
    
    rospy.spin()
   


if __name__ == '__main__':
    global twist
    twist = Twist()
    listener()

