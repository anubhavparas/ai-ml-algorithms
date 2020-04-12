#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import json
import time


file_name = '/home/aditya/Downloads/action_velocity.json' #Enter here the file path leading to the .json file from the path planner
with open(file_name) as json_file:
	params = json.load(json_file)


def velocity_publisher():
	
	LIN = 0
	ANG = 1
	
	action_velocity_list = params['velocity']
	delta_time = params['delta_time']
	print('dT: '+str(delta_time))

	#Initialize publisher node and publish message object
	rospy.init_node('vel_publisher', anonymous=True)
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
	vel_msg = Twist()


	while not rospy.is_shutdown():
		i = 0
		start_time = time.clock()
		print('Steps taken :'+str(len(action_velocity_list)))
		print('Simulating motion ..')
		while i < len(action_velocity_list):


			linear_vel = action_velocity_list[i][LIN]
			angular_vel = action_velocity_list[i][ANG]
			#print('Publishing : Linear Velocity:= '+str(linear_vel)+' Angular Velocity:= '+str(angular_vel))
			vel_msg.linear.x = linear_vel
			vel_msg.angular.z = angular_vel
			print('Publishing : Linear Velocity:= '+str(vel_msg.linear.x)+' Angular Velocity:= '+str(vel_msg.angular.z))
			pub.publish(vel_msg)
			rospy.sleep(delta_time) #Sleeps for T = delta_time. After publishing
			i += 1
		print('Stopping..')
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		pub.publish(vel_msg)
		rospy.spin()

if __name__ == '__main__':
	try:
		
		velocity_publisher()

	except rospy.ROSInterruptException:
		pass


