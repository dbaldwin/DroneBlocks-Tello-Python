# This example script demonstrates how to send/receive commands to/from Tello
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the built-in socket package
import socket
import threading
import time

# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# Create a UDP connection that we'll send the command to
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Function to send messages to Tello
def send(message):
  try:
    sock.sendto(message.encode(), tello_address)
  except Exception as e:
    print("Error sending: " + str(e))

# Function that listens for messages from Tello
def receive():
  try:
    response, ip_address = sock.recvfrom(128)
    print("Received message: " + response.decode(encoding='utf-8') + " from Tello with IP: " + str(ip_address))
  except Exception as e:
    print("Error receiving: " + str(e))


# Send Tello into command mode
send("command")

# Delay 1 second
time.sleep(1)

# Receive response from Tello
receive()

# Delay 1 second
time.sleep(1)

# Ask Tello its battery percentage remaining
send("battery?")

# Delay 1 second
time.sleep(1)

# Receive battery response from Tello
receive()

# Close the UDP socket
sock.close()