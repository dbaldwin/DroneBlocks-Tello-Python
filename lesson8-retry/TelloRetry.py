# This example script demonstrates how to get a response from Tello and use retry logic in the case of a failed command
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the necessary modules
import socket
import threading

class Tello:

  # Called when we create an instance of our class
  def __init__(self):

    # Variable that will contain the response from Tello
    self.response = None

    # Boolean value that toggles whether when the response timer is done receiving
    self.timerIsComplete = False

    # IP and port of Tello
    self.tello_address = ('192.168.10.1', 8889)

    # IP and port of sending computer
    self.local_address = ('', 9000)

    # Create a UDP connection where we'll send commands
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to the local address and port
    self.sock.bind(self.local_address)

    # Create and start a listening thread that runs in the background
    # This utilizes our receive function and will continuously monitor for incoming messages
    self.receive_thread = threading.Thread(target=self.receive)
    self.receive_thread.daemon = True
    self.receive_thread.start()

  # Used to set the boolean flag when the send/receive timer is complete
  def cancelTimer(self):
    self.timerIsComplete = True

  # Send the message to Tello and allow for a delay in seconds
  def send(self, message):

    # We are about to start the timer
    self.timerIsComplete = False

    # Create a timer that will run for 5 seconds and call cancelTimer when done
    timer = threading.Timer(5, self.cancelTimer)

    # Begin the timer
    timer.start()

    # Try to send the message otherwise print the exception
    try:
      self.sock.sendto(message.encode(), self.tello_address)
      print("Sending message: " + message)
    except Exception as e:
      print("Error sending: " + str(e))

    # If there is no response let's print a message
    while self.response is None:
      if self.timerIsComplete is True:
        print("There was no reply from Tello")
        break

    # End the timer
    timer.cancel()

    # Set data to the response from Tello
    if self.response is not None:
      data = self.response.decode(encoding='utf-8')
    else:
      data = "Timeout"

    # Reset response for the next time we read data
    self.response = None

    # Return the data to the caller
    return data


  def receive(self):
    # Continuously loop and listen for incoming messages
    while True:
      # Try to receive the message otherwise print the exception
      try:
        self.response, ip_address = self.sock.recvfrom(128)
        print("Received message: " + self.response.decode(encoding='utf-8'))
      except Exception as e:
        # If there's an error close the socket and break out of the loop
        self.sock.close()
        print("Error receiving: " + str(e))
        break
