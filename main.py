import sys
import traceback
from Tools import *
#from RawData import RawData
from Traffic import Traffic
from Ethernet import Ethernet
from IP import IP
from TCP import TCP
from TrafficDisplay import TrafficDisplay
from writerTrame import writerTrame
from writerTraffic import writerTraffic


def main():
    # TODO
	
	if sys.argv[1] == 0 :
		print ("usage: python3 discountwireshark.py <nom_du_fichier>")
		return
	filename = sys.argv[1]
	
	#trames = RawData(filename)
	"""
	try:									#malheureusement la version sans arguments sur la ligne de commmande ne fonctionne pas sur les macbook
		traffic = Traffic()					#création des objets
	except UnicodeDecodeError:
		print("Erreur de lecture du fichier")
		return
	except TypeError:
		print("Exécution annulée")
		return
	except:
		print("Erreur inconnue :")
		traceback.print_exc()
		return
	"""
	traffic = Traffic(filename)
	traffic_display = TrafficDisplay(traffic)	#GUI
	traffic_display.construct()
	traffic_display.run()
	
	
	
	# trames.printRawData()
	# print("trame 0")
	# print(trames.getTrame(0))
	
	
	# enteteEthernet = Ethernet(trames.getTrame(1))
	# enteteEthernet.printMacSrc()
	# enteteEthernet.printMacDst()
	# print(enteteEthernet.type)
 
 
	#enteteIP = IP(trames.getTrame(1))
	# print(enteteIP.fragmentOffset)
    # print("tset")
	# print(enteteIP.optionsAndPadding)
	#print(enteteIP.headerLengthHex)
	#enteteTCP = TCP(trames.getTrame(1), enteteIP.headerLengthHex)
	# enteteTCP.printSrcPort()
	# enteteTCP.printDstPort()
	
	# print(enteteTCP.tcpHeader)
 	# print("afh")
	#print(enteteTCP.flagsBin)
	#print(enteteTCP.URG)
	# print(str_to_bin("f0560f"))
	# s1 = "0b1010001010101001"
	# s2 = "0b1010010101010001"
	# s3 = ""
	# print(binary_sum(s1, s2))
	#print(t.lignesDeLEntete)
	#print(t.lignesDuCorps)
	# print(t.urgentPointer)
	# print(t.optionsAndPadding)
	# print(t.getInfo())
	w = writerTraffic(traffic)	#enregistrement
	
	#print(t.check_options())
	# print(f"check sum? {t.ValidPacket}")
	#print(t.check_options())



if __name__=="__main__":
	main()
