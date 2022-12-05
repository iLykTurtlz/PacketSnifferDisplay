from Tools import *
from Ethernet import Ethernet
from IP import IP
from TCP import TCP
from RawData import RawData

"""str : rawInput est le flux d'octets d'une seule trame, i.e. un élément d'un tabTrames de la classe RawData.py"""

class Trame:
	def __init__(self, str : rawInput):
		self.eth = Ethernet(rawInput)
		self.ip = IP(rawInput)
		self.tcp = TCP(rawInput, self.ip.headerLengthHex)
		self.http = HTTP(rawInput, self.tcp.headerLengthHex, self.tcp.overheadSize)
	
	
		
		
		
