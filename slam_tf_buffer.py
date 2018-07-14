#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv
if __name__ == '__main__':
    rospy.init_node('slam_tf_buffer')
    listener = tf.TransformListener()
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(20.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/map', '/slam_odom', rospy.Time(0))
            br.sendTransform(
                trans,
                rot,
                rospy.Time.now(),
                "odom",
                "map")
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as ex:
            print(ex)
            continue
        rate.sleep()
