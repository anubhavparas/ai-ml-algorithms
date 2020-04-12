#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def comm():
	pub = rospy.Publisher('receiver', String, queue_size=10)
	rospy.init_node('comm',anonymous=True)
	rate = rospy.Rate(10) #10Hz
	while not rospy.is_shutdown():
		hello_str = "Hello ROS! %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

if __name__ == 'main':
	try:
		comm()
	except rospy.ROSInterruptException:
		pass
