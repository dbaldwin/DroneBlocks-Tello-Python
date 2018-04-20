# This example script demonstrates how use Python to create custom flight behaviors with Tello
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
def send(message, delay):
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
# This utilizes our receive functions and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# Initiate command mode and takeoff
def takeoff():
  send("command", 3)
  send("takeoff", 5)

# Land
def land():
  send("land", 5)

# Tello commands respond with an OK when sucessful. This means Tello recognizes
# the command, but the instruction hasn't completed. OK is Tello saying "I got
# the message" but not necessarily saying "I completed the command"
# This means we need to calculate how long the spin will take before we execute the next command.
# Based on our tests a single 360 rotation takes 7 seconds. We'll use this in our spin function to delay
# before the next command. Your rotation time may vary. You can calculate this by
# sending a "cw 360" or "ccw 360" command and measuring the rotation time.

# 7 seconds per rotation
rotationTime = 7

# Spin right or left X number of times
def spin(direction, times):
  # One rotation is 360 degrees
  oneRotation = 360

  # Convert the number of rotations to degrees
  rotations = oneRotation * times

  # Calculate the delay to let the spin function complete
  delay = rotationTime * times

  # Spin right (cw) or left (ccw)
  if (direction == "right"):
    send("cw " + str(rotations), delay)
  elif (direction == "left"):
    send("ccw " + str(rotations), delay)

# Use 20 cm/sec as vertical speed
verticalSpeed = 20.0

def bounce(distance, times):

  bounceDelay = distance/verticalSpeed

  for i in range(times):
    send("down " + str(distance), bounceDelay)
    send("up " + str(distance), bounceDelay)

# Takeoff
takeoff()

# Spin right 2 times
spin("right", 2)

# Bounce up and down 60 cm and repeat 3 times
bounce(60, 3)

# Spin left 3 times
spin("left", 3)

# Land
land()

# Close the socket
sock.close()
