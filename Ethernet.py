#import Trame

class Ethernet:
	def __init__(self, trame):
		
		#Adresse MAC Destination
		self.dst = trame[0:12]
		res = "("
		i = 1
		for letter in self.dst :
			res+=letter
			if i%2 == 0 :
				res+=":"
			i+=1
		res = res.rstrip(res[-1])
		res+=")"
		self.dst = res
		
		#Adresse MAC Source
		self.src = trame[12:24]
		res = "("
		i = 1
		for letter in self.src :
			res+=letter
			if i%2 == 0 :
				res+=":"
			i+=1
		res = res.rstrip(res[-1])
		res+=")"
		self.src = res
		
		self.type = trame[24:28]
		
		
	def printMacSrc(self):
		print(f"Adresse MAC source = {self.src}")

		
	def printMacDst(self):
		print(f"Adresse MAC destination = {self.dst}")
		
	def strType(self):
		if self.type == "0800":
			return "IP"
		if self.type == "0806":
			return "ARP"
		return "Unknown"

	def getInfo(self):
		res = []
		res.append(f"Ethernet: ")
		res.append(f"Adresse MAC src: {self.src}")
		res.append(f"Adresse MAC dst: {self.dst}")
		res.append(f"Type 0x{self.type}: {self.strType()}")
		return res
