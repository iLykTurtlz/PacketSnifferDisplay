"""
ORIGINAL PYTHON SCRIPT WRITTEN
Kept for posterity sake
"""
import sys
def printRawData(tabTrames):
	cpt=0
	for trame in tabTrames :
		if(trame == ""):
			return
		print("Trame "+str(cpt))
		cpt+=1
		print(trame)

 
# Lit l'entete ETHERNET
# Recoit une sequence d'octets
def readEthernet(trame) :
	tabEthernet= []
	tabEthernet.append(trame[0:12])
	tabEthernet.append(trame[12:24])
	tabEthernet.append(trame[24:28])
	return tabEthernet


def printMacAddress(tempMac, origin):
	res = "("
	i = 1
	for letter in tempMac :
		res+=letter
		if i%2 == 0 :
			res+=":"
		i+=1
	res = res.rstrip(res[-1])
	res+=")"
	print("Addresse MAC "+origin+" = "+res)
	


def getInput(filename) :
	f = open(filename, 'r')
	# Ethernet reader
	tabTrames = []
	nTrame = -1
	rawInput = ""
	for line in f :	
		offset = line[0:4]
		if (offset == "0000") :
			nTrame+=1
		tabTrames.append("")
		line = line.lstrip(offset)
		line = line.replace("\n", "")
		line = line.replace(" ", "")
		rawInput += line
		tabTrames[nTrame]+=line
	f.close
	return tabTrames
	
	

def main() :
	if sys.argv[1] == 0 :
		print ("usage: python3 discountwireshark.py <nom_du_fichier>")
		return
	filename = sys.argv[1]
	tabTrames = getInput(filename)
	
	
	#test
	printRawData(tabTrames)
	enteteEthernet = readEthernet(tabTrames[1])
	printMacAddress(enteteEthernet[0], "dest")
	
	
	
	
	
	
	
	
	
	
if __name__ == "__main__":
	main()
