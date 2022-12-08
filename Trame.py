from Tools import *
from Ethernet import Ethernet
from IP import IP
from TCP import TCP
from HTTP import HTTP


"""str : rawInput est le flux d'octets d'une seule trame, i.e. un élément d'un tabTrames de la classe RawData.py"""

class Trame:
	def __init__(self, rawInput):
		self.eth = Ethernet(rawInput)
		self.ip = IP(rawInput)
		if(self.ip.hasTCP):
			self.tcp = TCP(rawInput, self.ip.headerLengthHex, self.ip.totalLengthHex)
			if(self.tcp.hasPayload and self.tcp.hasHTTP):
				self.http = HTTP(rawInput, self.tcp.headerLengthHex, self.tcp.overheadSize)
	
	def getHighestLayer(self):
		if self.ip.hasTCP:
			if self.tcp.hasHTTP:
				return self.http
			else:
				return self.tcp
		return self.ip


