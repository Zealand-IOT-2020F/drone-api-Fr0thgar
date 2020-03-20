import drone
import sys
import time

# Live drone
#drone_1 = drone.Drone("128.1.1.1", 8889)

# Test drone
drone_1 = drone.Drone('192.168.1.1', 8889)


drone_1.printinfo()

drone_1.connect()

print(drone_1.battery())
time.sleep(1)
print(drone_1.time())
time.sleep(1)
print(drone_1.sdk())
time.sleep(1)
print(drone_1.sn())

drone_1.takeOff()
time.sleep(1)
drone_1.cw("90")
time.sleep(1)
drone_1.ccw("360")
drone_1.cw("180")
time.sleep(1)
print(drone_1.battery())
time.sleep(1)
print(drone_1.time())
time.sleep(1)
print(drone_1.sdk())
time.sleep(1)
print(drone_1.sn())


drone_1.land()

drone_1.end()
