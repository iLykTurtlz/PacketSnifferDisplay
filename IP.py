from Tools import * 

class IP:
	
    def __init__(self, trame):
        datagramme = trame[28:]
		
        self.version = datagramme[0:1]
        self.headerLength = datagramme[1:2]
		
        # size of IP header in number of hex characters
        # a lil bit of movie magic for sure
        self.headerLengthHex = str_to_int(self.headerLength)*8
		
        self.tos = datagramme[2:4]
        
        
        self.totalLength = datagramme[4:8]
        self.totalLengthHex = str_to_int(self.totalLength)*8
		
        self.id = datagramme[8:12]


        flagsAndFragmentOffset = datagramme[12:16]
        self.flagsBin = str_to_bin(datagramme[12])
        self.flagDF = self.flagsBin[1]
        self.flagMF = self.flagsBin[2]
        self.fragmentOffset = str_to_bin(flagsAndFragmentOffset)[3:]
        self.flags = {'MF': self.flagMF==1, 'DF': self.flagDF==1}
  
        self.ttl = datagramme[16:18]
        self.protocol = datagramme[18:20]
        self.checksum = datagramme[20:24]
        self.srcAddress = datagramme[24:32]
        self.dstAddress = datagramme[32:40]

		#calculate remainder
        self.optionsAndPadding = datagramme[40:self.headerLengthHex]
        
        #basically only used for checksum verification purposes
        self.EntireIPHeader = datagramme[:self.headerLengthHex]
        self.ValidPacket = self.check_checksum()
        
        self.hasTCP = str_to_int(self.protocol) == 6

    def check_checksum(self):
        """Verifies Checksum

        Returns:
            Boolean: True if checksum is valid, False otherwise 
        """
        #print(self.EntireIPHeader)
        c = 0
        h1 = "0x0"
        for i in range(4,len(self.EntireIPHeader)+4,4) :
            h2 = "0x" + self.EntireIPHeader[c:i]
            h1 = hex_sum(h1, h2)
            c= i
            
        #pas besoin de faire le complement a 1
        return int(h1, 16) == int("0xFFFF", 16)
            
                
    def check_options(self):
        """Checks the Options present in packet

        Returns:
            [Tuple(str,str)]: tab filled with all the options present
        """
        print(self.optionsAndPadding)
        if self.optionsAndPadding == "":
            return []
        
        for letter in self.optionsAndPadding:
            pass
        
            
# Dictionnary of all IPv4 options     
IPv4options = {"0x00" : ("EOOL", 	"End of Option List"),
"0x01": ("NOP", 	"No Operation"),
"0x02": ( 	"SEC", 	"Security (defunct)"),
"0x07": ( 	"RR", 	"Record Route"),
"0x0A": (	"ZSU", 	"Experimental Measurement"),
"0x0B": (	"MTUP", 	"MTU Probe"),
"0x0C": (	"MTUR", 	"MTU Reply"),
"0x0F": (	"ENCODE", 	"ENCODE"),
"0x19": (	"QS", 	"Quick-Start"),
"0x1E": (	"EXP", 	"RFC3692-style Experiment"),
"0x44": (	"TS", 	"Time Stamp"),
"0x52": (	"TR", 	"Traceroute"),
"0x5E": (	"EXP", 	"RFC3692-style Experiment"),
"0x82": (	"SEC", 	"Security (RIPSO)"),
"0x83": (	"LSR", 	"Loose Source Route"),
"0x85": (	"E-SEC", 	"Extended Security (RIPSO)"),
"0x86": (	"CIPSO", 	"Commercial IP Security Option"),
"0x88": (   "SID", 	"Stream ID"),
"0x89": (	"SSR", 	"Strict Source Route"),
"0x8E": (	"VISA", 	"Experimental Access Control"),
"0x90": (	"IMITD", 	"IMI Traffic Descriptor"),
"0x91": (	"EIP", 	"Extended Internet Protocol"),
"0x93": (	"ADDEXT", 	"Address Extension"),
"0x94": (	"RTRALT", 	"Router Alert"),
"0x95": (	"SDB", 	"Selective Directed Broadcast"),
"0x97": ( 	"DPS", 	"Dynamic Packet State"),
"0x98": (	"UMP", 	"Upstream Multicast Packet"),
"0x9E": (	"EXP", 	"RFC3692-style Experiment"),
"0xCD": (	"FINN", 	"Experimental Flow Control"),
"0xDE": (	"EXP", "RFC3692-style Experiment")}
