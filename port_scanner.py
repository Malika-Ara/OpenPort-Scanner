import sys
import socket
from datetime import datetime


print("\n")
print("---OPEN PORT SCANNER---")
print("\n")
targetip = input(str("Enter target ip address:"))
 
# Add Banner 
startTime = datetime.now()
print("Scanning Target: " + targetip)
print("Scanning started at:" + str(datetime.now()))

try:
     
    # will scan ports between 1 to 655
    for port in range(1,655):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.2)   #will wait for 0.2 seconds then move to another port to check
         
        # returns an error indicator
        result = s.connect_ex((targetip,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()
    endTime = datetime.now()
    print('Time taken:', endTime - startTime)

except KeyboardInterrupt:
        print("\n Exit")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved")
        sys.exit()
except socket.error:
        print("\ Server is not responding")
        sys.exit()
total = endTime - startTime
print ("Scanning completed in: ",total)

#Press CTRL+C to exit in the middle of scanning