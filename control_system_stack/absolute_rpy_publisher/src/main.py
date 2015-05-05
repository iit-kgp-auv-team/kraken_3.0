import roslib;roslib.load_manifest('mission_planner')
import rospy
import rospy
import time

from resources import topicHeader

import kraken_msgs
import kraken_msgs
from kraken_msgs.msg._imuData import imuData
from kraken_msgs.msg._absoluteRPY import absoluteRPY

# print topicHeader.SENSOR_IMU
# print topicHeader.ABSOLUTE_RPY

def imuCallback(imu):

	global absolute_rpy_publisher

	roll = imu.data[0]
	pitch = imu.data[1]
	yaw = imu.data[2]

	# Fix the roll, pitch and yaw by subtracting it from 360

	roll = 360 - roll
	pitch = 360 - pitch
	yaw = 360 - yaw

	abrpy = absoluteRPY()
	abrpy.roll = roll
	abrpy.pitch = pitch
	abrpy.yaw = yaw

	absolute_rpy_publisher.publish(abrpy)

	# Store this in a message and publish it

absolute_rpy_publisher = rospy.Publisher(name=topicHeader.ABSOLUTE_RPY, data_class=absoluteRPY, queue_size=10)

rospy.Subscriber(name=topicHeader.SENSOR_IMU, data_class=imuData, callback=imuCallback)

rospy.init_node('absolute_roll_pitch_yaw_publisher')

rospy.spin()