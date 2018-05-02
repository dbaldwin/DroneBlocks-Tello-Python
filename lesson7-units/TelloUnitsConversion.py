# This example script demonstrates how to send distances to Tello either using imperial or metric units. By default Tello uses metric units.
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the necessary modules
import socket
import threading
import time

# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# IP and port of local computer
local_address = ('', 9000)

# Create a UDP connection that we'll send the command to
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port
sock.bind(local_address)

# Send the message to Tello and allow for a delay in seconds
def send(message, delay=0):
  # Try to send the message otherwise print the exception
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))
    
  # Delay for a user-defined period of time
  time.sleep(delay)

# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      response, ip_address = sock.recvfrom(128)
      print("Received message: " + response.decode(encoding='utf-8'))
    except Exception as e:
      # If there's an error close the socket and break out of the loop
      sock.close()
      print("Error receiving: " + str(e))
      break
      
# Create and start a listening thread that runs in the background
# This utilizes our receive function and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# Constants for converting in or ft to cm
INCHES_TO_CM = 2.54
FEET_TO_CM = 30.48

# Convert the distance to whatever conversion type specified, defaults to cm
def convertUnits(distance, conversionType="cm"):
  
  # Initalize the converted distance variable
  converted_distance = 0
  
  # Convert cm to inches
  if (conversionType == "in"):
    converted_distance = distance * INCHES_TO_CM
  # Convert cm to feet
  elif (conversionType == "ft"):
    converted_distance = distance * FEET_TO_CM
  # Default to cm in case where wrong conversionType is sent
  else:
    converted_distance = distance
    
  # Convert distance to string so it can be sent to Tello
  return str(converted_distance)
  
# Define variables for our star mission
leg_distance = 24
units = "in"
yaw_degrees = 144

# Put Tello into command mode and delay 3 seconds
send("command", 3)

# Takeoff and delay 5 seconds
send("takeoff", 5)

# We'll fly in a star pattern using cm, in, or ft
for i in range(5):
  
  # Fly forward leg_distance and specify units
  send("forward " + convertUnits(leg_distance, units), 5)

  # Rotate 144 degrees for the star pattern
  send("cw " + str(yaw_degrees), 5);

# Land - no need to specify a delay
send("land")