from IP import IP
from Tools import *
class TCP:
    def __init__(self, trame, sizeIP, totalSizeIP):
        self.overheadSize = sizeIP + 28 #14 bytes of frame header -> 28 hexadecimal characters
        self.tcpHeader = trame[self.overheadSize:]
        self.srcPort = self.tcpHeader[0:4]
        self.dstPort = self.tcpHeader[4:8]
        self.seqNumber = self.tcpHeader[8:16]
        self.ackNumber = self.tcpHeader[16:24]
        self.thl = self.tcpHeader[24:25] #transport header length
        self.headerLengthHex = str_to_int(self.thl)*8 # nb of 4 bit words = nb characters hex
        
        
        
        # All the flags are saved in bin 
        
        #separate flags
        reservedAndFlagsBin = str_to_bin(self.tcpHeader[25:28]) #corresponds to 12 bits, of which the last 6 are to be kept
        assert(len(reservedAndFlagsBin) == 12)
        self.flagsBin = reservedAndFlagsBin[6:]
        assert(len(self.flagsBin)==6)
        self.flags = {
            'URG':self.flagsBin[0]=='1', 
            'ACK':self.flagsBin[1]=='1', 
            'PSH':self.flagsBin[2]=='1', 
            'RST':self.flagsBin[3]=='1', 
            'SYN':self.flagsBin[4]=='1', 
            'FIN':self.flagsBin[5]=='1'
        }
        
        #window
        self.window = self.tcpHeader[28:32]
        self.checksum = self.tcpHeader[32:36]
        self.urgentPointer = self.tcpHeader[36:40]
        
        self.optionsAndPadding = self.tcpHeader[40:self.headerLengthHex]
        
        # Hacky way to do it!
        self.thlHex = str_to_int(self.thl) *8
        self.hasPayload = not (totalSizeIP == sizeIP + self.thlHex)
        firstLine = ""
        
        
        try:
            payload = self.tcpHeader[self.headerLengthHex:]
            #print(payload)
            payloadASCII = bytearray.fromhex(payload).decode()
            #print(payloadASCII)
            firstLine = payloadASCII.split("\r\n",1)
            #print(firstLine[0])
            self.hasHTTP = self.hasPayload and "HTTP" in firstLine[0]
            # print(self.hasHTTP)
        except UnicodeDecodeError:
            self.hasHTTP = False
        except ValueError:
            # self.hasHTTP = False
            print("ValueError")
            
        
        

    def printSrcPort(self):
        print(f"Port source : {str_to_int(self.srcPort)}")
        
    def printDstPort(self):
        print(f"Port destination : {str_to_int(self.dstPort)}")
        
    def printFlags(self):
        first=True
        for k,v in self.flags.items():
            if v:
                if first:
                    print(k)
                    first=False
                else:
                    print(" "+k)
                    
    def strInfo(self):
        f = ""
        for k,v in self.flags.items():
            if v:
                if f=="":
                    f+=k
                else:
                    f+=","+k
                    
        return (f"TCP: {str_to_int(self.srcPort)}->{str_to_int(self.dstPort)} [{f}] Seq: {str_to_int(self.seqNumber)} Ack: {str_to_int(self.ackNumber)} Win: {str_to_int(self.window)}")
    def getInfo(self):
        f = ""
        for k,v in self.flags.items():
            if v:
                if f=="":
                    f+=k
                else:
                    f+=","+k
        res = []
        res.append(f"TCP: {str_to_int(self.srcPort)}->{str_to_int(self.dstPort)}")
        res.append(f"Flags: [{f}]")
        res.append(f"Seq: {str_to_int(self.seqNumber)}")
        res.append(f"Ack: {str_to_int(self.ackNumber)}")
        res.append(f"Win: {str_to_int(self.window)}")
        return res

    def getShortInfo(self):
        f = ""
        for k,v in self.flags.items():
            if v:
                if f=="":
                    f+=k
                else:
                    f+=","+k
        return f"TCP:[{f}]"


                    

                
          
