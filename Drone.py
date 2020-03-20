import socket
import sys
import time


class Drone(object):
    """ In this class der wil be 3 regions with commands and information that the drone will have.
        The 4 regions are StartUp, Commands, Mission Pad and Information Messages.
        The start region includes det connection to the wifi and drone and the functions: sendMessage and printInfo.
        The commands includes the commands that the drone can perform.
        The mission pad includes the commands for the mission pad.
        The information messages includes the messages about battery, flytime, serial number and SDK informations."""

# region Startup/Setup

    # Constructor
    def __init__(self, ip, port):
        self.TelloIp = ip
        print("ip: " + ip)
        self.TelloPort = port
        self.Host = ""
        self.HostPort = 9000
        self.locaddr = (self.Host, self.HostPort)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tello_address = ("192.168.10.1", 8889)
        self.sock.bind(self.locaddr)

    # Connection
    def connect(self, wait):
        print("Connect")
        result = self.sendMessage("command")
        print(result)
        time.sleep(wait)

    # Sending messages/commands to the drone
    def sendMessage(self, TelloMessage):
        print("TelloMessage " + TelloMessage + " end")
        msg = TelloMessage.encode(encoding="utf-8")
        sent = self.sock.sendto(msg, self.tello_address)
        data, server = self.sock.recvfrom(1518)
        print(data.decode(encoding="utf-8"))

        return "from sendmessage " + TelloMessage + " end "

    # Print out information about location
    def printInfo(self, wait):
        print("Hello Drone at : " + self.TelloIp)
        time.sleep(wait)

    # set wifi password for Tello drone
    def wifi_ssid_pass(self, ssid, password, wait):
        print("wifi_ssid_pass")
        result = self.sendMessage("wifi " + "ssid" + " " + "password")
        time.sleep(wait)

    # update Wifi password for the Tello drone
    def ap_ssid_pass(self, ssid, password, wait):
        print("ap_ssid_pass")
        result = self.sendMessage("ap " + "ssid" + " " + "password")
        time.sleep(wait)

    # Remote controller settings
    def rcabcd(self, a, b, c, d, wait):
        print("rcabcd")
        result = self.sendMessage(
            "rc " + " " + a + " " + b + " " + c + " " + d
        )
        time.sleep(wait)

# endregion
# region Commands

    # TakeOff the ground
    def takeOff(self, wait):
        print("takeOff")
        result = self.sendMessage("TakeOff")
        time.sleep(wait)

    # Landing the drone
    def land(self, wait):
        print("land")
        result = self.sendMessage("land")
        time.sleep(wait)

    # End the drone
    def end(self, wait):
        print("end")
        self.sock.close()
        time.sleep(wait)

    # Turn clockwise
    def cw(self, x, wait):
        print("cw")
        result = self.sendMessage("cw " + x)
        time.sleep(wait)

    # Turn counter clockwise
    def ccw(self, x, wait):
        print("ccw")
        result = self.sendMessage("ccw " + x)
        time.sleep(wait)

    # Fly up
    def up(self, x, wait):
        print("up")
        result = self.sendMessage("up " + x)
        time.sleep(wait)

    # Fly down
    def down(self, x, wait):
        print("down")
        result = self.sendMessage("down " + x)
        time.sleep(wait)

    # Turn left
    def left(self, x, wait):
        print("left")
        result = self.sendMessage("left " + x)
        time.sleep(wait)

    # Turn right
    def right(self, x, wait):
        print("left")
        result = self.sendMessage("left " + x)
        time.sleep(wait)

    # Move forward
    def forward(self, x, wait):
        print("forward")
        result = self.sendMessage("forward " + x)
        time.sleep(wait)

    # Move backwards
    def back(self, x, wait):
        print("back")
        result = self.sendMessage("back " + x)
        time.sleep(wait)

    # Flip in given direction
    def flip(self, x, wait):
        print("flip")
        result = self.sendMessage("flip " + x)
        time.sleep(wait)

    # Hover
    def stop(self, wait):
        print("stop")
        result = self.sendMessage("stop")
        time.sleep(wait)

    # Set Speed
    def speed(self, wait):
        print("speed")
        result = self.sendMessage("speed " x)

    # Fly at a curve (drifting)
    def curve(self, x1, y1, z1, x2, y2, z2, speed, wait):
        print("curve")
        result = self.sendMessage(
        "curve " + x1 + " " + y1 + " " + z1 + " " + x2 +
            " " + y2 + " " + z2 + " " + speed
        )
        time.sleep(wait)


# endregion
# region Missionpad
""" A Mission pad is used together with a Tello Drone.
    The Tello Drone uses its camera to detect the Mission Pads ID and
    executes this Mission pads programmed commands. """

   # Fly at a curve, with mission pad (drifting)
   def curve_pad(self, x1, y1, z1, x2, y2, z2, speed, mid, wait):
        print("curve")
        result = self.sendMessage(
        "curve " + x1 + " " + y1 + " " + z1 + " " + x2 +
            " " + y2 + " " + z2 + " " + speed + " " + mid
        )
        time.sleep(wait)

    # Fly to the XYZ coordinates of the mission pad
    def goXYZSpeed(self, x, y, z, speed, wait):
        print("goXYZSpeed")
        result = self.sendMessage("go " + x + " " + y + " " + z + " " + speed)
        time.sleep(wait)

    # Mission pad detection
    def mdirection(self, x, wait):
        print("mdirection")
        result = self.sendMessage("mdirection" + x)
        time.sleep(wait)
        return result

    # Turn off mission pad detection
    def moff(self, wait):
        print("moff")
        result = self.sendMessage("moff")
        time.sleep(wait)
        return result

    # Fly from mission pad 1 to mission pad 2
    def jump(self, x, y, z, speed, yaw, mid1, mid2, wait):
        print("jump")
        result = self.sendMessage(
            "jump" + " " + x + " " + y + " " + z + " "
            + speed + " " + yaw + " " + mid1 + " " + mid2
        )

# endregion
# region informations messages

    # Give a battery message
    def battery(self, wait):
        result = self.sendMessage("battery?")
        time.sleep(wait)
        return result

    # Flytime
    def time(self, wait):
        result = self.sendMessage("time?")
        time.sleep(wait)
        return result

    # Trello SDK version
    def sdk(self, wait):
        result = self.sendMessage("sdk?")
        time.sleep(wait)
        return result

    # Trello serial number
    def sn(self, wait):
        result = self.sendMessage("sn?")
        time.sleep(wait)
        return result

# endregion
