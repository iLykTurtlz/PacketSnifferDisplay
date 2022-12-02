from IP import IP
from Tools import *
class TCP:
    def __init__(self, trame, sizeIP):
        self.overheadSize = sizeIP + 28
        self.tcpHeader = trame[self.overheadSize:]
        self.srcPort = self.tcpHeader[0:4]
        self.dstPort = self.tcpHeader[4:8]
        self.seqNumber = self.tcpHeader[8:16]
        self.ackNumber = self.tcpHeader[16:24]
        self.thl = self.tcpHeader[24:25]
        
        # All the flags are saved in bin 
        
        #separate falgs
        self.flagsBin = bin(str_to_int(self.tcpHeader[25:28]))[2:]
        
        #testing
        self.URG = 0
                
        # And then affected accordingly
        # self.URG = self.flagsBin[1]

    def printSrcPort(self):
        res = str_to_int(self.srcPort)
        print(f"Port source : {str_to_int(self.srcPort)}")
        
    def printDstPort(self):
        print(f"Port destination : {str_to_int(self.dstPort)}")