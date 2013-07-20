#!/usr/bin/env python

import roslib; roslib.load_manifest('nxt_assisted_teleop')  
import rospy
from nxt_msgs.msg import Color
from geometry_msgs.msg import Twist


class Follow:
    def __init__(self):
        self.sub = rospy.Subscriber('intensity', Color, self.sub_cb)
        self.pub = rospy.Publisher('cmd_vel', Twist)
        rospy.on_shutdown(self.shutdown)

    def sub_cb(self, msg):
        vel = Twist()
        #tests just speed with intensity. performance seems good
        vel.linear.x = 0.0007*(msg.intensity-227)
        vel.angular.z = 0.0007*(msg.intensity-227)
        self.pub.publish(vel)

    def shutdown(self):
        vel = Twist()
        vel.linear.x = 0
        vel.angular.z = 0
        self.pub.publish(vel)

def main():
    rospy.init_node('linefollower')
    follow = Follow()
    
    rospy.spin()



if __name__ == '__main__':
    main()
