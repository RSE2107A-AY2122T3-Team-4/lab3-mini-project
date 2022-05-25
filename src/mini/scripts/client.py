#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from ..srv import *

def req(req_val):
  rospy.wait_for_service('Status')
  rospy.Rate(1)
  try:
      get_status = rospy.ServiceProxy('Status', get_status)
      status = get_status(req_val)
  except:
      return
  rospy.spin()

def callback(data):
  pub0 = rospy.Publisher('limo_status/vehicle_state', String, queue_size = 10)
  pub1 = rospy.Publisher('limo_status/control_mode', String, queue_size = 10)
  pub2 = rospy.Publisher('limo_status/vehicle_state', String, queue_size = 10)
  pub3 = rospy.Publisher('/limo_status/error_code', String, queue_size = 10)
  pub4 = rospy.Publisher('/limo_status/motion_mode', String, queue_size = 10)
  rospy.spin()

if __name__ == '__main__':
  req()
