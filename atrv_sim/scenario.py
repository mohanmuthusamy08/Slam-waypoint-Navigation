from morse.builder import *


robot = ATRV()
#robot = QUAD2012() 
robot.add_interface('ros')
robot.translate(x=2.0, y=-2.0, z=0.0)

# An odometry sensor to get odometry information
odometry = Odometry()
robot.append(odometry)
odometry.add_interface('ros', topic="/odom")

# Keyboard control
keyboard = Keyboard()
robot.append(keyboard)


motion = MotionXYW()
motion.properties(ControlType = 'Position')
robot.append(motion)
motion.add_interface('ros', topic='/cmd_vel')

# Set the environment
#env = Environment('indoors-1/indoor-1')
#env = Environment('indoors-1/boxes')
#env = Environment('laas/grande_salle')
#env = Environment('tum_kitchen/tum_kitchen')
#env = Environment('outdoors')
env = Environment('/home/mohan/simple_world.blend')
#env = Environment('land-1/trees')
env.set_camera_rotation([1.0470, 0, 0.7854])

#Lidar Specs
scan = Hokuyo()
robot.append(scan)
scan.properties(Visible_arc = True)
scan.properties(laser_range = 30.0)
scan.properties(resolution = 1.0)
scan.properties(scan_window = 180.0)
scan.create_laser_arc()

scan.add_interface('ros', topic='/base_scan')
