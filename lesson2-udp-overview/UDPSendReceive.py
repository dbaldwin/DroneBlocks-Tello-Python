# Import the built-in socket package
import socket
import threading

# IP and port of sending computer
# In this case we're sending a UDP packet to PacketSender for demonstration purposes
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