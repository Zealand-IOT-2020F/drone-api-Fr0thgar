import drone
import sys
import time

drone_1 = drone.Drone("128.1.1.1", 8889)

#here you should interact with the drone

drone_1.printinfo()

drone_1.connect()

drone_1.takeOff()
time.sleep(1)
drone_1.cw("90")
time.sleep(1)
drone_1.ccw("360")
drone_1.cw("180")
time.sleep(1)
print(drone_1.battery())
drone_1.land()

drone_1.end()
