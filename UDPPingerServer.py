# UDPPingerServer.py
# Group H: Semaa Amin, Sabarinathan Kulasekaran, Yifan Zhang
# Sources: Textbook: Computer Networking: A Top-Down Approach; 8th edition; Kurose & Ross


# We will need the following module to generate randomized lost packets import random
import random
# From textbook 8th edition, page 156:
# The socket module forms the basis of all network communications in Python. By
# including this line, we will be able to create sockets within our program.
from socket import *

# Create a UDP socket
# Creating an IP address using AF_INET according that is corresponds to the socket we are creating
# according to the Python documentation https://docs.python.org/3/library/socket.html
# Using SOCK_Dgram for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM) # complete this line

# Assign IP address and port number to socket
# using group number 7 which corresponds to Project Group H
# we are providing a string containing either the IP address of the server (e.g., “128.138.32.126”)
# or the hostname of the server, in this case the problem asks us to use the hostname, then a
# DNS lookup will automatically be performed to get the IP address when it is run
# we add a line into our Python program after we create the socket to associate
# a specific port number (15007 in this case) to this UDP socket via the socket bind() method:
serverSocket.bind(('localhost', 15007))  # binds socket to ‘localhost’, port 15000+X, where X is your group number
print("Started UDP server on port 15007")
while True:
# Generate random number in the range of 0 to 10 rand =
# using the random() method imported from random above
    rand = random.randint(0, 10)

# Receive the client packet along with the address it is coming from message, address = # complete this line
# From page 158-159 of textbook
# When a packet arrives at the server’s socket, the packet’s data is put into the variable message and the
# packet’s source address is put into the variable address.
# The variable address contains both the client’s IP address and the client’s port number.
# Here, UDPServer will make use of this address information, as it provides a return
# address, similar to the return address with ordinary postal mail. With this source
# address information, the server now knows to where it should direct its reply.
# The standard/preferred UDP packet size is 1024
# The method recvfrom() also takes the buffer size 1024*0.7 as input
    message, address = serverSocket.recvfrom(int(1024*0.7))
# Capitalize the message from the client message =
# This line takes the line sent by the client and,after converting the message to a string,
# uses the method upper() to capitalize it.
    message = message.upper()
# complete this line
# If rand is less than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
# Otherwise, the server responds and sends the message to the client #complete this line
# This last line attaches the client’s address (IP address and port number) to the capitalized
# message (after converting the string to bytes), and sends the resulting packet into
# the server’s socket. Internet will then deliver the packet to this client address.
# After the server sends the packet, it remains in the while loop, waiting for another UDP packet to arrive

    serverSocket.sendto(message, address)


#SemaaAmin-completed-10302021