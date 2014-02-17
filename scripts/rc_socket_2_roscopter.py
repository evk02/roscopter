#!/usr/bin/env python
import rospy
import socket
import json
from roscopter.msg import RC
from time import *

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0',7000))

def rc_socket_2_roscopter():
    pub = rospy.Publisher('send_rc', RC)
    rospy.init_node('rc_socket_2_roscopter')
    while not rospy.is_shutdown():
        # wait for UDP packet
        data,addr= sock.recvfrom(1024)
        data = data.replace("'", "\"");
    
        # parse it
        p = json.loads(data)
        print(p)
    
        # if control packet, send to ardupilot
        if p['type'] == 'rcinput':
            #str = "%d,%d,%d,%d" % (p['roll'], -p['pitch'], 1070 +  p['thr']*10, p['yaw'])
            rc_data = [1500 + p['roll']*10, 1500 - p['pitch']*10, 1070 +  p['thr']*10, 1500 + p['yaw']*10, 65535, 65535, 65535, 65535]
            pub.publish(RC(rc_data))

if __name__ == '__main__':
    try:
        rc_socket_2_roscopter()
    except rospy.ROSInterruptException:
        pass