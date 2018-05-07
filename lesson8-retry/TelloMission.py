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
retry("command", 3)
retry("takeoff", 3)
retry("go 60 60 60 5", 3)
retry("go -60 -60 -60 5", 3)
retry("flip b", 3)
retry("flip f", 3)
retry("land", 3)
