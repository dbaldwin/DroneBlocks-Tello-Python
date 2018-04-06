#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time


host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)
#tello_address = ('127.0.0.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

command = "command"
command = command.encode(encoding="utf-8")
sock.sendto(command, tello_address)

time.sleep(3)

while True:

    try:
        #msg = input("");

        #if not msg:
        #    break  

        #if 'end' in msg:
        #    print ('...')
        #    sock.close()  
        #    break

        # Send data
        #msg = msg.encode(encoding="utf-8") 
        msg = "battery?".encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
        time.sleep(10)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break




