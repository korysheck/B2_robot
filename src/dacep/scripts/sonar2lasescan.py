#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import sensor_msgs.msg

# TALKER bere v nezname 'data' info ze sonaru a publikuje
def talker(data):
    if data.header.frame_id == '/base_laser_link_1':
        pub = rospy.Publisher('/SRF08_1', sensor_msgs.msg.LaserScan, queue_size=10)
        data.ranges = data.ranges + data.ranges + data.ranges + data.ranges + data.ranges # takto se upravuje pole typu 'tuple'
        data.angle_increment = 0.026179938
        data.intensities = data.intensities + data.intensities + data.intensities + data.intensities + data.intensities
        data.header.frame_id = "srf08_1"
        #print(data.ranges)
        print('1')
        pub.publish(data)
    elif data.header.frame_id == '/base_laser_link_2':
        pub = rospy.Publisher('/SRF08_2', sensor_msgs.msg.LaserScan, queue_size=10) # NAJDI V dacep.urdf spravne usporadani senzoru tak, jak je bere move_base!
        data.ranges = data.ranges + data.ranges + data.ranges + data.ranges + data.ranges
        data.angle_increment = 0.026179938
        data.intensities = data.intensities + data.intensities + data.intensities + data.intensities + data.intensities
        data.header.frame_id = "srf08_2"
        #print(data.ranges)
        print('2')
        pub.publish(data)
    elif data.header.frame_id == '/base_laser_link_3':
        pub = rospy.Publisher('/SRF08_3', sensor_msgs.msg.LaserScan, queue_size=10) # NAJDI V dacep.urdf spravne usporadani senzoru tak, jak je bere move_base!
        data.ranges = data.ranges + data.ranges + data.ranges + data.ranges + data.ranges
        data.angle_increment = 0.026179938
        data.intensities = data.intensities + data.intensities + data.intensities + data.intensities + data.intensities
        data.header.frame_id = "srf08_3"
        #print(data.ranges)
        print('3')
        pub.publish(data)
    elif data.header.frame_id == '/base_laser_link_4':
        pub = rospy.Publisher('/SRF08_4', sensor_msgs.msg.LaserScan, queue_size=10) # NAJDI V dacep.urdf spravne usporadani senzoru tak, jak je bere move_base!
        data.ranges = data.ranges + data.ranges + data.ranges + data.ranges + data.ranges
        data.angle_increment = 0.026179938
        data.intensities = data.intensities + data.intensities + data.intensities + data.intensities + data.intensities
        data.header.frame_id = "srf08_4"
        #print(data.ranges)
        print('4')
        pub.publish(data)
    elif data.header.frame_id == '/base_laser_link_5':
        pub = rospy.Publisher('/SRF08_5', sensor_msgs.msg.LaserScan, queue_size=10) # NAJDI V dacep.urdf spravne usporadani senzoru tak, jak je bere move_base!
        data.ranges = data.ranges + data.ranges + data.ranges + data.ranges + data.ranges
        data.angle_increment = 0.026179938
        data.intensities = data.intensities + data.intensities + data.intensities + data.intensities + data.intensities
        data.header.frame_id = "srf08_5"
        #print(data.ranges)
        print('5')
        pub.publish(data)
    elif data.header.frame_id == '/base_laser_link_6':
        pub = rospy.Publisher('/SRF08_6', sensor_msgs.msg.LaserScan, queue_size=10) # NAJDI V dacep.urdf spravne usporadani senzoru tak, jak je bere move_base!
        data.ranges = data.ranges + data.ranges + data.ranges + data.ranges + data.ranges
        data.angle_increment = 0.026179938
        data.intensities = data.intensities + data.intensities + data.intensities + data.intensities + data.intensities
        data.header.frame_id = "srf08_6"
        #print(data.ranges)
        print('6')
        pub.publish(data)
    elif data.header.frame_id == '/base_laser_link_7':
        pub = rospy.Publisher('/SRF08_7', sensor_msgs.msg.LaserScan, queue_size=10) # NAJDI V dacep.urdf spravne usporadani senzoru tak, jak je bere move_base!
        data.ranges = data.ranges + data.ranges + data.ranges + data.ranges + data.ranges
        data.angle_increment = 0.026179938
        data.intensities = data.intensities + data.intensities + data.intensities + data.intensities + data.intensities
        data.header.frame_id = "srf08_7"
        #print(data.ranges)
        print('7')
        pub.publish(data)
    else:
        print('Did not find right -header.frame_id- for desired sensor')

# LISTENER pouziva jako callback funkci talkera
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('sonar2lasescan', anonymous=True) # staci node inicializovat tady, v talkeru uz nesmis

    rospy.Subscriber('/base_scan_1', sensor_msgs.msg.LaserScan, talker)
    rospy.Subscriber('/base_scan_2', sensor_msgs.msg.LaserScan, talker)
    rospy.Subscriber('/base_scan_3', sensor_msgs.msg.LaserScan, talker)
    rospy.Subscriber('/base_scan_4', sensor_msgs.msg.LaserScan, talker)
    rospy.Subscriber('/base_scan_5', sensor_msgs.msg.LaserScan, talker)
    rospy.Subscriber('/base_scan_6', sensor_msgs.msg.LaserScan, talker)
    rospy.Subscriber('/base_scan_7', sensor_msgs.msg.LaserScan, talker)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    
    #1rate = rospy.Rate(10)
    #1rate.sleep()

# MAIN smyska
if __name__ == '__main__':
    listener()
    #1while not rospy.is_shutdown():
        #1listener()
