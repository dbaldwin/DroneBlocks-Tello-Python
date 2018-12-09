import socket
import time

filepath = './tello_state.log'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sender_address = ('', 8890)
sender_address = ('192.168.86.203', 5000)


with open(filepath) as fp:
    line = fp.readline()

    while line:
        print("Line: {}".format(line.strip()))
        line = fp.readline()
        sock.sendto(line.encode(), sender_address)
        time.sleep(1)