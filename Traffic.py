from Tools import *
from Ethernet import Ethernet
from IP import IP
from TCP import TCP
from RawData import RawData

"""

"""


class Traffic:
    def __init__(self, filename):
        self.raw = RawData(filename)
        self.trames = []
        for frameBytes in raw.tabTrames:
            self.trames.append(Trame(frameBytes))
			
    def getDistinctIpAddresses():
        ips = set()
        for frame in trames:
            ips.add(frame.ip.srcAddress)
            ips.add(frame.ip.dstAddress)
        return [address for address in ips]
        
		
		
		
