# This example script demonstrates how to get a response from Tello and use retry logic in the case of a failed command
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the necessary modules
import socket
import threading

# Global variable that will contain the response from Tello
response = None

# Boolean value that toggles whether when the response timer is done receiving
timerIsComplete = false

# Used to set the boolean flag when the send/receive timer is complete
def cancelTimer():
  timerIsComplete = true

# Send the message to Tello and allow for a delay in seconds
def send(message):
  
  # We are about to start the timer
  timerIsComplete = false
  
  # Create a timer that will run for 5 seconds and call cancelTimer when done
  timer = threading.Timer(5, cancelTimer)
  
  # Begin the timer
  timer.start()
  
  # Try to send the message otherwise print the exception
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))
  
  # If there is no response let's print a message
  while response is None:
    if timerIsComplete is True:
      print("There was no reply from Tello")
  
  # End the timer
  timer.cancel()
  
  # Set data to the response from Tello
  data = response.decode(encoding='utf-8'))
  
  # Reset response for the next time we read data
  response = None
  
  # Return the data to the caller
  return data
  

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

      
send("command")
