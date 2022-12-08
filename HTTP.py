from Tools import *



class HTTP:
    def __init__(self, trame, sizeTCP, overheadSize):
        # string of hex
        #self.rawHTTP = trame[sizeTCP + overheadSize:]
        #self.rawASCII = 0
        
        self.segment = trame[(sizeTCP+overheadSize):]
        self.segmentDecoded = bytearray.fromhex(self.segment).decode()
        lignes = self.segmentDecoded.split("\r\n")
        
        try:
            indexOfEmpty = lignes.index("")
            self.lignesDeLEntete, self.lignesDuCorps = (lignes[:indexOfEmpty], lignes[(indexOfEmpty+1):])
        except:
            print("ERROR!!!!")
            for line in lignes:
        	    print(line)

            print(trame[(sizeTCP+overheadSize):(sizeTCP+overheadSize+20)])
        
        #TODO
        #self.premiereLigne = 


    def getInfo(self):
        return "Replace this with actual info."
        
        
        
