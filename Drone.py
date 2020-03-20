import socket
import sys
import time


class Drone(object):
    """description of class"""
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


    #Sending messages/commands to the drone
    def sendMessage(self, TelloMessage):
        print("TelloMessage "+ TelloMessage +" end")
        msg = TelloMessage.encode(encoding="utf-8")
        sent  = self.sock.sendto(msg, self.tello_address)
        data, server = self.sock.recvfrom(1518)
        print(data.decode(encoding="utf-8"))
        
        return "from sendmessage " + TelloMessage + " end "
        
    #Print out information abbut location
    def printInfo(self):
        print("Hello Drone at : " + self.TelloIp)

    #Connection
    def connect(self):
        print("Connect")
        result = self.sendMessage("command")
        print(result)

    #TakeOff the ground
    def takeOff(self):
        print("takeOff")
        result = self.sendMessage("TakeOff")

    #Landing the drone
    def land(self):
        print("land")
        result = self.sendMessage("land")
    
    #End the drone
    def end(self):
        print("end")
        self.sock.close()

    #Turn clockwise
    def cw(self,x):
        print("cw")
        result = self.sendMessage("cw " + x)
    
    #Turn counter clockwise
    def ccw(self,x):
        print("ccw")
        result = self.sendMessage("ccw " + x)

    #Give a battery message
    def battery(self):
        result = self.sendMessage("battery?")
        return result

    