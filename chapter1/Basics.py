#variables
port = 21
print("Port is", port)

#strings
banner = "FreeBSD 9.0"
print(banner)

#Lists
portList = []
portList.append(121)
portList.append(80)
portList.append(443)
print("POrtList before sorting: ", portList)
portList.sort()
print("PortList after sorting: ", portList)

#Dictionaries
services = {'ftp':21, 'ssh':22, 'smtp':25, 'http':80}
print("FTP port keys is", services.keys())
print("FTP port items is", services.items())


#Networking
# import socket
# socket.setdefaulttimeout(10)
# s= socket.socket()
# s.connect(("socket.gethostname()", 1234))
# ans = s.recv(1024)
# print(ans)

#Exception Handling
try:
    print(5/0)
except Exception as e:
    print("Error: ", e)

#Functions
# def Socket_to_me(ip,port,time):
#         try:
#             s = socket.socket()
#             s.settimeout(time)
#             s.connect((ip,port))
#             ans = s.recv(1024)
#             print(ans)
#             s.shutdown(1) # By convention, but not actually necessary
#             s.close()     # Remember to close sockets after use!
#         except socket.error as socketerror:
#             print("Error: ", socketerror) 

# call the method by:
# Socket_to_me(socket.gethostname(),1234,10)

#Iteration
for x in range(1,20):
    print ("192.168.1."+str(x))

#File I/O
# def checkVulns(banner):
#     f = open("vuln_banners.txt", 'r')
#     for line in f.readlines():
#         if line.strip('\n') in banner:
#             print(" Server is vulnerable :" + banner.strip('\n'))

# Sys Module
import sys
print("Sys arguments: ", sys.argv)
if len(sys.argv) == 2:
    filename = sys.argv[1]
    print("Filename is", filename)

# OS Module
import os
if len(sys.argv) == 2:
    if not os.path.isfile(filename):
        print("File does not exist")
        exit(0)
    if not os.access(filename, os.R_OK):
        print("Access denied")
        exit(0)
    print("Reading file")
    f = open(filename, 'r')
    print(f.read())
    f.close()
