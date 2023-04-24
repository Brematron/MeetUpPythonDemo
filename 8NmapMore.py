import os
import sys

ip = sys.argv[1]

print("\n ### NMAP ### \n")

nmap = "nmap %s " % ip
nmap_output = os.popen(nmap).read()
print(nmap_output)

if "80/tcp" in str(nmap_output):
    nmap = "nmap -sC -sV -p 80 %s " % ip
    print(f"\n ### {nmap} ### \n")
    os.system(nmap)
