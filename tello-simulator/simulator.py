# A basic Tello simulator for testing UDP commands
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/


import threading 
import socket
import sys
import time

# Address of this computer and port simulating Tello
tello_address = ('10.0.1.6', 8889)

# Create a local socket and bind to it
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(tello_address)

# Tello's address
sender_address = ('10.0.1.6', 9000)
tello_commands = ["command", "takeoff", "land", "up", "down", "left", "right", "back", "cw", "ccw", "flip", "speed", "Speed?", "Battery?", "Time?"]

def recv():
    while True:
        try:
            data, address = sock.recvfrom(2048)
            print("Received command: " + data.decode(encoding="utf-8"))
            reply = response(data.decode(encoding="utf-8"))
            sock.sendto(reply.encode(), sender_address)
        except Exception as e:
            print ('\nExit . . .\n' + str(e))
            break
            
def response(data):  
    if data in tello_commands:
      return "OK"
    else:
      return "FALSE"


#def send():
#  battery = 100
#  while True:
#    try:
#      print("sending")
#      sock.sendto(str(battery).encode(), tello_address)
#      time.sleep(10)
#      battery = battery - 1
#    except Exception as e:
#      print (str(e))
#      break
    
    
            
recvThread = threading.Thread(target=recv)
recvThread.start()

#sendThread = threading.Thread(target=send)
#sendThread.start()

