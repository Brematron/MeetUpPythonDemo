import os
import sys

ip = sys.argv[1]

print("\n ### PING ### \n")

ping = "ping %s -c 3" % ip
os.system(ping)


print("\n ### NMAP ### \n")

nmap = "nmap %s " % ip
os.system(nmap)

print("\n ### SMB ### \n")

smb = 'smbmap -u "guest" -H ' + ip
os.system(smb)



