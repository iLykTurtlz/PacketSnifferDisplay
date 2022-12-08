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

	def has(self, protocol):
		if protocol == "IP":
			return True
		elif protocol == "TCP":
			return self.ip.hasTCP
		elif self.ip.hasTCP and protocol == "HTTP":
			return self.tcp.hasHTTP
		return False

	def getInfo(self):
		"""Returns an array full with all the information of the given packet
  
		Type :
			[str] -> Each case contains a single bit (as in piece) of info
		"""
		res = self.eth.getInfo() + self.ip.getInfo()
		if(self.ip.hasTCP):
			res = res + self.tcp.getInfo()
			if(self.tcp.hasPayload and self.tcp.hasHTTP):
				res = res + self.http.getInfo()
		res.append("\n")
		return res



  
  