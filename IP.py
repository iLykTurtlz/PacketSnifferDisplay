from Tools import * 

class IP:
	
	def __init__(self, trame):
		datagramme = trame[28:]
		
		self.version = datagramme[0:1]
		self.headerLength = datagramme[1:2]
		
		# size of IP header in hex characters
		self.headerLengthHex = str_to_int(self.headerLength)*8
		
		self.tos = datagramme[2:4]
		self.totalLength = datagramme[4:8]
		
		self.id = datagramme[8:12]


		flagsAndFragmentOffset = datagramme[12:16]
		self.flagsBin = str_to_bin(datagramme[12])
		self.flagDF = self.flagsBin[1]
		self.flagMF = self.flagsBin[2]
		self.fragmentOffset = str_to_bin(flagsAndFragmentOffset)[3:]
  
		self.ttl = datagramme[16:18]
		self.protocol = datagramme[18:20]
		self.checksum = datagramme[20:24]
		self.srcAddress = datagramme[24:32]
		self.dstAddress = datagramme[32:40]

		#calculate remainder
		self.optionsAndPadding = datagramme[40:self.headerLengthHex]
		
	def check_checksum(self):
		pass