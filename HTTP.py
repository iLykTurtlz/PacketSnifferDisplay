from Tools import *



class HTTP:
    def __init__(self, trame, sizeTCP, overheadSize):
        # string of hex
        #self.rawHTTP = trame[sizeTCP + overheadSize:]
        #self.rawASCII = 0
        
        self.segment = trame[(sizeTCP+overheadSize):]
        self.segmentDecoded = bytearray.fromhex(self.segment).decode()
        lignes = self.segmentDecoded.split("\r\n")
        self.lignesDeLEntete, self.lignesDuCorps = (lignes[:lignes.index("")], lignes[(lignes.index("")+1):])
        
        
        #TODO
        #self.premiereLigne = 
        
        
        
