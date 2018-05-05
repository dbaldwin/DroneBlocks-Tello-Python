# This example script demonstrates how to get a response from Tello and use retry logic in the case of a failed command
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

from TelloRetry import Tello

tello = Tello()
tello.send("command")