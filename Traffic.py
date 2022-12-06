from Tools import *
from Ethernet import Ethernet
from IP import IP
from TCP import TCP
from RawData import RawData
from Trame import Trame

"""

"""


class Traffic:
    def __init__(self, filename):
        self.raw = RawData(filename)
        self.trames = []
        for frameBytes in self.raw.tabTrames:
            self.trames.append(Trame(frameBytes))
			
    def getDistinctIpAddresses(self):
        ips = set()
        for frame in self.trames:
            ips.add(frame.ip.srcAddress)
            ips.add(frame.ip.dstAddress)
        return [address for address in ips]
        
		
		
		
