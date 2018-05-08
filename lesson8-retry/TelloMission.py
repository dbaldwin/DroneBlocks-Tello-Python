# This example script demonstrates how to get a response from Tello and use retry logic in the case of a failed command
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

from TelloRetry import Tello
import time

# Initialize our tello object
tello = Tello()

# Retry function with a command name and number of times to retry
def retry(command, times):

  # Configure a delay between each retry
  delay = 5

  # Send command to Tello and get response
  response = tello.send(command)

  # Delay before we send the next command
  time.sleep(delay)

  # See if the response was invalid
  if response != "OK":

    # Loop N times to retry the command with a 3s delay for each loop
    for i in range(times):

      # Send command again
      response = tello.send(command)

      # If response was good then lets break
      if response == "OK":
        break
      # Otherwise delay and loop again
      else:
        # Delay 5 seconds before retrying the command
        time.sleep(delay)

# Issue a series of SDK commands and watch the retry logic in action
retry("command", 2)
retry("takeoff", 2)

# Send an invalid command to Tello
retry("bad command", 2)

# Loop four times to fly back and forth
for i in range(4):
  retry("forward 75", 2)
  retry("cw 180", 2)
  
# Send a command with a value out of range
retry("speed 1000", 2)

# Land
retry("land", 2)