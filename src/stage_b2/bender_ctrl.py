#!/usr/bin/env python
# Skript snima klavesy a posila do 'key_input', z nehoz to bere 'bender_list_talk.py'

import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('key_input', Twist, queue_size=10)
    rospy.init_node('talker')
    twist = Twist() # definuju ze prom twist je format Twist
    while not rospy.is_shutdown():

        a = str(raw_input('vloz cislo m-couva /  k-stoji / i-dopredu: '))
        if a == 'i':
            twist.linear.x = 0.1 
        elif a == 'k':
            twist.linear.x = 0
        elif a == 'm':
            twist.linear.x = -0.1 
        
        print(twist)    
        pub.publish(twist)
        #rospy.sleep(1.0)


if __name__ == '__main__':
    try:
        talker()

    except rospy.ROSInterruptException:
        pass
        
        
        
        
        
