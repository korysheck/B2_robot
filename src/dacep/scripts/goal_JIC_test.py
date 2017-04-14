#! /usr/bin/env python

import roslib
import rospy

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import actionlib_tutorials.msg
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal 
from std_srvs.srv import *

def goals_client():
	# create publisher
	pub = rospy.Publisher('/move_base_simple/goal', PoseStamped,  queue_size=5 )
	
	#rospy.wait_for_service('sleep_service')
	
	# Creates the SimpleActionClient, passing the type of the action
	# (FibonacciAction) to the constructor.
	client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	rospy.wait_for_service('sleep_service')
	wait_service = rospy.ServiceProxy('sleep_service', Empty)
	
	# Waits until the action server has started up and started
	# listening for goals.
	client.wait_for_server()
	
	#wait_client.wait_for_server()
	
	goal = MoveBaseGoal()
	
	#while not rospy.is_shutdown():
	
	print "begin"
	
	#
	# 1
	#
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.get_rostime()
	
	goal.target_pose.pose.position.x = 5.93922615051
	goal.target_pose.pose.position.y = 9.22567939758
	
	goal.target_pose.pose.orientation.z = 0.703845392918
	goal.target_pose.pose.orientation.w = 0.710353195859
	
	# Sends the goal to the action server
	client.send_goal(goal)
	# Waits for the server to finish performing the action.
	client.wait_for_result()
	
	print "service calling"
	
	prd = Empty()
	#hovno = wait_service.call(prd)
	hovno = rospy.ServiceProxy('sleep_service', prd)
	#hovno = wait_client.call(prd)
	
	print "calling succes"
	
	#result = client.get_result()
	#print "Result:", ', '.join([str(n) for n in result.sequence])
	
	print "1 complete"
	
	#
	#2
	#
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.get_rostime()
	
	goal.target_pose.pose.position.x = 5.89642810822 
	goal.target_pose.pose.position.y = 11.594865799 
	
	goal.target_pose.pose.orientation.z = 0.703845034053 
	goal.target_pose.pose.orientation.w = 0.710353551437 
	
	# Sends the goal to the action server
	client.send_goal(goal)
	# Waits for the server to finish performing the action.
	client.wait_for_result()
	
	#result = client.get_result()
	#print "Result:", ', '.join([str(n) for n in result.sequence])
	print "2 complete"
	
	#
	#3
	#
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.get_rostime()
	
	goal.target_pose.pose.position.x = 5.87271595001 
	goal.target_pose.pose.position.y = 11.3582048416 
	
	goal.target_pose.pose.orientation.z = -0.708417042404 
	goal.target_pose.pose.orientation.w = 0.705794087558
			 
	# Sends the goal to the action server.
	client.send_goal(goal)
	# Waits for the server to finish performing the action.
	client.wait_for_result()
	
	#result = client.get_result()
	#print "Result:", ', '.join([str(n) for n in result.sequence])
	print "3 complete"
	
	#
	# 4
	#
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.get_rostime()
	
	goal.target_pose.pose.position.x = 5.91584014893 
	goal.target_pose.pose.position.y = 6.68482637405 
	
	goal.target_pose.pose.orientation.z = -0.700081090066 
	goal.target_pose.pose.orientation.w = 0.714063349663 
			
	# Sends the goal to the action server.
	client.send_goal(goal)
	# Waits for the server to finish performing the action.
	client.wait_for_result()
	
	print "4 complete"
	
	#
	# 5
	#
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.get_rostime()
	
	goal.target_pose.pose.position.x = 5.92848920822 
	goal.target_pose.pose.position.y = 6.88928699493 
	
	goal.target_pose.pose.orientation.z = 0.710514529913 
	goal.target_pose.pose.orientation.w = 0.703682529827 
			
	# Sends the goal to the action server.
	client.send_goal(goal)
	# Waits for the server to finish performing the action.
	client.wait_for_result()
	
	print "5 complete"
	
	#
	# 6
	#
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.get_rostime()
	
	goal.target_pose.pose.position.x = 5.91187620163 
	goal.target_pose.pose.position.y = 6.25417232513 
	
	goal.target_pose.pose.orientation.z = 0.707066782365 
	goal.target_pose.pose.orientation.w = 0.707146777745 
			
	# Sends the goal to the action server.
	client.send_goal(goal)
	# Waits for the server to finish performing the action.
	client.wait_for_result()
	
	
	print "6 complete"
	
	#
	# 6
	#
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.get_rostime()
	
	goal.target_pose.pose.position.x = 5.91187620163 
	goal.target_pose.pose.position.y = 6.25417232513 
	
	goal.target_pose.pose.orientation.z = 0.707066782365 
	goal.target_pose.pose.orientation.w = 0.707146777745 
			
	# Sends the goal to the action server.
	client.send_goal(goal)
	# Waits for the server to finish performing the action.
	client.wait_for_result()
	
	
	print "6 complete"
	
	# Prints out the result of executing the action
	return client.get_result()  # A FibonacciResult

if __name__ == '__main__':
    try:
        # Init nodes
        rospy.init_node('simple_navigation_goals')
        result = goals_client()
        #print "Result:", ', '.join([str(n) for n in result.sequence])
    except rospy.ROSInterruptException:
        print "program interrupted before completion"
