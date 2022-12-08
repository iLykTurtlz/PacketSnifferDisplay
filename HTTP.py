from Tools import *



class HTTP:
    def __init__(self, trame, sizeTCP, overheadSize):
        # string of hex
        #self.rawHTTP = trame[sizeTCP + overheadSize:]
        #self.rawASCII = 0
        
        self.segment = trame[(sizeTCP+overheadSize):]
        self.segmentDecoded = bytearray.fromhex(self.segment).decode()
        lignes = self.segmentDecoded.split("\r\n")
        self.lignesDeLEntete = []
        self.lignesDuCorps = []
        try:
            indexOfEmpty = lignes.index("")
            self.lignesDeLEntete, self.lignesDuCorps = (lignes[:indexOfEmpty], lignes[(indexOfEmpty+1):])
        except:
            print("ERROR!!!!")
            for line in lignes:
                print(line)

            print(trame[(sizeTCP+overheadSize):(sizeTCP+overheadSize+20)])
        
        try:
            self.premiereLigne = self.lignesDeLEntete[0]
            self.methode = self.premiereLigne.split(" ")[0]
            self.URL = self.premiereLigne.split(" ")[1]
            self.version = self.premiereLigne.split(" ")[2]
            
        except:
            self.methode = "?"
            self.URL = "?"
            self.version = "?"
            
        try:
            self.lignesDuCorpsTraduits = []
            tmp = []
            for ligne in self.lignesDeLEntete:
                tmp = []
                for champ in ligne.split(" "):
                    tmp.append(champ)
                try:
                    self.lignesDuCorpsTraduits.append(f"FIELD: {tmp[0]} {tmp[1]}")
                except:
                    self.lignesDuCorpsTraduits.append("FIELD: ?, VALUE: ?")
                
        except:
            self.lignesDuCorpsTraduits = []
                    
            


    def getInfo(self):
        """Generates a tab with all the HTTP info of the packet

        Returns:
            [str] : Each str represents a field of HTML
        """
        res = []
        res.append("VERSION: "+self.version)
        res.append(" "+self.methode)
        res.append("URL: "+self.URL)
        # res.append("\n")
        
        if(self.lignesDuCorpsTraduits != []):
            for line in self.lignesDuCorpsTraduits:
                res.append(line)
        return res
        
    def getShortInfo(self):
        return f"HTTP:{self.version} {self.methode}"
        
        
