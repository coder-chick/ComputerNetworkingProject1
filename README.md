# Computer Networking - Project 1 - UDP Socket Programming in Python
Course Materials from the Masters Computer Networking class CS5700 at Northeastern University

A socket programming for UDP in Python where datagram packets are sent and received between Server and Client. The server packet drop rate is simulated to be 30%.  The Round Trip Time (RTT) is calculated for 10 Pings and a proper socket timeout is implemented

## This project contains the following:
1. README.md
2. The Server UDP Pinger Python code --> "UDPPingerServer.py"
3. The Client UDP Pinger Python code --> "UDPPingerClient.py"
4. The Project requirement document --> "CS5700ProgrammingProjectRequirements.pdf"
5. A document explaining the code --> "CS5700Project1CodeExplanation.pdf"
6. Screenshot of terminal from the Server --> "UDPPingerServerScreenShot.png"
7. Screenshot of terminal from the Client --> "UDPPingerClientScreenShot.png"
8. Screenshot of terminal from the Server --> "Project1ServerPingsFromDifferentNetworks.png"
9. Screenshot of terminal from the Client --> "Project1ClientPingsFromDifferentNetworks.png"

## To Execute on the same network: 
From the computer terminal or command line:
1. First run the server. In the terminal, enter:
   * python UDPPingerServer.py 15007
2. Second, run the client. In the terminal, enter:
   * python UDPPingerClient.py localhost 15007

## To Execute on 2 different networks/computers: 
1. Turn Off Firewall of Server network
2. Turn off Firewall of Client network
3. From server network, find the IPv4 address
    * On a Mac, type "ipconfig getifaddr en0" in the terminal to find the IPv4
    * On a Windows, type "ipconfig" from the Command Prompt(CMD)
4. From the server network, edit the <UDPPingerServer.py> file to change the IP address in line 28 from 'localhost' to the Server's IPv4 that was found in step 3
5. From the client network, edit the <UDPPingerClient.py> file to change the IP address in line 19 from 'localhost' to the Server's IPv4 address that was found in step 3

From the computer terminal or command line:

6. Run the server. In the terminal, enter:
   * python UDPPingerServer.py 15007
7. Run the client. In the terminal, enter:
   * python UDPPingerClient.py <server's IPv4 address> 15007
 

## Screenshots of Terminal from same network

Client Screenshot          |  Server Screenshot
:-------------------------:|:-------------------------:
![Client Screenshot](https://github.com/coder-chick/ComputerNetworkingProject1/blob/main/UDPPingerClientScreenShot.png)  |  ![Server Screenshot](https://github.com/coder-chick/ComputerNetworkingProject1/blob/main/UDPPingerServerScreenShot.png)

## Screenshots of Terminal from different network

Client Screenshot from Different Network          |  Server Screenshot from Different Network
:-------------------------:|:-------------------------:
![Client Screenshot from Different Network](https://github.com/coder-chick/ComputerNetworkingProject1/blob/main/Project1ClientPingsFromDifferentNetworks.png)  |  ![Server Screenshot from Different Network](https://github.com/coder-chick/ComputerNetworkingProject1/blob/main/Project1ServerPingsFromDifferentNetworks.png)

## Author:
* Semaa Amin


