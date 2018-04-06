# This example script demonstrates how to send a basic command over UDP to Tello
# We will use PacketSender to simulate Tello for the purposes of this demonstration.
# PacketSender makes it easy to test code that can then be run when connected to Tello.
# https://packetsender.com/

# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the built-in socket package
import socket

# IP and port of sending computer
# In this case we're sending a UDP packet to PacketSender for demonstration purposes
# Be sure to change this to the IP address of the computer running this Python script
simulated_tello_address = ('10.0.1.6', 8889)

# Create a UDP connection that we'll send the command to
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Command variable that we'll send
# This "command" value is what lets Tello know that we want to enter command mode
message = "command"

# Send the message to Tello
sock.sendto(message.encode(), simulated_tello_address)

# Print message to screen
print("Message sent!")