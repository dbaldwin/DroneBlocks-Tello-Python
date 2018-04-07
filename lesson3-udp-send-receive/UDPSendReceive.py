# This example script demonstrates how to send/receive commands to/from Tello
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the built-in socket package
import socket
import time

# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# Create a UDP connection that we'll send the command to
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# This "command" value is what lets Tello know that we want to enter command mode
message = "command"

# Send the message to Tello
sock.sendto(message.encode(), tello_address)

# Give Tello a bit of time to respond by adding a 1s delay (we'll make this more efficient in another script)
time.sleep(1)

# Read 128 bytes from the socket. Most of Tello responses are very small so 128 should be plenty
response = sock.recvfrom(128)

# Print message to screen
print(response)