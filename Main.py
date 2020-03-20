import drone
import sys
import time

# Live drone
#drone_1 = drone.Drone("128.1.1.1", 8889)

# Test drone
#drone start up
drone_1 = drone.Drone('192.168.1.1', 8889)
drone_1.printinfo()
drone_1.connect()

#Print out start information
print(drone_1.battery(0.1))
print(drone_1.time(0.1))
print(drone_1.sdk(0.1))
print(drone_1.sn(0.1))

#Drone flightplan 
drone_1.takeOff(1)
drone_1.cw("90",1)
drone_1.ccw("360",1)
drone_1.cw("180",1)
drone_1.up("60",1)
drone_1.flip("b",1)
drone_1.down("30",1)
drone_1.left("20",1)
drone_1.right("20",1)

#print out landing information
print(drone_1.battery(0.1))
print(drone_1.time(0.1))

#Landing sequence
drone_1.land(1)
drone_1.end()